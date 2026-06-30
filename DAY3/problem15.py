import matplotlib.pyplot as plt

years = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
cloud_users = [100, 140, 190, 250, 320, 400, 500]

plt.plot(years, cloud_users)
plt.title("Cloud Users Growth")
plt.xlabel("Years")
plt.ylabel("Number of Cloud Users")
plt.show()

print("The number of cloud users has grown from 100 in 2018 to 500 in 2024.")
