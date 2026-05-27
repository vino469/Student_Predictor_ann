Student CGPA Predictor Using Artificial Neural Networks (ANN)
 Project Overview

The Student CGPA Predictor is a Deep Learning-based regression project developed using an Artificial Neural Network (ANN) with TensorFlow and Keras.

The model predicts a student’s CGPA based on academic performance indicators such as attendance, internal assessment marks, and number of backlogs.

This project demonstrates a complete machine learning workflow including data preprocessing, ANN model development, training, evaluation, and visualization.

 Objective
To predict student CGPA using deep learning techniques
To implement Artificial Neural Networks for regression problems
To perform data preprocessing and feature scaling
To evaluate model performance using appropriate metrics
To visualize training and validation results
🛠️ Technologies Used
Technology	Purpose
Python	Programming language
TensorFlow / Keras	Deep Learning framework
NumPy	Numerical computations
Pandas	Data manipulation
Matplotlib	Data visualization
Scikit-learn	Data preprocessing & evaluation
 Project Structure
CGPA-Predictor-ANN/
│
├── cgpa_predictor.py          # Main ANN model implementation
├── student_cgpa_dataset.csv   # Dataset used for training
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
 Dataset Description
Input Features:
Attendance Percentage
Internal Marks
Number of Backlogs
Output:
CGPA (Continuous numerical value)
 Model Architecture

The Artificial Neural Network is designed as follows:

Input Layer: 3 features
Hidden Layer 1: 16 neurons (ReLU activation)
Hidden Layer 2: 8 neurons (ReLU activation)
Output Layer: 1 neuron (Linear activation for regression)
 Model Configuration
Optimizer: Adam
Loss Function: Mean Squared Error (MSE)
Evaluation Metric: Mean Absolute Error (MAE)
 Workflow
Import required libraries
Load dataset
Perform data preprocessing
Split dataset into training and testing sets
Apply feature scaling
Build ANN model
Train the model
Evaluate performance
Make predictions
Visualize training results
📈 Model Performance

The model training process includes visualization of:

Training Loss
Validation Loss

These graphs help in analyzing model convergence and detecting overfitting or underfitting.

 Installation & Execution
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
 Key Features
Simple and efficient ANN-based regression model
Beginner-friendly deep learning implementation
Real-world academic performance prediction
Clear visualization of model performance
Easily extensible for improvements
 Future Enhancements
Increase dataset size for better accuracy
Add dropout layers to reduce overfitting
Deploy as a web application using Streamlit/Flask
Compare ANN with other machine learning models
Improve feature engineering techniques
 Developed Using
TensorFlow
Keras
Python
 Conclusion

This project demonstrates the practical application of Artificial Neural Networks for predicting student academic performance. It provides a complete deep learning pipeline from data preprocessing to model evaluation.
