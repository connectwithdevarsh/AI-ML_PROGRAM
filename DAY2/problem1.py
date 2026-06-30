import matplotlib.pyplot as plt

spend = [5, 8, 10, 12, 15, 18]
conversions = [120, 180, 210, 260, 310, 360]

n = len(spend)
mean_x = sum(spend) / n
mean_y = sum(conversions) / n

num = 0
den_x = 0
den_y = 0
for i in range(n):
    num += (spend[i] - mean_x) * (conversions[i] - mean_y)
    den_x += (spend[i] - mean_x) ** 2
    den_y += (conversions[i] - mean_y) ** 2

r = num / ((den_x * den_y) ** 0.5)

if r > 0:
    corr_ans = "Yes, there is a positive correlation."
else:
    corr_ans = "No, there is no positive correlation."

slow_level = None
prev_growth = None
for i in range(1, n):
    growth = (conversions[i] - conversions[i-1]) / (spend[i] - spend[i-1])
    if prev_growth is not None and growth < prev_growth:
        slow_level = spend[i-1]
        break
    prev_growth = growth

best_eff = 0
best_spend = spend[0]
for i in range(n):
    eff = conversions[i] / spend[i]
    if eff > best_eff:
        best_eff = eff
        best_spend = spend[i]

print("Question 1: Is there a positive correlation between ad spend and conversions?")
print(corr_ans)
print("Correlation coefficient:", round(r, 4))
print()
print("Question 2: At what spending level does conversion growth start slowing down?")
print("Growth starts slowing down at:", slow_level, "Lakhs")
print()
print("Question 3: Which ad spend value delivers the highest conversion efficiency?")
print("Ad spend with highest efficiency:", best_spend, "Lakhs (Efficiency:", round(best_eff, 2), "conversions per Lakh)")

plt.plot(spend, conversions, marker='o')
plt.title("Ad Spend vs Conversions")
plt.xlabel("Ad Spend (₹ Lakhs)")
plt.ylabel("Conversions")
plt.show()
