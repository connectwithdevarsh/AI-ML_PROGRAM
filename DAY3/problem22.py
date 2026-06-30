import matplotlib.pyplot as plt

weekly_data = {"Expense": ["Groceries", "Transport", "Entertainment", "Dining"], "Amount": [120, 50, 80, 40]}

plt.bar(weekly_data["Expense"], weekly_data["Amount"])
plt.title("Weekly Expenses by Category")
plt.xlabel("Expense Categories")
plt.ylabel("Amount Spent (in USD)")
plt.show()

print("Groceries have the highest expense amount of 120, and Dining has the lowest expense amount of 40.")
