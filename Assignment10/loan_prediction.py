import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_excel("d:/AIML/Assignment10/loan_data.xlsx")

df = df.drop(columns=["ApplicantID"])

le_edu = LabelEncoder()
df["Education"] = le_edu.fit_transform(df["Education"])

le_status = LabelEncoder()
df["Loan_Status"] = le_status.fit_transform(df["Loan_Status"])

X = df[["ApplicantIncome", "LoanAmount", "Education"]]
y = df["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
acc = accuracy_score(y_test, pred)

print("--- Loan Eligibility Prediction ---")
print("Accuracy Score:", acc)

print("\n--- Enter Details for Prediction ---")
income = float(input("Enter Applicant Income: "))
amount = float(input("Enter Loan Amount: "))
edu_input = input("Enter Education (Graduate/Not Graduate): ")

edu_encoded = le_edu.transform([edu_input])[0]

user_df = pd.DataFrame([[income, amount, edu_encoded]], columns=["ApplicantIncome", "LoanAmount", "Education"])
user_pred = model.predict(user_df)

result = le_status.inverse_transform(user_pred)[0]
print("Loan Status:", result)
