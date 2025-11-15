
import streamlit as st
import joblib
import numpy as np
import json

#Load the trained model
model = joblib.load('linear_regression_model.pkl')

#Streamlit App
st.title("Insurance Charges Prediction")
st.write("Enter the input values for prediction.")

# Input fields for user to enter values for each feature
age = st.number_input("Age", min_value=18, max_value=65, step=1, value=30)
bmi = st.number_input("BMI", min_value=15.0, max_value=50.0, step=0.1, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1, value=0)
diabetes = st.selectbox("Has Diabetes?", options=["No", "Yes"])
heart_rate = st.number_input("Heart Rate", min_value=50, max_value=120, step=1, value=75)
creatinine = st.number_input("Creatinine", min_value=0.0, max_value=2.0, step=0.1, value=1.0)
glucose = st.number_input("Glucose", min_value=50.0, max_value=300.0, step=1.0, value=100.0)

# Categorical features
sex_female = st.selectbox("Sex", options=["Male", "Female"]) =="Female"
smoker_no = st.selectbox("Smoker?", options=["No", "Yes"])=="No"

#Region Selection
region = st.selectbox("Region", options=["Northeast", "Northwest", "Southeast", "Southwest"])
region_northeast = region == "Northeast"
region_northwest = region == "Northwest"
region_southeast = region == "Southeast"
region_southwest = region == "Southwest"

# Normalization function
def min_max_scale(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val)

#Load Min-Max values from JSON
with open("min_max_values.json", "r") as json_file:
    min_max_values = json.load(json_file)

#Normalize inputs
age_norm = min_max_scale(age, *min_max_values["age"])
bmi_norm = min_max_scale(bmi, *min_max_values["bmi"])
heart_rate_norm = min_max_scale(heart_rate, *min_max_values["heart rate"])
creatinine_norm = min_max_scale(creatinine, *min_max_values["Creatinine"])
glucose_norm = min_max_scale(glucose, *min_max_values["glucose"])

# Convert categorical values to numeric
diabetes_val = 1 if diabetes == "Yes" else 0
sex_female_val = 1 if sex_female else 0
smoker_no_val = 1 if smoker_no else 0
region_vals = [
    int(region_northeast),
    int(region_northwest),
    int(region_southeast),
    int(region_southwest)
]

# Prepare input for prediction (ensure all numeric)
input_data = np.array([[age_norm, bmi_norm, children, diabetes_val,
                        heart_rate_norm, creatinine_norm, glucose_norm,
                        sex_female_val, smoker_no_val, *region_vals]])

# Predict button
if st.button("Predict Charges"):
    prediction = model.predict(input_data)
    st.success(f"Predicted Insurance Charges: ${prediction[0]:,.2f}")
