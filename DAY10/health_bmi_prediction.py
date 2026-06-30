import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

data = pd.read_excel("HEALTH BMI (1).xlsx")

data = data.drop("PatientID", axis=1)

encoder = LabelEncoder()
data["BloodPressure"] = encoder.fit_transform(data["BloodPressure"])
data["Outcome"] = encoder.fit_transform(data["Outcome"])

X = data[["Age", "BMI", "BloodPressure"]]
y = data["Outcome"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(x_train, y_train)

predictions = clf.predict(x_test)

accuracy = accuracy_score(y_test, predictions)
print("Model Accuracy:", accuracy)
