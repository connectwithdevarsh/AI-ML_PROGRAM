import streamlit as st
import pickle

st.title("Employee Salary Prediction Portal")
st.write("Fill out the form below to calculate the estimated market salary.")

exp = st.number_input("Years Experience", min_value=0.0)
hours = st.number_input("Training Hours", min_value=0.0)
edu = st.selectbox("Education", ["Bachelor's Degree", "Master's Degree"])

if edu == "Bachelor's Degree":
    edu_encoded = 0
else:
    edu_encoded = 1

if st.button("Apply & Predict Salary"):
    with open("salary_model.pkl", "rb") as f:
        model = pickle.load(f)
    
    pred = model.predict([[exp, hours, edu_encoded]])
    salary = int(pred[0])
    
    st.success(f"Predicted Salary: ₹{salary:,}")
