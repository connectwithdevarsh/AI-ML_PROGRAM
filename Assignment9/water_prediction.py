import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_excel("d:/AIML/Assignment9/water_usage.xlsx")

print("--- First Few Rows ---")
print(df.head())

X = df[["Households"]]
y = df["Total_Litres"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("\n--- Model Coefficients ---")
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

pred = model.predict(X_test)

pred_250 = model.predict([[250]])[0]
print("\nPredicted water usage for 250 households:", pred_250)

plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color="red")
plt.title("Households vs Total Water Usage Regression Line")
plt.xlabel("Households")
plt.ylabel("Total Water Usage (Litres)")
plt.show()
