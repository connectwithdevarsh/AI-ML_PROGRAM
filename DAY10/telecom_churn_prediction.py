import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_excel("telecom_churn (1).xlsx")

df = df.drop(columns=["CustomerID"])

le = LabelEncoder()
df["TechSupport"] = le.fit_transform(df["TechSupport"])
df["Churn_Status"] = le.fit_transform(df["Churn_Status"])

X = df[["Tenure_Months", "Monthly_Charges", "TechSupport"]]
y = df["Churn_Status"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

pred = model.predict(x_test)

acc = accuracy_score(y_test, pred)
print("Accuracy Score:", acc)
