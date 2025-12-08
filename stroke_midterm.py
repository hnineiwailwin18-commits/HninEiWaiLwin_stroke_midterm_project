import streamlit as st
import pickle
import os
import pandas as pd

st.title("Stroke Prediction App")

with open("stroke_midterm.pkl", "rb") as file:
    model = pickle.load(file)

logo_path = "images/parami.jpg"
if os.path.exists(logo_path):
    st.sidebar.image(logo_path, width=150)
    
st.sidebar.markdown("**Student Name:** Hnin Ei Wai Lwin")
st.sidebar.markdown("**Student ID:** PIUS20230022")

name= st.text_input("Your Name")


gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=120, value=10)
hypertension = st.selectbox("Hypertension", ["Yes", "No"])
heart_disease = st.selectbox("Heart Disease", ["Yes", "No"])
ever_married = st.selectbox("Ever Married", ["Yes", "No"])
work_type = st.selectbox("Work Type", ["Private", "Self-employed", "Govt_job", "children", "Never_worked"])
Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])
avg_glucose_level = st.slider("Average Glucose Level", min_value=50.0, max_value=300.0, value=100.0)
bmi = st.slider("BMI", min_value=10.0, max_value=60.0, value=25.0)
smoking_status = st.selectbox("Smoking Status", ["formerly smoked", "never smoked", "smokes", "Unknown"])

columns = [
    "gender", "age", "hypertension", "heart_disease", "ever_married",
    "work_type", "Residence_type", "avg_glucose_level", "bmi", "smoking_status"
]

if st.button("Predict Stroke"):
    
    hypertension_val=1 if hypertension == "Yes" else 0
    heart_disease_val=1 if heart_disease == "Yes" else 0

    data = pd.DataFrame([{
        "gender": gender,
        "age": age,
        "hypertension": hypertension_val,
        "heart_disease": heart_disease_val,
        "ever_married": ever_married,
        "work_type": work_type,
        "Residence_type": Residence_type,
        "avg_glucose_level": avg_glucose_level,
        "bmi": bmi,
        "smoking_status": smoking_status
    }], columns=columns)

    prediction = model.predict(data)

    if prediction[0] == 1:
        if name:
            st.error(f"{name}, you jave a High Risk of Stroke.")
        else:
            st.error("High Risk of Stoke")
    else:
        if name:
            st.success(f"{name}, you have a Low Risk of Stroke.")
        else:

            st.success("Low Risk of Stroke")


