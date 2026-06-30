import matplotlib.pyplot as plt

food = ["Burger", "Pizza", "Pasta", "Sandwich", "Salad"]
calories = [350, 420, 380, 300, 150]

plt.bar(food, calories)
plt.title("Calories in Food Items")
plt.xlabel("Food Item")
plt.ylabel("Calories")
plt.show()

print("Pizza has the highest calories (420) and Salad has the lowest calories (150).")
