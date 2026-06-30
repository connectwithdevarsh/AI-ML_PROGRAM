import matplotlib.pyplot as plt

departments = ["HR", "IT", "Sales", "Marketing", "Operations"]
expenses = [200, 450, 380, 320, 410]

plt.bar(departments, expenses)
plt.title("Departmental Expenses")
plt.xlabel("Departments")
plt.ylabel("Expenses (in USD)")
plt.show()

print("IT department has the maximum expenses (450) and HR department has the minimum expenses (200).")
