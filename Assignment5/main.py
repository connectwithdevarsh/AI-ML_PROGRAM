import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("d:/AIML/Assignment5/Uber data set ncr.xlsx")

print("========== SECTION 1 ==========")
print("\n--- First 10 Rows ---")
print(df.head(10))

print("\n--- Total Rows and Columns ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)

print("\n--- Describe statistics ---")
print(df.describe())

print("\n--- Unique Booking Status values ---")
print("Unique status count:", df["Booking Status"].nunique())


print("\n========== SECTION 2 ==========")
print("\n--- First 5 Booking ID and Customer ID ---")
print(df[["Booking ID", "Customer ID"]].head(5))

print("\n--- Last 5 Go Sedan rides ---")
sedan_rides = df[df["Vehicle Type"] == "Go Sedan"]
print(sedan_rides.tail(5))

print("\n--- Average Booking Value ---")
avg_val = df["Booking Value"].mean()
print("Average value:", avg_val)

print("\n--- Average Ride Distance ---")
avg_dist = df["Ride Distance"].mean()
print("Average distance:", avg_dist)

print("\n--- Maximum Ride Distance with Pickup Location ---")
max_dist_row = df.loc[df["Ride Distance"].idxmax()]
print("Max distance:", max_dist_row["Ride Distance"])
print("Pickup location:", max_dist_row["Pickup Location"])

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Display Booking ID, Vehicle Type and Booking Value ---")
print(df[["Booking ID", "Vehicle Type", "Booking Value"]])

print("\n--- 100th Booking ---")
print(df.iloc[99])

print("\n--- Completed Rides ---")
completed_rides = df[df["Booking Status"] == "Completed"]
print(completed_rides)

print("\n--- Booking Value > 500 ---")
high_value_rides = df[df["Booking Value"] > 500]
print(high_value_rides)

print("\n--- Completed UPI rides ---")
completed_upi = df[(df["Booking Status"] == "Completed") & (df["Payment Method"] == "UPI")]
print(completed_upi)

print("\n--- Top 5 Booking Values ---")
top_bookings = df.sort_values(by="Booking Value", ascending=False)
print(top_bookings.head(5))


print("\n========== SECTION 3 ==========")
print("\n--- Average Booking Value by Vehicle Type ---")
print(df.groupby("Vehicle Type")["Booking Value"].mean())

print("\n--- Ride Count by Payment Method ---")
print(df.groupby("Payment Method")["Booking ID"].count())

print("\n--- Total Booking Value by Pickup Location ---")
print(df.groupby("Pickup Location")["Booking Value"].sum())


print("\n========== SECTION 4 ==========")
counts = df["Vehicle Type"].value_counts()
plt.figure()
plt.bar(counts.index, counts.values)
plt.title("Vehicle Type vs Number of Rides")
plt.xlabel("Vehicle Type")
plt.ylabel("Number of Rides")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.hist(df["Booking Value"].dropna(), bins=20)
plt.title("Booking Value Distribution")
plt.xlabel("Booking Value")
plt.ylabel("Frequency")
plt.show()

pm_counts = df["Payment Method"].value_counts()
plt.figure()
plt.pie(pm_counts.values, labels=pm_counts.index, autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.show()

plt.figure()
plt.scatter(df["Ride Distance"], df["Booking Value"])
plt.title("Ride Distance vs Booking Value")
plt.xlabel("Ride Distance")
plt.ylabel("Booking Value")
plt.show()

date_avg = df.groupby("Date")["Booking Value"].mean().sort_index()
plt.figure()
plt.plot(date_avg.index, date_avg.values)
plt.title("Average Booking Value over Date")
plt.xlabel("Date")
plt.ylabel("Average Booking Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
