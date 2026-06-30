import matplotlib.pyplot as plt

months = ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"]
monthly_profit = [4000, 4200, 4500, 4800, 5200, 5600]

plt.plot(months, monthly_profit)
plt.title("Monthly Profit Trend")
plt.xlabel("Months")
plt.ylabel("Profit (in USD)")
plt.show()

print("The monthly profit is steadily increasing, starting from 4000 and reaching 5600 by Month 6.")
