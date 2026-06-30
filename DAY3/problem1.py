import matplotlib.pyplot as plt

hotels = ["Hotel A", "Hotel B", "Hotel C", "Hotel D", "Hotel E"]
bookings = [420, 380, 340, 290, 260]

plt.bar(hotels, bookings)
plt.title("Hotel Room Bookings")
plt.xlabel("Hotels")
plt.ylabel("Number of Bookings")
plt.show()

print("Hotel A has the highest bookings with 420, while Hotel E has the lowest bookings with 260.")
