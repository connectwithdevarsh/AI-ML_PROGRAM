import matplotlib.pyplot as plt

hours = ["6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM"]
drivers = [120, 180, 260, 310, 280, 240, 220, 200, 190, 170]

print("--- Ride-Hailing Driver Availability Study ---")
print("1. Hours with lowest driver availability:")
min_drivers = drivers[0]
min_hour = hours[0]
for i in range(len(drivers)):
    if drivers[i] < min_drivers:
        min_drivers = drivers[i]
        min_hour = hours[i]
print("Absolute lowest availability is at", min_hour, "with", min_drivers, "active drivers.")

print("\n2. Supply alignment with demand patterns:")
print("Supply increases for the morning rush hours (7 AM - 9 AM) peaking at 9 AM.")
print("However, supply declines continuously from 10 AM onwards.")

print("\n3. When driver incentives should be introduced:")
print("Incentives should be introduced during low availability periods:")
for i in range(len(drivers)):
    if drivers[i] < 200:
        print("At", hours[i], "with only", drivers[i], "drivers")

plt.plot(hours, drivers, marker="s", color="orange", linewidth=2)
plt.title("Active Driver Availability over Time")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Active Drivers")
plt.grid(True)
plt.show()
