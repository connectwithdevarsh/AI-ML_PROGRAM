import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "June"]
partner_a = [800, 950, 1100, 1300, 1500, 1550]
partner_b = [600, 700, 820, 980, 1020, 1060]

print("--- E-Commerce Order Fulfillment Growth ---")

growth_a = partner_a[5] - partner_a[0]
growth_b = partner_b[5] - partner_b[0]

print("1. Growth in order fulfillment:")
print("Partner A growth:", growth_a, "orders")
print("Partner B growth:", growth_b, "orders")
if growth_a > growth_b:
    print("Partner A shows faster growth in order fulfillment.")
else:
    print("Partner B shows faster growth in order fulfillment.")

print("\n2. Single partner dependency analysis:")
total_june = partner_a[5] + partner_b[5]
pct_a = (partner_a[5] / total_june) * 100
print("In June, Partner A handles", round(pct_a, 2), "% of total orders.")
if pct_a > 55:
    print("Yes, the company is becoming overly dependent on Partner A.")
else:
    print("No, the distribution is balanced.")

print("\n3. Order distribution adjustment recommendation:")
print("Redistribute a portion of orders from Partner A to Partner B to maintain a balanced allocation (e.g. 50-50 share) and avoid bottlenecks.")

plt.plot(months, partner_a, marker="o", color="blue", label="Partner A")
plt.plot(months, partner_b, marker="s", color="green", label="Partner B")
plt.title("Logistics Partner Order Fulfillment Trend")
plt.xlabel("Month")
plt.ylabel("Orders Fulfilled")
plt.legend()
plt.show()
