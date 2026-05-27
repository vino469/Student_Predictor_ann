import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


st.set_page_config(page_title="CGPA Predictor", page_icon="🎓")

st.title(" Student CGPA Predictor")
st.write("Predict CGPA using Artificial Neural Network (ANN)")


df = pd.read_csv("student_cgpa_dataset.csv")

# CLEAN COLUMN NAMES (IMPORTANT FIX)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")


X = df[["attendance", "internal_marks", "backlogs"]].values
y = df["cgpa"].values.reshape(-1, 1)


x_scaler = MinMaxScaler()
y_scaler = MinMaxScaler()

X_scaled = x_scaler.fit_transform(X)
y_scaled = y_scaler.fit_transform(y)


model = Sequential([
    Dense(16, input_dim=3, activation='relu'),
    Dense(8, activation='relu'),
    Dense(1, activation='linear')
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])


model.fit(X_scaled, y_scaled, epochs=80, batch_size=4, verbose=0)


attendance = st.number_input("Attendance Percentage", 0.0, 100.0, 80.0)
internal_marks = st.number_input("Internal Marks", 0.0, 100.0, 75.0)
backlogs = st.number_input("Number of Backlogs", 0, 10, 0)


if st.button("Predict CGPA"):
    
    input_data = np.array([[attendance, internal_marks, backlogs]])
    

    input_scaled = x_scaler.transform(input_data)
    
 
    pred_scaled = model.predict(input_scaled)
    

    pred = y_scaler.inverse_transform(pred_scaled)

    cgpa = float(pred[0][0])

    st.success(f" Predicted CGPA: {cgpa:.2f}")

    # performance label
    if cgpa >= 8:
        st.info("Excellent Performance")
    elif cgpa >= 6:
        st.info(" Good Performance")
    else:
        st.warning(" Need Improvement")
