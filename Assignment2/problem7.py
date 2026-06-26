import matplotlib.pyplot as plt

units = ["U1", "U2", "U3", "U4", "U5", "U6", "U7", "U8", "U9", "U10"]
temps = [4.1, 3.8, 4.5, 5.2, 3.6, 4.9, 6.0, 3.9, 5.5, 6.8]

safe_limit = 5.0

print("--- Warehouse Cold Storage Temperature Control ---")
print("1. Storage units showing temperature instability (exceeding safe limit of", safe_limit, "°C):")
for i in range(len(temps)):
    if temps[i] > safe_limit:
        print(units[i], "has unstable temperature of", temps[i], "°C")

print("\n2. Units exceeding safe temperature limits:")
exceeding_units = []
for i in range(len(temps)):
    if temps[i] > safe_limit:
        exceeding_units.append(units[i])
print("Units exceeding safe limits are:", exceeding_units)

print("\n3. Units requiring immediate maintenance:")
max_temp = temps[0]
max_unit = units[0]
for i in range(len(temps)):
    if temps[i] > max_temp:
        max_temp = temps[i]
        max_unit = units[i]
print("Unit", max_unit, "requires immediate maintenance as it has the highest temperature of", max_temp, "°C.")

plt.bar(units, temps, color="skyblue")
plt.axhline(y=safe_limit, color="red", linestyle="--", linewidth=1.5, label="Safe Limit (5.0°C)")
plt.title("Cold Storage Temperature by Unit")
plt.xlabel("Storage Unit")
plt.ylabel("Temperature (°C)")
plt.legend()
plt.show()
