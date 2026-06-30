import matplotlib.pyplot as plt

books = ["Book A", "Book B", "Book C", "Book D", "Book E"]
sold = [850, 720, 680, 540, 500]

plt.bar(books, sold)
plt.title("Book Sales Report")
plt.xlabel("Book Titles")
plt.ylabel("Number of Copies Sold")
plt.show()

print("Book A sold the most copies (850) and Book E sold the least copies (500).")
