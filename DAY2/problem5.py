import matplotlib.pyplot as plt

products = ["P10231", "P10232", "P10233", "P10234", "P10235"]
prices = [499, 699, 899, 1099, 1299]
ratings = [3.8, 4.0, 4.2, 4.5, 4.6]
sales = [6200, 5800, 5400, 5000, 4600]

max_sales = sales[0]
max_product = products[0]
for i in range(1, len(sales)):
    if sales[i] > max_sales:
        max_sales = sales[i]
        max_product = products[i]

print("Question 1: Which traffic source contributes the most visitors over time?")
print("Note: The dataset does not contain traffic source data.")
print("If we use Sales Volume as a proxy, the highest contributor is product:", max_product, "with", max_sales, "sales.")
print()
print("Question 2: Which product shows the fastest growth rate?")
print("Note: Growth rate over time is not provided in this static dataset.")
print("Product with the highest sales volume is:", max_product)
print()
print("Question 3: Are any product declining in traffic?")
print("Note: Traffic data is not available.")
print("However, sales volume declines as product price increases (from 6200 for P10231 to 4600 for P10235).")

plt.scatter(prices, ratings, s=[s_val/10 for s_val in sales], alpha=0.6)
plt.title("Product Price vs Rating (Size represents Sales Volume)")
plt.xlabel("Price (₹)")
plt.ylabel("Rating")
plt.show()
