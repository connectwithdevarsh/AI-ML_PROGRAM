import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
ahmedabad = [52, 55, 60, 65, 70, 78]
mumbai = [46, 48, 52, 56, 60, 66]
delhi = [38, 40, 44, 48, 52, 58]

sum_ahmedabad = sum(ahmedabad)
sum_mumbai = sum(mumbai)
sum_delhi = sum(delhi)

if sum_ahmedabad > sum_mumbai and sum_ahmedabad > sum_delhi:
    highest_branch = "Ahmedabad"
elif sum_mumbai > sum_ahmedabad and sum_mumbai > sum_delhi:
    highest_branch = "Mumbai"
else:
    highest_branch = "Delhi"

growth_months = []
for i in range(1, len(months)):
    if ahmedabad[i] > ahmedabad[i-1] and mumbai[i] > mumbai[i-1] and delhi[i] > delhi[i-1]:
        growth_months.append(months[i])

mean_a = sum_ahmedabad / len(ahmedabad)
mean_m = sum_mumbai / len(mumbai)
mean_d = sum_delhi / len(delhi)

var_a = sum((x - mean_a) ** 2 for x in ahmedabad) / len(ahmedabad)
var_m = sum((x - mean_m) ** 2 for x in mumbai) / len(mumbai)
var_d = sum((x - mean_d) ** 2 for x in delhi) / len(delhi)

std_a = var_a ** 0.5
std_m = var_m ** 0.5
std_d = var_d ** 0.5

if std_a > std_m and std_a > std_d:
    volatile_branch = "Ahmedabad"
elif std_m > std_a and std_m > std_d:
    volatile_branch = "Mumbai"
else:
    volatile_branch = "Delhi"

print("Question 1: Which branch consistently generates the highest revenue?")
print("Highest performing branch:", highest_branch)
print()
print("Question 2: During which months do all branches experience revenue growth?")
print("Months with growth in all branches:", ", ".join(growth_months))
print()
print("Question 3: Which branch shows the highest revenue volatility?")
print("Branch with highest volatility:", volatile_branch)

plt.plot(months, ahmedabad, marker='o', label="Ahmedabad")
plt.plot(months, mumbai, marker='s', label="Mumbai")
plt.plot(months, delhi, marker='d', label="Delhi")
plt.title("Monthly Revenue Comparison Across Branches")
plt.xlabel("Month")
plt.ylabel("Revenue (₹ Lakhs)")
plt.legend()
plt.show()
