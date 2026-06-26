import matplotlib.pyplot as plt

shifts = ["6 AM", "10 AM", "2 PM", "6 PM", "10 PM"]
power = [200, 350, 350, 500, 300]

print("--- Factory Shift Power Usage ---")

max_power = power[0]
max_shift = shifts[0]
for i in range(len(power)):
    if power[i] > max_power:
        max_power = power[i]
        max_shift = shifts[i]

print("1. Shift with highest power usage:")
print("The shift at", max_shift, "consumes the most power (", max_power, "kWh).")

print("\n2. Sudden increases in power usage:")
for i in range(len(power) - 1):
    diff = power[i+1] - power[i]
    if diff > 100:
        print("Sudden increase of", diff, "kWh observed from", shifts[i], "to", shifts[i+1])

print("\n3. Power usage optimization strategy:")
print("To optimize power usage, shift machinery load from the peak hours of 6 PM and 10 AM to the 6 AM or 10 PM shifts.")

plt.plot(shifts, power, marker="o", color="red")
plt.title("Power Usage across Factory Shifts")
plt.xlabel("Shift Time")
plt.ylabel("Power Usage (kWh)")
plt.grid(True)
plt.show()
