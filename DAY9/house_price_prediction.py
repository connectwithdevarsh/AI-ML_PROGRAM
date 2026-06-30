import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_excel("house_prices.xlsx")

x = data[["Square_Feet"]]
y = data["Price_USD"]

model = LinearRegression()
model.fit(x, y)

print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_)

predictions = model.predict(x)

test_house = pd.DataFrame({"Square_Feet": [2200]})
pred_price = model.predict(test_house)
print("Predicted Price for 2200 Sq Ft:", pred_price[0])

plt.scatter(data["Square_Feet"], y)
plt.plot(data["Square_Feet"], predictions, color="red")
plt.title("Property Size vs. House Price Regression Line")
plt.xlabel("Square Feet")
plt.ylabel("Price USD")
plt.show()
