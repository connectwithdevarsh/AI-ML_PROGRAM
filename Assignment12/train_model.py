import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('employee_salary.csv')

X = df[['Years_Experience', 'Training_Hours', 'Education_Encoded']]
y = df['Salary']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

print("Model Score:", model.score(X_test, y_test))
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

with open('salary_model.pkl', 'wb') as file:
    pickle.dump(model, file)
