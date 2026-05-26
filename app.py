import streamlit as st
import numpy as np
import joblib


st.set_page_config(
    page_title="Student CGPA Predictor",
    page_icon="",
    layout="centered"
)

model = joblib.load("cgpa_predictor_model.pkl")



st.title(" Student CGPA Predictor")

st.write("Predict student CGPA using Machine Learning Model")

st.write("---")



attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=85.0
)

internal_marks = st.number_input(
    "Internal Marks",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

backlogs = st.number_input(
    "Number of Backlogs",
    min_value=0,
    max_value=10,
    value=1
)


if st.button("Predict CGPA"):

    input_data = np.array([
        [attendance, internal_marks, backlogs]
    ])

   
    prediction = model.predict(input_data)

    
    predicted_cgpa = float(prediction[0][0])

 
    st.success(f"Predicted CGPA: {predicted_cgpa:.2f}")


    if predicted_cgpa >= 8.5:
        st.info("Excellent Performance")

    elif predicted_cgpa >= 7.0:
        st.info("Good Performance ")

    elif predicted_cgpa >= 5.0:
        st.warning("Average Performance ")

    else:
        st.error("Needs Improvement ")



st.write("---")
st.caption("Built using Streamlit and Deep Learning Model")