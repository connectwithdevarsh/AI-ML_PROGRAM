import matplotlib.pyplot as plt

intervals = ["I1", "I2", "I3", "I4", "I5", "I6", "I7", "I8", "I9", "I10"]
response_times = [120, 150, 180, 220, 260, 310, 280, 240, 190, 350]

print("--- Corporate Email Server Response Monitoring ---")
print("1. Intervals where response time degrades most (>= 280 ms):")
for i in range(len(response_times)):
    if response_times[i] >= 280:
        print("Interval", intervals[i], "has response time of", response_times[i], "ms")

print("\n2. Extreme latency values affecting communication:")
max_time = response_times[0]
for t in response_times:
    if t > max_time:
        max_time = t
print("The maximum latency observed is", max_time, "ms at interval I10, which significantly slows down email delivery.")

print("\n3. Recommended timing for server scaling/optimization:")
print("Optimization and auto-scaling should be scheduled before peaks, specifically before I5-I7 and I10.")

plt.plot(intervals, response_times, marker="d", color="red", linewidth=2)
plt.title("Email Server Response Time")
plt.xlabel("Interval")
plt.ylabel("Response Time (ms)")
plt.grid(True)
plt.show()
