import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("advertising_sales.xlsx")

X = df[["TV_Budget"]]
y = df["Sales_Units"]

model = LinearRegression()
model.fit(X, y)

print("Slope (Coefficient):", model.coef_[0])
print("Y-Intercept:", model.intercept_)

pred = model.predict(X)

new_data = pd.DataFrame({"TV_Budget": [150]})
pred_150 = model.predict(new_data)
print("Predicted Sales Units for TV Budget 150:", pred_150[0])

plt.scatter(df["TV_Budget"], y)
plt.plot(df["TV_Budget"], pred, color="red")
plt.title("TV Budget vs. Product Sales Regression Line")
plt.xlabel("TV Budget")
plt.ylabel("Sales Units")
plt.show()
