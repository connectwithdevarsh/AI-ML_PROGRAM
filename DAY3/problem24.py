import matplotlib.pyplot as plt

stream = {"Service": ["Netflix", "Amazon Prime", "Disney+", "HBO Max"], "Subscribers(M)": [200, 150, 100, 80]}

plt.bar(stream["Service"], stream["Subscribers(M)"])
plt.title("Streaming Services Subscribers")
plt.xlabel("Streaming Platform")
plt.ylabel("Subscribers (in Millions)")
plt.show()

print("Netflix has the highest subscriber count of 200 Million, and HBO Max has the lowest count of 80 Million.")
