import matplotlib.pyplot as plt

fast_food = {"Food": ["Burger", "Pizza", "Fries", "Hotdog", "Taco"], "Orders": [60, 70, 50, 40, 30]}

plt.bar(fast_food["Food"], fast_food["Orders"])
plt.title("Fast Food Orders Count")
plt.xlabel("Food Items")
plt.ylabel("Number of Orders")
plt.show()

print("Pizza has the highest number of orders (70) and Taco has the lowest number of orders (30).")
