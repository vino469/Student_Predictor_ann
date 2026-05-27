Student CGPA Predictor Using Artificial Neural Networks (ANN)


The **Student CGPA Predictor** is a Deep Learning regression project built using an **Artificial Neural Network (ANN)** with TensorFlow and Keras.

The system predicts a student’s CGPA based on academic performance factors such as attendance percentage, internal marks, and number of backlogs.

This project demonstrates an end-to-end machine learning workflow including data preprocessing, ANN model development, training, evaluation, and performance visualization.



- Develop a regression model using Artificial Neural Networks  
- Predict student CGPA using academic performance features  
- Implement data preprocessing and feature scaling techniques  
- Evaluate model performance using regression metrics  
- Visualize training and validation results  

---


- **Programming Language:** Python  
- **Deep Learning Framework:** TensorFlow, Keras  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib  
- **Machine Learning Utilities:** Scikit-learn  

---




CGPA-Predictor-ANN/
│
├── cgpa_predictor.py # Main ANN model implementation
├── student_cgpa_dataset.csv # Dataset used for training
├── requirements.txt # Required dependencies
└── README.md # Project documentation


---

## 📊 Dataset Description

### Input Features:
- Attendance Percentage  
- Internal Marks  
- Number of Backlogs  

### Output Variable:
- CGPA (Continuous numerical value)

---

## 🧠 Model Architecture

The Artificial Neural Network consists of:

- Input Layer: 3 Features  
- Hidden Layer 1: 16 Neurons (ReLU Activation)  
- Hidden Layer 2: 8 Neurons (ReLU Activation)  
- Output Layer: 1 Neuron (Linear Activation)

---

## ⚙️ Model Configuration

- Optimizer: **Adam**  
- Loss Function: **Mean Squared Error (MSE)**  
- Evaluation Metric: **Mean Absolute Error (MAE)**  

---

## 🔁 Workflow

1. Import required libraries  
2. Load dataset  
3. Perform data preprocessing  
4. Split dataset into training and testing sets  
5. Apply feature scaling  
6. Build ANN model  
7. Train the model  
8. Evaluate performance  
9. Make predictions  
10. Visualize training results  

---

## 📈 Model Performance

The model training process includes:

- Training Loss Curve  
- Validation Loss Curve  

These graphs are used to analyze:

- Model convergence  
- Overfitting / Underfitting behavior  
- Training stability  

---


```bash
pip install -r requirements.txt
Step 2: Run the Application
python cgpa_predictor.py
 Sample Prediction

Input:

Attendance: 85
Internal Marks: 80
Backlogs: 1

Output:

Predicted CGPA ≈ 8.0
 Key Features
Simple ANN-based regression model
Real-world academic prediction system
Clean and structured implementation
Training visualization support
Easily extendable architecture
 Future Improvements
Increase dataset size for improved accuracy
Add Dropout layers to reduce overfitting
Deploy as a web application (Streamlit/Flask)
Compare ANN with traditional ML models
Enhance feature engineering techniques
 Technologies Used

TensorFlow • Keras • Python • NumPy • Pandas • Scikit-learn • Matplotlib

 Conclusion

This project demonstrates how Artificial Neural Networks can be effectively used for regression-based prediction tasks. It covers the complete machine learning pipeline from data preprocessing to model evaluation and prediction.
