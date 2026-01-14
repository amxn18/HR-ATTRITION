import os
import streamlit as st
import requests

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(
    page_title="Employee Attrition Predictor",
    layout="centered",
    initial_sidebar_state="auto",
)

st.title("Employee Attrition Prediction")
st.markdown("Please fill in these employee details to predict the liklehood of attrition")

with st.form("attrition_form"):
    age = st.number_input("Age", min_value=18, max_value=65, value=30)
    
    gender = st.selectbox("Gender", ["Male", "Female"])
    
    marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    
    department = st.selectbox("Department", ["Sales", "Research & Development", "Human Resources"])

    job_role = st.selectbox("Job Role", ["Sales Executive","Research Scientist","Laboratory Technician","Manufacturing Director","Healthcare Representative", "Manager","Human Resources"])

    job_level = st.slider("Job Level", 1, 5, 2)

    monthly_income = st.number_input("Monthly Income",min_value=1000,max_value=200000,value=5000)

    overtime = st.selectbox("OverTime",["Yes", "No"])

    work_life_balance = st.slider("Work Life Balance",1, 4, 3)

    years_at_company = st.slider("Years at Company",0, 40, 5)

    submit = st.form_submit_button("Predict Attrition")

if submit :
    input_data = {
    "Age": age,
    "Gender": gender,
    "MaritalStatus": marital_status,
    "Department": department,
    "JobRole": job_role,
    "JobLevel": job_level,
    "MonthlyIncome": monthly_income,
    "OverTime": overtime,
    "WorkLifeBalance": work_life_balance,
    "YearsAtCompany": years_at_company,

    "BusinessTravel": "Travel_Rarely",
    "DistanceFromHome": 5,
    "DailyRate": 1000,
    "Education": 3,
    "EducationField": "Life Sciences",
    "EnvironmentSatisfaction": 3,
    "HourlyRate": 60,
    "JobInvolvement": 3,
    "JobSatisfaction": 3,
    "MonthlyRate": 20000,
    "NumCompaniesWorked": 1,
    "PercentSalaryHike": 12,
    "PerformanceRating": 3,
    "RelationshipSatisfaction": 3,
    "StockOptionLevel": 1,
    "TotalWorkingYears": 8,
    "TrainingTimesLastYear": 3,
    "YearsInCurrentRole": 3,
    "YearsSinceLastPromotion": 1,
    "YearsWithCurrManager": 3
}


    with st.spinner("Predicting..."):
        try:
            response = requests.post(
                f"{API_URL}/predict",
                json = input_data,
                timeout= 10
            )
            response.raise_for_status()
            result = response.json()

            prediction = result["attrition_prediction"]
            probability = result["attrition_probability"]

            st.subheader("Prediction Result")

            if prediction == 1:
                st.error(
                    f"Likely to Leave"
                    f"(Probability: {probability * 100:.2f}%)"
                )
            else:
                st.success(
                    f"Likely to Stay"
                    f"(Probability: {(1 - probability) * 100:.2f}%)"
                )
        
        except Exception as e:
            st.error(f"Error calling API: {e}")