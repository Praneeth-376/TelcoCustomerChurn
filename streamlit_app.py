import streamlit as st
import pandas as pd
import joblib
import cloudpickle

with open("full_churn_model.pkl", "wb") as f:
    cloudpickle.dump(pipeline, f)

st.title("📊 Telecom Customer Churn Prediction (All Features)")

# Load pipeline
model = joblib.load("full_churn_model.pkl")

st.write("Enter customer details to predict churn:")

# INPUT FORM
tenure = st.number_input("Tenure", min_value=0, max_value=100)
monthly = st.number_input("MonthlyCharges", min_value=0.0, max_value=200.0)
total_charges = st.number_input("TotalCharges", min_value=0.0)

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("SeniorCitizen", ["0", "1"])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
phone_service = st.selectbox("PhoneService", ["Yes", "No"])
multiple_lines = st.selectbox("MultipleLines", ["Yes", "No", "No phone service"])
internet_service = st.selectbox("InternetService", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("OnlineSecurity", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("OnlineBackup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("DeviceProtection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("TechSupport", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("StreamingTV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("StreamingMovies", ["Yes", "No", "No internet service"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("PaperlessBilling", ["Yes", "No"])
payment = st.selectbox("PaymentMethod", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

# Create input DataFrame
raw_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone_service],
    "MultipleLines": [multiple_lines],
    "InternetService": [internet_service],
    "OnlineSecurity": [online_security],
    "OnlineBackup": [online_backup],
    "DeviceProtection": [device_protection],
    "TechSupport": [tech_support],
    "StreamingTV": [streaming_tv],
    "StreamingMovies": [streaming_movies],
    "Contract": [contract],
    "PaperlessBilling": [paperless],
    "PaymentMethod": [payment],
    "MonthlyCharges": [monthly],
    "TotalCharges": [total_charges]
})

if st.button("Predict Churn"):
    prediction = model.predict(raw_data)[0]
    prob = model.predict_proba(raw_data)[0][1]

    if prediction == "Yes":
        st.error(f"⚠️ Customer likely to churn (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer will stay (Probability: {prob:.2f})")
