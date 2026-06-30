import matplotlib.pyplot as plt

batches = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
units = [1000, 1200, 1500, 1800, 2200, 2600, 3000, 2800, 2400, 2000]
defects = [1.2, 1.4, 1.8, 2.1, 2.5, 2.9, 3.4, 3.0, 2.6, 2.2]

n = len(units)
mean_u = sum(units) / n
mean_d = sum(defects) / n

num = 0
den_u = 0
den_d = 0
for i in range(n):
    num += (units[i] - mean_u) * (defects[i] - mean_d)
    den_u += (units[i] - mean_u) ** 2
    den_d += (defects[i] - mean_d) ** 2

r = num / ((den_u * den_d) ** 0.5)

if r > 0.7:
    relation = "Yes, defect rate increases significantly with production volume."
else:
    relation = "No clear strong positive relationship."

max_defect = defects[0]
max_batch = batches[0]
for i in range(1, n):
    if defects[i] > max_defect:
        max_defect = defects[i]
        max_batch = batches[i]

safe_units = []
for i in range(n):
    if defects[i] <= 2.0:
        safe_units.append(units[i])

min_safe = min(safe_units)
max_safe = max(safe_units)

print("Question 1: Does defect rate increase with production volume?")
print(relation, "(Correlation:", round(r, 4), ")")
print()
print("Question 2: Which batch has the highest defect percentage?")
print("Batch with highest defect rate:", max_batch, f"({max_defect}%)")
print()
print("Question 3: What production range appears safest for quality control?")
print(f"Production range of {min_safe} to {max_safe} units (where defect rate is <= 2.0%)")

plt.scatter(units, defects)
plt.title("Production Volume vs Defect Rate")
plt.xlabel("Units Produced")
plt.ylabel("Defect Rate (%)")
plt.show()
