import matplotlib.pyplot as plt

cafe = {"Beverage": ["Latte", "Espresso", "Cappuccino", "Mocha"], "Cups": [30, 25, 20, 15]}

plt.bar(cafe["Beverage"], cafe["Cups"])
plt.title("Beverage Sales at Cafe")
plt.xlabel("Beverages")
plt.ylabel("Cups Sold")
plt.show()

print("Latte is the most sold beverage with 30 cups, and Mocha is the least sold with 15 cups.")
