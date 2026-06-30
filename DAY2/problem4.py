import matplotlib.pyplot as plt

departments = ["HR", "IT", "Marketing", "Operations", "Sales", "R&D", "Finance", "Support", "Legal", "Admin"]
expenses = [45, 80, 95, 120, 70, 60, 40, 35, 25, 30]

max_expense = expenses[0]
max_dept = departments[0]
for i in range(1, len(expenses)):
    if expenses[i] > max_expense:
        max_expense = expenses[i]
        max_dept = departments[i]

total_expense = sum(expenses)
ops_mkt_expense = 0
for i in range(len(departments)):
    if departments[i] == "Operations" or departments[i] == "Marketing":
        ops_mkt_expense += expenses[i]

percentage = (ops_mkt_expense / total_expense) * 100

opt_dept = max_dept

print("Question 1: Which department has the highest operational cost?")
print("Department with highest cost:", max_dept, f"({max_expense} ₹ Crores)")
print()
print("Question 2: What percentage of total expenses is consumed by Operations and Marketing combined?")
print("Percentage:", round(percentage, 2), "%")
print()
print("Question 3: Which department could be optimized to reduce overall expenses?")
print("Department recommended for optimization:", opt_dept, "(since it has the highest expense)")

plt.pie(expenses, labels=departments, autopct='%1.1f%%')
plt.title("Company Expense Distribution")
plt.show()
