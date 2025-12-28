import streamlit as st
import numpy as np
import joblib

# --------------------------------
# Load model and scaler
# --------------------------------
model = joblib.load("exam_score_model.pkl")
scaler = joblib.load("scaler.pkl")

# --------------------------------
# App Configuration
# --------------------------------
st.set_page_config(
    page_title="Student Performance Score Predictor",
    layout="centered"
)

# --------------------------------
# Title
# --------------------------------
st.markdown(
    "<h1 style='text-align:center;'>Student Performance Score Predictor</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# --------------------------------
# Input Sliders
# --------------------------------
study_hours = st.number_input("Study Hours per Day", 0.0, 12.0, 2.0, step=0.5)
social_media = st.number_input("Social Media Hours", 0.0, 10.0, 2.0, step=0.5)
netflix = st.number_input("Netflix Hours", 0.0, 10.0, 1.0, step=0.5)
attendance = st.number_input("Attendance Percentage", 0.0, 100.0, 80.0, step=1.0)
sleep = st.number_input("Sleep Hours per Night", 3.0, 10.0, 7.0, step=0.5)
exercise = st.number_input("Exercise Frequency (per week)", 0, 7, 3)
mental_health = st.number_input("Mental Health Rating (1–10)", 1, 10, 7)

st.markdown("<br>", unsafe_allow_html=True)

# --------------------------------
# Predict Button
# --------------------------------
if st.button("Predict Exam Score", use_container_width=True):

    input_data = np.array([[study_hours, social_media, netflix,
                            attendance, sleep, exercise, mental_health]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    st.markdown("---")

    st.markdown(
        "<h2 style='text-align:center;'>Predicted Exam Score</h2>",
        unsafe_allow_html=True
    )

    st.metric(
        label="Expected Score",
        value=f"{prediction:.2f}"
    )
