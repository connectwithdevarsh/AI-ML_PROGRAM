import matplotlib.pyplot as plt

claims = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10"]
days = [7, 12, 9, 18, 25, 14, 30, 10, 22, 35]

print("--- Insurance Claim Processing Time Assessment ---")
print("1. Claims taking significantly longer to process (>= 25 days):")
for i in range(len(days)):
    if days[i] >= 25:
        print("Claim", claims[i], "takes", days[i], "days")

print("\n2. Consistency of processing times:")
min_days = days[0]
max_days = days[0]
for d in days:
    if d < min_days:
        min_days = d
    if d > max_days:
        max_days = d
diff = max_days - min_days
print("Range is from", min_days, "days to", max_days, "days (Difference:", diff, "days).")
print("This indicates that the processing time is highly inconsistent.")

print("\n3. Workflow efficiency improvement area:")
total_days = 0
for d in days:
    total_days += d
avg_days = total_days / len(claims)
print("Average processing time is", avg_days, "days.")
print("Focus on optimizing steps for claims taking longer than average (C5, C7, C9, C10).")

plt.bar(claims, days, color="salmon")
plt.title("Insurance Claim Processing Time")
plt.xlabel("Claim ID")
plt.ylabel("Processing Time (Days)")
plt.show()
