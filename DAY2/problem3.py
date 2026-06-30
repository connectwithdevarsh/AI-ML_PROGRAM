import matplotlib.pyplot as plt

employees = ["E1", "E2", "E3", "E4", "E5"]
skills = [2, 3, 4, 5, 6]
productivity = [55, 62, 68, 74, 80]

increasing = True
for i in range(1, len(skills)):
    if productivity[i] <= productivity[i-1]:
        increasing = False
        break

if increasing:
    trend = "Productivity increases consistently as skill level increases."
else:
    trend = "Productivity does not increase consistently as skill level increases."

avg_skill = sum(skills) / len(skills)
avg_prod = sum(productivity) / len(productivity)

high_skill_low_prod = []
for i in range(len(employees)):
    if skills[i] > avg_skill and productivity[i] < avg_prod:
        high_skill_low_prod.append(employees[i])

above_6_prod = []
for i in range(len(skills)):
    if skills[i] > 6:
        above_6_prod.append(productivity[i])

if len(above_6_prod) > 0:
    avg_above_6 = sum(above_6_prod) / len(above_6_prod)
else:
    avg_above_6 = "No employees with skill level above 6"

print("Question 1: How does productivity change as skill level increases?")
print(trend)
print()
print("Question 2: Are there employees with high skill but low productivity?")
if len(high_skill_low_prod) > 0:
    print("Yes:", ", ".join(high_skill_low_prod))
else:
    print("No employees found with high skill and low productivity.")
print()
print("Question 3: What is the average productivity score for skill levels above 6?")
print("Average productivity:", avg_above_6)

plt.plot(skills, productivity, marker='o')
plt.title("Employee Skill Level vs Productivity")
plt.xlabel("Skill Level")
plt.ylabel("Productivity Score")
plt.show()
