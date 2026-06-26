import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("d:/AIML/Assignment9/parking_revenue.xlsx")

print("--- First Few Rows ---")
print(df.head())

X = df[["Vehicles_Parked"]]
y = df["Revenue_INR"]

model = LinearRegression()
model.fit(X, y)

print("\n--- Model Coefficients ---")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

pred = model.predict(X)

pred_850 = model.predict([[850]])[0]
print("\nPredicted revenue for 850 vehicles:", pred_850)

plt.scatter(X, y, color="blue")
plt.plot(X, pred, color="red")
plt.title("Parking Revenue Prediction")
plt.xlabel("Vehicles Parked")
plt.ylabel("Revenue (INR)")
plt.show()
