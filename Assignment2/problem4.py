import matplotlib.pyplot as plt

rooms = ["R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10"]
usage = [6, 4, 8, 5, 7, 9, 3, 6, 10, 2]

print("--- Corporate Meeting Room Utilization ---")
print("1. Underutilized and Overutilized rooms:")
total_usage = 0
for u in usage:
    total_usage += u
avg_usage = total_usage / len(rooms)
print("Average usage is", avg_usage, "hours")

print("Overutilized rooms (usage >= 8 hours):")
for i in range(len(usage)):
    if usage[i] >= 8:
        print(rooms[i], "with", usage[i], "hours")

print("Underutilized rooms (usage <= 3 hours):")
for i in range(len(usage)):
    if usage[i] <= 3:
        print(rooms[i], "with", usage[i], "hours")

print("\n2. Distribution of room usage:")
min_val = usage[0]
max_val = usage[0]
for u in usage:
    if u < min_val:
        min_val = u
    if u > max_val:
        max_val = u
print("Usage is not evenly distributed. Range is from", min_val, "hours (R10) to", max_val, "hours (R9).")

print("\n3. Scheduling optimization strategy:")
print("Reroute meeting bookings from overutilized rooms (R9, R6, R3) to underutilized rooms (R10, R7).")

plt.bar(rooms, usage, color="purple")
plt.title("Meeting Room Usage Hours")
plt.xlabel("Room ID")
plt.ylabel("Usage Time (hours)")
plt.show()
