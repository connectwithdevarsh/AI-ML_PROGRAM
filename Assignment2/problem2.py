import matplotlib.pyplot as plt

batches = ["B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "B9", "B10"]
times = [14, 18, 22, 16, 25, 19, 30, 28, 20, 35]

print("--- Manufacturing Quality Inspection Time ---")
print("1. Batches that take the longest to inspect (above 25 minutes):")
for i in range(len(times)):
    if times[i] > 25:
        print(batches[i], "takes", times[i], "minutes")

print("\n2. Variations in inspection time:")
min_time = times[0]
max_time = times[0]
for t in times:
    if t < min_time:
        min_time = t
    if t > max_time:
        max_time = t
variation = max_time - min_time
print("Minimum inspection time:", min_time, "minutes")
print("Maximum inspection time:", max_time, "minutes")
print("Range/Variation is", variation, "minutes. This indicates a high variation.")

print("\n3. Inspection stages requiring process optimization:")
total_time = 0
for t in times:
    total_time += t
avg_time = total_time / len(times)
print("Average inspection time is", avg_time, "minutes.")
print("Batches taking longer than average should be optimized:")
for i in range(len(times)):
    if times[i] > avg_time:
        print("Batch", batches[i], "takes", times[i], "minutes")

plt.bar(batches, times, color="green")
plt.title("Inspection Time per Batch")
plt.xlabel("Batch Number")
plt.ylabel("Inspection Time (minutes)")
plt.show()
