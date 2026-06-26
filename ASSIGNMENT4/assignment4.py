import pandas as pd

df = pd.read_excel("student_analytics_dataset.xlsx")

print("Q1")
print(df.head(10))
print()

print("Q2")
print(df.tail(3))
print()

print("Q3")
print(df.dtypes)
print()

print("Q4")
print(df.size)
print()

print("Q5")
print(df["City"])
print()

print("Q6")
print(df["Python_Marks"])
print()

print("Q7")
print(df[["Student_Name", "Age", "Department"]])
print()

print("Q8")
print(df.iloc[0])
print()

print("Q9")
print(df[df["Age"] == 18])
print()

print("Q10")
print(df[df["City"] == "Rajkot"])
print()

print("Q11")
print(df[df["Department"] == "MECH"])
print()

print("Q12")
print(df[df["Attendance"] < 75])
print()

print("Q13")
print(df[df["SQL_Marks"] < 40])
print()

print("Q14")
print(df[df["PowerBI_Marks"] > 80])
print()

print("Q15")
print(df[df["Placement_Status"] == "Not Placed"])
print()

print("Q16")
print(df[df["Python_Marks"] == 98])
print()

print("Q17")
print(df["SQL_Marks"].mean())
print()

print("Q18")
print(df["PowerBI_Marks"].max())
print()

print("Q19")
print(df["Python_Marks"].min())
print()

print("Q20")
print(df["Python_Marks"].sum())
print()

print("Q21")
print(df["Attendance"].mean())
print()

print("Q22")
print(df["Age"].max())
print()

print("Q23")
print(df["Age"].min())
print()

print("Q24")
print(df["Department"].count())
print()

print("Q25")
print(df.sort_values(by="Student_Name"))
print()

print("Q26")
print(df.sort_values(by="Student_Name", ascending=False))
print()

print("Q27")
print(df.sort_values(by="SQL_Marks"))
print()

print("Q28")
print(df.sort_values(by="PowerBI_Marks", ascending=False))
print()

print("Q29")
print(df.sort_values(by="Student_ID", ascending=False))
print()

print("Q30")
print(df.sort_values(by="Age"))
print()

print("Assignment Completed")
