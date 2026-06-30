import matplotlib.pyplot as plt

gym = {"Activity": ["Yoga", "Cardio", "Weightlifting", "Zumba"], "Participants": [20, 15, 25, 10]}

plt.bar(gym["Activity"], gym["Participants"])
plt.title("Gym Activities Participation")
plt.xlabel("Gym Activities")
plt.ylabel("Number of Participants")
plt.show()

print("Weightlifting has the highest number of participants (25), and Zumba has the lowest (10).")
