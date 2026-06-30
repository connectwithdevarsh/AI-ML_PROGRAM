import matplotlib.pyplot as plt

sales = {"Cheese": ["Cheddar", "Mozzarella", "Parmesan", "Gouda"], "Packs": [10, 12, 8, 6]}

plt.bar(sales["Cheese"], sales["Packs"])
plt.title("Cheese Packs Sold")
plt.xlabel("Cheese Type")
plt.ylabel("Number of Packs Sold")
plt.show()

print("Mozzarella has the highest sales of 12 packs, and Gouda has the lowest sales of 6 packs.")
