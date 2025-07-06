import streamlit as st
import pandas as pd
import time

# Page Config
st.set_page_config(page_title="🌟 Streamlit Multipurpose App", layout="wide")

# Title and Description
st.title("🌟 Welcome to My Streamlit App")
st.write("An interactive multipurpose app built with Streamlit.")

# Sidebar for Navigation
st.sidebar.title("🔍 Navigation")
app_mode = st.sidebar.selectbox("Choose a section", ["Home", "About", "Contact", "Upload", "Chart", "Widgets", "Progress", "HTML Section"])

# Main App Logic
if app_mode == "Home":
    st.header("🏠 Home")
    st.write("This is the home page.")

    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! Welcome to the app.")

    st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=250)

elif app_mode == "About":
    st.header("ℹ️ About")
    st.write("""
        📌 This multipurpose app is built using **Streamlit**.  
        You can upload files, view data, interact with charts, pick dates, and more!
        """)

elif app_mode == "Contact":
    st.header("📬 Contact Us")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    if st.button("Submit"):
        st.success(f"Thanks {email}! We'll get back to you soon.")

elif app_mode == "Upload":
    st.header("📤 Upload Your Data")
    uploaded_file = st.file_uploader("Choose a CSV or Excel file", type=["csv", "xlsx"])
    if uploaded_file:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.write("✅ Uploaded Data Preview:")
        st.dataframe(df)

elif app_mode == "Chart":
    st.header("📊 Data Visualization")
    data = pd.DataFrame({
        'Products': ['Laptop', 'Mobile', 'Tablet', 'Smartwatch'],
        'Sales': [150, 250, 100, 180]
    })
    st.bar_chart(data.set_index('Products'))

elif app_mode == "Widgets":
    st.header("🎛️ Interactive Widgets")

    num = st.slider("Select a number", 0, 100, 50)
    st.write(f"You selected: {num}")

    date = st.date_input("Pick a date")
    st.write(f"Date selected: {date}")

    time_picker = st.time_input("Pick a time")
    st.write(f"Time selected: {time_picker}")

    img_upload = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])
    if img_upload:
        st.image(img_upload, caption="Uploaded Image", use_column_width=True)

elif app_mode == "Progress":
    st.header("⏳ Progress Bar Demo")

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    st.success("Done!")

elif app_mode == "HTML Section":
    st.header("💻 Custom HTML / CSS Section")
    st.markdown("""
        <style>
        .custom {
            font-size:20px;
            color:#ff4b4b;
            font-weight:bold;
        }
        </style>
        <p class='custom'>This is a styled text using custom CSS inside Streamlit.</p>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit | Demo App by Vijaya Sri Manda")
