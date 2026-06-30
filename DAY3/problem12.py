import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
likes_growth = [120, 180, 250, 340, 460, 600]

plt.plot(months, likes_growth)
plt.title("Social Media Likes Growth")
plt.xlabel("Months")
plt.ylabel("Number of Likes")
plt.show()

print("The social media likes show a steady growth from 120 likes to 600 likes over 6 months.")
