# Student CGPA Predictor Using Artificial Neural Networks (ANN)
 Project Overview
The Student CGPA Predictor is a Deep Learning mini project developed using an Artificial Neural Network (ANN).  
The model predicts a student’s CGPA based on:

- Attendance Percentage
- Internal Marks
- Number of Backlogs

This project demonstrates the implementation of regression using ANN with TensorFlow and Keras.

---

 Objective
The main objective of this project is to:

- Predict student CGPA accurately
- Understand ANN architecture
- Learn regression using Deep Learning
- Perform data preprocessing and visualization

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| TensorFlow / Keras | Building ANN Model |
| NumPy | Numerical Operations |
| Pandas | Dataset Handling |
| Matplotlib | Data Visualization |
| Scikit-learn | Data Preprocessing |

---

## 📂 Project Files

| File Name | Description |
|---|---|
| cgpa_predictor.py | Main ANN model code |
| student_cgpa_dataset.csv | Dataset used for training |
| README.md | Project documentation |
| requirements.txt | Required Python libraries |

---

## 📊 Dataset Information

### Input Features
1. Attendance
2. Internal Marks
3. Backlogs

### Output
- CGPA

---

## 🧠 ANN Architecture

```text
Input Layer (3 Features)
        ↓
Hidden Layer 1 (16 Neurons, ReLU)
        ↓
Hidden Layer 2 (8 Neurons, ReLU)
        ↓
Output Layer (1 Neuron, Linear)
⚙️ Model Configuration
Optimizer
Adam Optimizer
Loss Function
Mean Squared Error (MSE)
Metric
Mean Absolute Error (MAE)
🚀 Steps Involved
Import Libraries
Create Dataset
Split Training and Testing Data
Apply Feature Scaling
Build ANN Model
Train Model
Evaluate Performance
Predict CGPA
Visualize Loss Graph
📈 Training Visualization

The project plots:

Training Loss
Validation Loss

This helps analyze:

Model learning
Overfitting
Performance improvement
 How to Run the Project
Step 1: Install Requirements
pip install -r requirements.txt
Step 2: Run Python File
python cgpa_predictor.py
 Sample Prediction
Input
Attendance = 85
Internal Marks = 80
Backlogs = 1
Output
Predicted CGPA ≈ 8.0
 Advantages
Simple ANN implementation
Beginner-friendly project
Demonstrates regression using Deep Learning
Easy to modify and improve
 Future Enhancements
Add larger dataset
Improve prediction accuracy
Use Dropout to reduce overfitting
Deploy as a web application
Compare ANN with other ML algorithms
 Developed Using

TensorFlow and Keras Deep Learning Framework

 Conclusion

This project successfully predicts student CGPA using an Artificial Neural Network (ANN).
It demonstrates the complete workflow of a Deep Learning regression project including preprocessing, training, evaluation, prediction, and visualization
