import matplotlib.pyplot as plt

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6"]
water_usage_2 = [130, 135, 140, 150, 155, 160]

plt.plot(days, water_usage_2)
plt.title("Daily Water Usage Trend")
plt.xlabel("Days")
plt.ylabel("Water Usage (Liters)")
plt.show()

print("The daily water usage shows an increasing trend, starting at 130 liters and rising to 160 liters.")
