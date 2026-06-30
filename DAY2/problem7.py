import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
occupancy = [45, 50, 58, 65, 72, 80, 88, 85, 70, 62]

peak_months = []
for i in range(len(months)):
    if occupancy[i] >= 80:
        peak_months.append(months[i])

max_occ = max(occupancy)
min_occ = min(occupancy)
diff = max_occ - min_occ

is_pattern = "Yes, occupancy rises from winter to summer (Jan to Jul) and then starts falling in autumn (Aug to Oct)."

print("Question 1: Which months represent peak occupancy periods?")
print("Peak occupancy months (>= 80%):", ", ".join(peak_months))
print()
print("Question 2: How large is the occupancy difference between peak and off-season?")
print(f"Difference: {diff}% (Peak: {max_occ}%, Off-season: {min_occ}%)")
print()
print("Question 3: Is there a consistent seasonal pattern in occupancy?")
print(is_pattern)

plt.plot(months, occupancy, marker='o')
plt.title("Hotel Room Occupancy Across Seasons")
plt.xlabel("Month")
plt.ylabel("Occupancy (%)")
plt.show()
