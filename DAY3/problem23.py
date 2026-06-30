import matplotlib.pyplot as plt

candy_Sales = {"Candy": ["Chocolate", "Lollipop", "Gum", "Jelly Beans"], "Sales": [25, 15, 10, 20]}

plt.bar(candy_Sales["Candy"], candy_Sales["Sales"])
plt.title("Candy Sales Data")
plt.xlabel("Candy Types")
plt.ylabel("Sales Count")
plt.show()

print("Chocolate has the highest sales of 25, while Gum has the lowest sales of 10.")
