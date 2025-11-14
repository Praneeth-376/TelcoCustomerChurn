📊 Telecom Customer Churn Prediction

Predicting whether a telecom customer will churn (leave the service) using machine learning.

This project builds a complete end-to-end ML pipeline including data cleaning, preprocessing, model training, evaluation, and insights.
The goal is to help telecom companies identify customers who are likely to churn and take preventive actions.

🧠 Project Overview

Customer churn causes major revenue loss in telecom companies.
By predicting churn in advance, the company can:

Offer discounts

Improve services

Target retention campaigns

This project analyzes customer data and predicts Churn = Yes / No using multiple ML algorithms.

📁 Dataset

Source: IBM Telco Customer Churn Dataset
Rows: ~7000
Target variable: Churn (Yes/No)

Key Features

Customer tenure

MonthlyCharges

TotalCharges

Contract type

InternetService

TechSupport

PaymentMethod

Partner / SeniorCitizen / Gender

🛠️ Technologies Used

Python

Pandas

NumPy

Matplotlib & Seaborn

Scikit-learn

Jupyter / Google Colab

🔍 Workflow
1️⃣ Data Cleaning

✔ Removed missing values
✔ Converted TotalCharges to numeric
✔ Dropped unnecessary columns (like customerID)

2️⃣ Exploratory Data Analysis

✔ Churn rate visualization
✔ Contract vs Churn
✔ Monthly charges distribution
✔ Correlation heatmap

3️⃣ Preprocessing

✔ Label encoding for categorical variables
✔ Train-test split
✔ Scaling (optional)

4️⃣ Model Training

Trained and evaluated:

Model	Status
Logistic Regression	✅ Best Model
Decision Tree	✔ Tested
Random Forest	✔ Tested
Naive Bayes	✔ Tested
SVM	✔ Tested
🏆 Best Model: Logistic Regression
📌 Why Logistic Regression performed best:

Works great with categorical yes/no features

Less overfitting than Decision Trees

Smooth probability estimation

Highest ROC-AUC Score among all models

| Model               | Accuracy | ROC AUC  |
| ------------------- | -------- | -------- |
| Logistic Regression | ⭐ Best   | ⭐ Best   |
| Random Forest       | Good     | Good     |
| SVM                 | Good     | Average  |
| Decision Tree       | Moderate | Moderate |
| Naive Bayes         | Lower    | Lower    |


🧩 Confusion Matrix (Best Model)
Shows how well the model classifies churn vs non-churn.
<img width="640" height="588" alt="Screenshot 2025-11-14 143721" src="https://github.com/user-attachments/assets/96c61b22-5a94-4011-8007-e6229e5da929" />
