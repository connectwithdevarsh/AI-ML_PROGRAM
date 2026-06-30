import matplotlib.pyplot as plt

weeks = ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5", "Week 6"]
bounce_rate = [65, 63, 61, 60, 58, 55]

plt.plot(weeks, bounce_rate)
plt.title("Website Bounce Rate Trend")
plt.xlabel("Weeks")
plt.ylabel("Bounce Rate (%)")
plt.show()

print("The website bounce rate has decreased from 65% in Week 1 to 55% in Week 6, showing improvement.")
