Student CGPA Predictor Using Artificial Neural Networks (ANN)
 Overview

The Student CGPA Predictor is a Deep Learning mini project developed using an Artificial Neural Network (ANN).
The model predicts a student's CGPA based on academic performance indicators such as attendance, internal marks, and number of backlogs.

This project demonstrates a complete regression pipeline using TensorFlow and Keras, including data preprocessing, model training, evaluation, and visualization.

 Objective

The main objectives of this project are:

Predict student CGPA using deep learning techniques
Understand ANN architecture for regression problems
Perform data preprocessing and feature scaling
Train and evaluate a neural network model
Visualize training performance and loss trends
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
TensorFlow / Keras	Building and training ANN model
NumPy	Numerical computations
Pandas	Data handling and processing
Matplotlib	Data visualization
Scikit-learn	Data preprocessing and evaluation
 Project Structure
CGPA-Predictor-ANN/
│
├── cgpa_predictor.py          # Main ANN model script
├── student_cgpa_dataset.csv   # Dataset used for training
├── requirements.txt           # Required dependencies
├── README.md                  # Project documentation
📊 Dataset Description
Input Features:
Attendance Percentage
Internal Marks
Number of Backlogs
Output:
CGPA (Continuous value)
🧠 ANN Model Architecture
Input Layer (3 features)
        ↓
Hidden Layer 1 (16 neurons, ReLU)
        ↓
Hidden Layer 2 (8 neurons, ReLU)
        ↓
Output Layer (1 neuron, Linear activation)
⚙️ Model Configuration
Optimizer: Adam
Loss Function: Mean Squared Error (MSE)
Evaluation Metric: Mean Absolute Error (MAE)
🚀 Workflow
Import required libraries
Load and preprocess dataset
Split dataset into training and testing sets
Apply feature scaling
Build ANN model using Keras
Train the model
Evaluate performance
Make predictions
Visualize training & validation loss
📈 Performance Visualization

The model generates training graphs showing:

Training Loss
Validation Loss

These help in analyzing:

Model convergence
Overfitting/underfitting
Training performance
 How to Run the Project
1. Install Dependencies
pip install -r requirements.txt
2. Run the Application
python cgpa_predictor.py
 Sample Prediction
Input:
Attendance: 85
Internal Marks: 80
Backlogs: 1
Output:
Predicted CGPA ≈ 8.0
 Advantages
Simple and beginner-friendly ANN implementation
Demonstrates real-world regression use case
Helps understand deep learning workflow
Easily extendable for improvements
 Future Enhancements
Expand dataset for better accuracy
Add dropout layers to reduce overfitting
Deploy as a web application using Flask/Streamlit
Compare ANN with traditional ML models
Improve feature engineering
 Developed Using
TensorFlow
Keras
Python Deep Learning Stack

 Conclusion
This project successfully demonstrates how an Artificial Neural Network can be used to predict student CGPA. It covers the full lifecycle of a deep learning regression model, including preprocessing, training, evaluation, and prediction.
