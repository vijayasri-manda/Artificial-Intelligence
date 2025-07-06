import streamlit as st

st.title("🩺 Healthcare Disease Prediction & Diet Plan")

st.markdown("""
Enter your medical values and symptoms below, select the disease to get personalized health advice and a diet plan.
""")

# Input medical values
glucose = st.number_input("Glucose level (mg/dL)", min_value=40, max_value=300, value=100)
bp = st.number_input("Blood Pressure (mm Hg)", min_value=60, max_value=200, value=80)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=100, max_value=400, value=180)
bmi = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, value=22.0)
age = st.number_input("Age (years)", min_value=1, max_value=120, value=30)

# Symptoms input (simple example)
symptoms = st.multiselect(
    "Select your symptoms",
    ["Fatigue", "Frequent urination", "Blurred vision", "Chest pain", "Shortness of breath", "Swelling", "Dizziness"]
)

# Disease selection
disease = st.selectbox("Select Disease to check", ["Diabetes", "Heart Disease"])


# Simple prediction logic (dummy, replace with model)
def predict_disease(glucose, bp, cholesterol, bmi, age, symptoms, disease):
    risk = 0
    if disease == "Diabetes":
        risk += (glucose > 125) * 2
        risk += (bmi > 25) * 1
        risk += ("Frequent urination" in symptoms) * 2
        risk += ("Fatigue" in symptoms) * 1
        risk += (age > 45) * 1
    elif disease == "Heart Disease":
        risk += (bp > 140) * 2
        risk += (cholesterol > 240) * 2
        risk += ("Chest pain" in symptoms) * 3
        risk += ("Shortness of breath" in symptoms) * 2
        risk += (age > 50) * 1

    if risk >= 4:
        return "High Risk"
    elif risk >= 2:
        return "Moderate Risk"
    else:
        return "Low Risk"


# Diet plans for diseases
diet_plans = {
    "Diabetes": """
- Eat more fiber-rich foods (vegetables, fruits, whole grains)
- Avoid sugary drinks and sweets
- Opt for lean proteins like fish and chicken
- Limit saturated and trans fats
- Monitor carbohydrate intake and prefer low glycemic index foods
- Stay hydrated
""",
    "Heart Disease": """
- Eat plenty of fruits and vegetables
- Choose whole grains over refined grains
- Include healthy fats (olive oil, nuts, avocado)
- Limit salt intake to control blood pressure
- Avoid processed and fried foods
- Maintain a healthy weight through balanced diet and exercise
"""
}

if st.button("Get Prediction & Diet Plan"):
    prediction = predict_disease(glucose, bp, cholesterol, bmi, age, symptoms, disease)
    st.subheader(f"🩺 Prediction Result: {prediction}")

    if prediction == "High Risk":
        st.error("You are at HIGH RISK. Please consult a healthcare professional immediately.")
    elif prediction == "Moderate Risk":
        st.warning("You have MODERATE RISK. Consider lifestyle changes and regular check-ups.")
    else:
        st.success("You have LOW RISK. Maintain a healthy lifestyle!")

    st.subheader(f"🍽️ Recommended Diet Plan for {disease}")
    st.markdown(diet_plans[disease])

    st.subheader("💡 Additional Health Tips")
    if disease == "Diabetes":
        st.write("""
        - Exercise regularly (at least 30 mins/day)
        - Monitor blood sugar levels regularly
        - Avoid smoking and limit alcohol consumption
        """)
    else:
        st.write("""
        - Manage stress levels
        - Monitor blood pressure regularly
        - Get regular cardiovascular exercise
        - Avoid smoking and limit alcohol consumption
        """)
