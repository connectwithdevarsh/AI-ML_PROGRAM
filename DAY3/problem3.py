import matplotlib.pyplot as plt

telecom = ["Jio", "Airtel", "Vi", "BSNL", "MTNL"]
users = [4600, 4200, 2800, 2100, 900]

plt.bar(telecom, users)
plt.title("Telecom Companies User Base")
plt.xlabel("Telecom Operators")
plt.ylabel("Number of Users (in Thousands)")
plt.show()

print("Jio has the highest user base of 4600, whereas MTNL has the lowest user base of 900.")
