import matplotlib.pyplot as plt

days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6"]
streaming_hours = [3, 4, 5, 6, 7, 9]

plt.plot(days, streaming_hours)
plt.title("Daily Video Streaming Hours")
plt.xlabel("Days")
plt.ylabel("Streaming Hours")
plt.show()

print("The daily video streaming hours show a steady rise, starting at 3 hours and reaching 9 hours.")
