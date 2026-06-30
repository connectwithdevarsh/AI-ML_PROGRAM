import streamlit as st
import pandas as pd
import pickle

st.title("Used Car Valuation Portal")
st.subheader("Fill out the form below to calculate the estimated market value of your vehicle.")

years = st.number_input("Years Old", min_value=0, value=5)
mileage = st.slider("Mileage (in Thousands)", min_value=0, max_value=300, value=50)
fuel_type = st.selectbox("Fuel Type", options=["Petrol", "Diesel"])

if fuel_type == "Petrol":
    fuel_val = 0
else:
    fuel_val = 1

if st.button("Evaluate & Predict Price"):
    with open("car_model.pkl", "rb") as file:
        model = pickle.load(file)
    
    input_data = pd.DataFrame({
        "Years_Old": [years],
        "Mileage_Thousands": [mileage],
        "Fuel_Encoded": [fuel_val]
    })
    
    pred = model.predict(input_data)
    price = pred[0] * 1000
    
    st.success(f"The predicted value of the vehicle is ${price:,.0f}")
