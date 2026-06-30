import matplotlib.pyplot as plt

categories = ["Electronics", "Fashion", "Grocery", "Home", "Beauty"]
revenue = [5200, 4300, 3900, 2800, 2400]

plt.bar(categories, revenue)
plt.title("Revenue by Shopping Category")
plt.xlabel("Shopping Categories")
plt.ylabel("Revenue (in USD)")
plt.show()

print("Electronics generated the highest revenue of 5200, and Beauty generated the lowest revenue of 2400.")
