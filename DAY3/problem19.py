import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6]
delivery_orders = [90, 110, 130, 160, 200, 240]

plt.plot(days, delivery_orders)
plt.title("Delivery Orders Over Days")
plt.xlabel("Days")
plt.ylabel("Number of Orders")
plt.show()

print("The number of delivery orders has increased from 90 orders on Day 1 to 240 orders on Day 6.")
