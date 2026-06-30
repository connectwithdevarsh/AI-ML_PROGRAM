import matplotlib.pyplot as plt

veggies = {"Vegetable": ["Carrot", "Tomato", "Potato", "Cabbage"], "Quantity": [12, 15, 20, 8]}

plt.bar(veggies["Vegetable"], veggies["Quantity"])
plt.title("Vegetable Quantity Inventory")
plt.xlabel("Vegetable Name")
plt.ylabel("Quantity Available")
plt.show()

print("Potato has the maximum quantity of 20, and Cabbage has the minimum quantity of 8.")
