import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the trained model
model = joblib.load("best_model.pkl")

st.title("📊 Telecom Customer Churn Prediction")

st.write("Enter details to predict whether the customer will churn.")

# Input fields
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100)
monthly = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0)
total = st.number_input("Total Charges", min_value=0.0, max_value=10000.0)

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
techsupport = st.selectbox("Tech Support", ["Yes", "No"])

# Convert to features
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
internet_map = {"No": 0, "DSL": 1, "Fiber optic": 2}
tech_map = {"No": 0, "Yes": 1}

input_data = np.array([[
    tenure,
    monthly,
    total,
    contract_map[contract],
    internet_map[internet],
    tech_map[techsupport]
]])

if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]
    
    if prediction == 1:
        st.error(f"⚠️ Customer is likely to churn! (Probability: {probability:.2f})")
    else:
        st.success(f"✅ Customer will stay. (Probability: {probability:.2f})")
