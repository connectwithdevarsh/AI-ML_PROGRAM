import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5, 6, 7, 8]
temp_change = [26, 27, 28, 29, 31, 33, 34, 35]

plt.plot(days, temp_change)
plt.title("Daily Temperature Change")
plt.xlabel("Days")
plt.ylabel("Temperature (Degree Celsius)")
plt.show()

print("The temperature shows an upward trend, rising from 26 degrees to 35 degrees.")
