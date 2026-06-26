import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_excel("d:/AIML/Assignment10/vehicle loan.xlsx")

df = df.drop(columns=["ApplicationID"])

le_emp = LabelEncoder()
df["EmploymentType"] = le_emp.fit_transform(df["EmploymentType"])

le_status = LabelEncoder()
df["LoanStatus"] = le_status.fit_transform(df["LoanStatus"])

X = df[["ApplicantIncome", "VehiclePrice", "EmploymentType"]]
y = df["LoanStatus"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print("--- Vehicle Loan Eligibility Prediction ---")
print("Accuracy Score:", acc)

print("\n--- Enter Details for Prediction ---")
income = float(input("Enter Applicant Income: "))
price = float(input("Enter Vehicle Price: "))
emp_input = input("Enter Employment Type (Salaried/Self-Employed): ")

emp_encoded = le_emp.transform([emp_input])[0]

user_df = pd.DataFrame([[income, price, emp_encoded]], columns=["ApplicantIncome", "VehiclePrice", "EmploymentType"])
user_pred = model.predict(user_df)

result = le_status.inverse_transform(user_pred)[0]
print("Vehicle Loan Status:", result)
