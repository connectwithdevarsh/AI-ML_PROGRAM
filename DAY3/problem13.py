import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6]
fuel_usage = [15, 16, 17, 18, 19, 20]

plt.plot(days, fuel_usage)
plt.title("Daily Fuel Consumption")
plt.xlabel("Days")
plt.ylabel("Fuel Consumed (Liters)")
plt.show()

print("The fuel consumption has increased continuously from 15 liters to 20 liters.")
