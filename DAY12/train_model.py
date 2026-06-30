import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

df = pd.read_csv("car_prices (1).csv")

X = df[["Years_Old", "Mileage_Thousands", "Fuel_Encoded"]]
y = df["Price_USD"]

model = LinearRegression()
model.fit(X, y)

with open("car_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully.")
