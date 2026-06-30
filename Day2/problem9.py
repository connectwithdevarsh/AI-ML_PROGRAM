import matplotlib.pyplot as plt

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]
bounce_rates = [52, 50, 48, 49, 47, 46, 45]

if bounce_rates[-1] < bounce_rates[0]:
    trend = "Downward (which means bounce rate is improving/decreasing)"
else:
    trend = "Upward"

min_bounce = min(bounce_rates)
best_day = None
for i in range(len(bounce_rates)):
    if bounce_rates[i] == min_bounce:
        best_day = days[i]
        break

improvement = bounce_rates[0] - bounce_rates[-1]

print("Question 1: Is the bounce rate trending upward or downward?")
print("Trend:", trend)
print()
print("Question 2: On which day is user engagement the highest?")
print("Highest engagement day (lowest bounce rate):", best_day, f"({min_bounce}%)")
print()
print("Question 3: How much improvement is observed from Day 1 to Day 10?")
print(f"Improvement from Day 1 to Day 7 (last available day): {improvement}%")

plt.plot(days, bounce_rates, marker='o')
plt.title("Daily Website Bounce Rate Trend")
plt.xlabel("Day")
plt.ylabel("Bounce Rate (%)")
plt.show()
