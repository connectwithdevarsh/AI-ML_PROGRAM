import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

data = pd.read_csv("Order_dataset - Sheet1.csv")

cat_cols = ['month', 'day_of_week', 'food_category', 'order_platform', 'payment_method', 'time_slot', 'weather_condition', 'kitchen_load']

encoders = {}
for col in cat_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

target_encoder = LabelEncoder()
data['order_status'] = target_encoder.fit_transform(data['order_status'])

X = data.drop('order_status', axis=1)
y = data['order_status']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

def predict_status(input_data):
    df_temp = pd.DataFrame([input_data])
    df_temp = df_temp[X.columns]
    for col in cat_cols:
        le = encoders[col]
        df_temp[col] = le.transform(df_temp[col])
    pred = model.predict(df_temp)
    res = target_encoder.inverse_transform(pred)
    return res[0]
