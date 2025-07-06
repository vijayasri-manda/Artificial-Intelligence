# import streamlit as st
# import requests
# import pandas as pd
#
# # App Title and Layout
# st.set_page_config(page_title="COVID-19 Tracker", layout="centered")
#
# st.title("🦠 COVID-19 Global & Country-wise Statistics")
# st.write("Live data fetched from [disease.sh](https://disease.sh/)")
#
# # Function to fetch data
# def get_global_data():
#     url = "https://disease.sh/v3/covid-19/all"
#     response = requests.get(url)
#     return response.json()
#
# def get_country_data():
#     url = "https://disease.sh/v3/covid-19/countries"
#     response = requests.get(url)
#     return response.json()
#
# # Fetch Data
# global_data = get_global_data()
# country_data = get_country_data()
#
# # Display Global Data
# st.subheader("🌍 Global Statistics")
#
# st.metric("Total Cases", f"{global_data['cases']:,}")
# st.metric("Total Deaths", f"{global_data['deaths']:,}")
# st.metric("Total Recovered", f"{global_data['recovered']:,}")
#
# st.markdown("---")
#
# # Country-wise Data
# st.subheader("🏳️ Country-wise Statistics")
#
# # Create DataFrame
# df = pd.DataFrame(country_data)
# df = df[['country', 'cases', 'deaths', 'recovered', 'active']]
# df = df.sort_values(by='cases', ascending=False)
#
# # Show Country Selector
# country_list = df['country'].tolist()
# selected_country = st.selectbox("Select a Country", country_list)
#
# # Show Selected Country Stats
# country_stats = df[df['country'] == selected_country]
#
# st.write(f"**Stats for {selected_country}**")
# st.dataframe(country_stats)
#
# # Display Full Table
# if st.checkbox("Show full country list"):
#     st.dataframe(df.reset_index(drop=True))
#
# st.markdown("---")
# st.write("📊 Data Source: [disease.sh](https://disease.sh/) API")
#


import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="🌍 COVID-19 Dashboard with Date Range", layout="wide")
st.title("🦠 COVID-19 Dashboard with Date & Country Selection")
st.caption(f"📅 Today: {datetime.now().strftime('%A, %d %B %Y')}")
st.markdown("Live data from [disease.sh](https://disease.sh)")


# --------------- Helper Functions -----------------

@st.cache_data
def get_country_list():
    try:
        res = requests.get("https://disease.sh/v3/covid-19/countries").json()
        countries = sorted([item['country'] for item in res])
        return ["Worldwide"] + countries
    except:
        return ["Worldwide"]


def get_current_data(country):
    url = "https://disease.sh/v3/covid-19/all" if country == "Worldwide" else f"https://disease.sh/v3/covid-19/countries/{country}"
    try:
        return requests.get(url).json()
    except:
        return {}


def get_historical_data(country):
    # Fetch max lastdays=90 data and filter by user locally
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=90" if country == "Worldwide" else f"https://disease.sh/v3/covid-19/historical/{country}?lastdays=90"
    try:
        data = requests.get(url).json()
        return data if country == "Worldwide" else data.get("timeline", {})
    except:
        return {}


def filter_by_date(df, start_date, end_date):
    return df.loc[(df.index >= start_date) & (df.index <= end_date)]


# --------------- Sidebar -------------------

with st.sidebar:
    st.header("🌎 Select Region & Date Range")
    country = st.selectbox("Country/Region", get_country_list())

    today = datetime.today()
    default_start = today - timedelta(days=30)
    start_date = st.date_input("Start date", default_start, max_value=today)
    end_date = st.date_input("End date", today, min_value=start_date, max_value=today)

    if start_date > end_date:
        st.error("Error: End date must fall after start date.")

# --------------- Main -------------------

with st.spinner("Fetching data..."):
    current = get_current_data(country)
    history = get_historical_data(country)

if current and history:
    st.subheader(f"📍 COVID-19 Stats for {country}")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Cases", f"{current.get('cases', 0):,}")
    col2.metric("Recovered", f"{current.get('recovered', 0):,}")
    col3.metric("Deaths", f"{current.get('deaths', 0):,}")
    col4.metric("Active", f"{current.get('active', 0):,}")

    # Convert timeline dict to DataFrame
    df = pd.DataFrame(history)
    df.index = pd.to_datetime(df.index, format='%m/%d/%y')
    df = df.sort_index()

    # Filter by selected dates
    df_filtered = filter_by_date(df, pd.to_datetime(start_date), pd.to_datetime(end_date))

    if df_filtered.empty:
        st.warning("No data available for the selected date range.")
    else:
        df_daily = df_filtered.diff().fillna(0)

        tabs = st.tabs(["📈 Cumulative", "📉 Daily New Cases"])

        with tabs[0]:
            st.markdown(f"### Cumulative Trends ({start_date.strftime('%d %b %Y')} - {end_date.strftime('%d %b %Y')})")
            fig_line = px.line(
                df_filtered,
                x=df_filtered.index,
                y=["cases", "recovered", "deaths"],
                labels={"value": "Count", "index": "Date", "variable": "Metric"},
                title="Cumulative COVID-19 Trends"
            )
            fig_line.update_yaxes(tickformat=",")
            st.plotly_chart(fig_line, use_container_width=True)

        with tabs[1]:
            st.markdown(f"### Daily New Cases ({start_date.strftime('%d %b %Y')} - {end_date.strftime('%d %b %Y')})")
            fig_bar = px.bar(
                df_daily,
                x=df_daily.index,
                y="cases",
                labels={"cases": "New Cases", "index": "Date"},
                title="Daily New Cases"
            )
            fig_bar.update_yaxes(tickformat=",")
            st.plotly_chart(fig_bar, use_container_width=True)
else:
    st.error("Failed to fetch data. Check your internet connection or try again.")

