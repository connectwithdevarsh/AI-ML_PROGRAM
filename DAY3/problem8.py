import matplotlib.pyplot as plt

departments = ["HR", "IT", "Finance", "Sales", "Support"]
employees = [45, 120, 60, 90, 70]

plt.bar(departments, employees)
plt.title("Employee Count by Department")
plt.xlabel("Departments")
plt.ylabel("Number of Employees")
plt.show()

print("The IT department has the highest number of employees (120) and the HR department has the lowest (45).")
