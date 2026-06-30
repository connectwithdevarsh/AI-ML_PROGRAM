import matplotlib.pyplot as plt

data = {"Shoes": ["Sneakers", "Sandals", "Boots", "Loafers"], "Sold": [30, 25, 15, 20]}

plt.bar(data["Shoes"], data["Sold"])
plt.title("Shoes Quantity Sold")
plt.xlabel("Shoe Types")
plt.ylabel("Pairs Sold")
plt.show()

print("Sneakers are the highest sold shoes with 30 pairs, whereas Boots are the lowest sold with 15 pairs.")
