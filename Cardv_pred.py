import streamlit as st
import pickle
import numpy as np
from PIL import Image

# Load the model
with open('cardiovascular_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Page settings
st.set_page_config(page_title="Cardiovascular Risk Predictor", layout="wide")

# Load and display heart image
image = Image.open("heart.png")  # Make sure this file exists in your working directory
st.image(image, caption="Know Your Heart Health ❤️", use_container_width=True)

# App title and description
st.title("🫀 Cardiovascular Disease Risk Predictor")
st.markdown("""
This app uses a machine learning model to predict the risk of cardiovascular disease based on health parameters. 
Please fill in the details below and click **Predict** to see your result.
""")

# User Inputs
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 20, 80, 30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    sex = 1 if sex == "Male" else 0

    chest_pain = st.selectbox("Chest Pain Type", [
        "Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    chest_pain_dict = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-anginal Pain": 2,
        "Asymptomatic": 3
    }
    chest_pain = chest_pain_dict[chest_pain]

    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)

    cholesterol = st.selectbox("Cholesterol Level", [
        "Normal (<200)", "Borderline High (200-239)", "High (≥240)"])
    cholesterol_dict = {
        "Normal (<200)": 1,
        "Borderline High (200-239)": 2,
        "High (≥240)": 3
    }
    cholesterol = cholesterol_dict[cholesterol]

with col2:
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["No", "Yes"])
    fasting_bs = 1 if fasting_bs == "Yes" else 0

    resting_ecg = st.selectbox("Resting ECG Results", [
        "Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
    resting_ecg_dict = {
        "Normal": 0,
        "ST-T Wave Abnormality": 1,
        "Left Ventricular Hypertrophy": 2
    }
    resting_ecg = resting_ecg_dict[resting_ecg]

    max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)

    exercise_angina = st.selectbox("Exercise-Induced Angina?", ["No", "Yes"])
    exercise_angina = 1 if exercise_angina == "Yes" else 0

    oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=6.0, value=1.0, step=0.1)

    st_slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])
    st_slope_dict = {
        "Upsloping": 0,
        "Flat": 1,
        "Downsloping": 2
    }
    st_slope = st_slope_dict[st_slope]

# Prediction
if st.button("🔍 Predict"):
    input_data = np.array([[age, sex, chest_pain, resting_bp, cholesterol,
                            fasting_bs, resting_ecg, max_hr, exercise_angina,
                            oldpeak, st_slope]])

    prediction = model.predict(input_data)
    result = "Yes" if prediction[0] == 1 else "No"

    st.markdown("---")
    st.subheader("🩺 Prediction Result")
    st.success(f"✅ Cardiovascular Disease Risk: **{result}**")

    with st.expander("🔍 View Input Summary"):
        st.json({
            "Age": age,
            "Sex": "Male" if sex == 1 else "Female",
            "Chest Pain Type": list(chest_pain_dict.keys())[list(chest_pain_dict.values()).index(chest_pain)],
            "Resting Blood Pressure": resting_bp,
            "Cholesterol": list(cholesterol_dict.keys())[list(cholesterol_dict.values()).index(cholesterol)],
            "Fasting Blood Sugar > 120 mg/dl": "Yes" if fasting_bs == 1 else "No",
            "Resting ECG": list(resting_ecg_dict.keys())[list(resting_ecg_dict.values()).index(resting_ecg)],
            "Max Heart Rate": max_hr,
            "Exercise-Induced Angina": "Yes" if exercise_angina == 1 else "No",
            "Oldpeak": oldpeak,
            "ST Slope": list(st_slope_dict.keys())[list(st_slope_dict.values()).index(st_slope)]
        })

