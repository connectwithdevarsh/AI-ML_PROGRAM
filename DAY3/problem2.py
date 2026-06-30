import matplotlib.pyplot as plt

airports = ["Delhi", "Mumbai", "Bangalore", "Hyderabad", "Chennai"]
flights = [980, 870, 760, 620, 590]

plt.bar(airports, flights)
plt.title("Daily Flights at Different Airports")
plt.xlabel("Airports")
plt.ylabel("Number of Daily Flights")
plt.show()

print("Delhi airport has the most daily flights (980) and Chennai has the lowest daily flights (590).")
