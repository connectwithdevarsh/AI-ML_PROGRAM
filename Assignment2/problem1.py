# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt

hours = ["8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM"]
transactions = [1200, 1800, 2600, 3200, 4100, 3800, 3600, 4200, 4700, 5200]

print("--- E-Wallet Transaction Volume Analysis ---")
print("1. Hours where transaction volume increases sharply:")
for i in range(len(transactions) - 1):
    diff = transactions[i+1] - transactions[i]
    if diff >= 600:
        print("Increase from", hours[i], "to", hours[i+1], "is", diff, "transactions")

print("\n2. Periods of unusually low transaction activity:")
min_val = transactions[0]
min_hour = hours[0]
for i in range(len(transactions)):
    if transactions[i] < min_val:
        min_val = transactions[i]
        min_hour = hours[i]
print("Lowest activity is at", min_hour, "with", min_val, "transactions")

print("\n3. System capacity recommendation:")
max_val = transactions[0]
max_hour = hours[0]
for i in range(len(transactions)):
    if transactions[i] > max_val:
        max_val = transactions[i]
        max_hour = hours[i]
print("Peak traffic is at", max_hour, "with", max_val, "transactions. Upgrade capacity during this period.")

plt.plot(hours, transactions, marker="o", color="blue", linewidth=2)
plt.title("Transaction Volume over Time")
plt.xlabel("Hour of the Day")
plt.ylabel("Number of Transactions")
plt.grid(True)
plt.show()
