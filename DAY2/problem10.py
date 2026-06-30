import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5, 6, 7]
sales = [4.2, 5.1, 6.0, 6.8, 7.5, 8.1, 9.0]

n = len(experience)
mean_x = sum(experience) / n
mean_y = sum(sales) / n

num = 0
den_x = 0
den_y = 0
for i in range(n):
    num += (experience[i] - mean_x) * (sales[i] - mean_y)
    den_x += (experience[i] - mean_x) ** 2
    den_y += (sales[i] - mean_y) ** 2

r = num / ((den_x * den_y) ** 0.5)

if r > 0.8:
    impact = "Yes, experience has a strong positive impact on sales."
else:
    impact = "No strong impact found."

diminishing = "No clear diminishing returns as sales grow steadily, though the growth rate fluctuates slightly between 0.6 and 0.9 Lakhs per year."

above_avg_exp = []
for i in range(n):
    if sales[i] > mean_y:
        above_avg_exp.append(str(experience[i]))

print("Question 1: Does experience significantly impact sales performance?")
print(impact, "(Correlation:", round(r, 4), ")")
print()
print("Question 2: Are there diminishing returns after a certain experience level?")
print(diminishing)
print()
print("Question 3: Which experience group generates above-average sales?")
print("Experience years generating above-average sales (> " + str(round(mean_y, 2)) + " Lakhs):", ", ".join(above_avg_exp))

plt.plot(experience, sales, marker='o')
plt.title("Salesperson Experience vs Monthly Sales")
plt.xlabel("Experience (Years)")
plt.ylabel("Monthly Sales (₹ Lakhs)")
plt.show()
