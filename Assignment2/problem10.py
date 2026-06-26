import matplotlib.pyplot as plt

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7", "Day 8", "Day 9", "Day 10"]
output = [48, 50, 52, 47, 55, 60, 58, 62, 45, 65]

print("--- Water Treatment Plant Output Stability Review ---")
total_output = 0
for val in output:
    total_output += val
avg_output = total_output / len(days)
print("Average daily water output is", avg_output, "units")

print("\n1. Days with unusually low or high output:")
# Identify high output (>= 60)
for i in range(len(output)):
    if output[i] >= 60:
        print(days[i], "has high output of", output[i], "units")
# Identify low output (<= 47)
for i in range(len(output)):
    if output[i] <= 47:
        print(days[i], "has low output of", output[i], "units")

print("\n2. Stability of water production:")
min_out = output[0]
max_out = output[0]
for val in output:
    if val < min_out:
        min_out = val
    if val > max_out:
        max_out = val
print("Water production is moderately stable but varies between a minimum of", min_out, "units (Day 9) and a maximum of", max_out, "units (Day 10).")

print("\n3. Actionable recommendation to improve consistency:")
print("Implement water reservoirs/tanks to buffer daily output fluctuations, and avoid scheduling maintenance during high demand periods.")

plt.plot(days, output, marker="^", color="darkcyan", linewidth=2)
plt.title("Daily Water Treatment Plant Output")
plt.xlabel("Day")
plt.ylabel("Output (units)")
plt.grid(True)
plt.show()
