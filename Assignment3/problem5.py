import matplotlib.pyplot as plt

levels = ["Beginner", "Beginner", "Beginner", "Intermediate", "Intermediate", "Advanced", "Advanced"]
durations = [25, 30, 45, 50, 65, 80, 95]

unique_levels = []
for l in levels:
    if l not in unique_levels:
        unique_levels.append(l)

print("--- Online Learning Session Duration ---")

level_mins = []
level_maxs = []
level_sums = []
level_counts = []

for ul in unique_levels:
    l_min = 9999
    l_max = -1
    l_sum = 0
    l_count = 0
    for i in range(len(levels)):
        if levels[i] == ul:
            val = durations[i]
            l_sum += val
            l_count += 1
            if val < l_min:
                l_min = val
            if val > l_max:
                l_max = val
    level_mins.append(l_min)
    level_maxs.append(l_max)
    level_sums.append(l_sum)
    level_counts.append(l_count)

variations = []
averages = []

for i in range(len(unique_levels)):
    var = level_maxs[i] - level_mins[i]
    avg = level_sums[i] / level_counts[i]
    variations.append(var)
    averages.append(avg)
    print("Level:", unique_levels[i], "| Variation:", var, "mins | Average:", round(avg, 2), "mins")

max_var = variations[0]
var_level = unique_levels[0]
for i in range(len(unique_levels)):
    if variations[i] > max_var:
        max_var = variations[i]
        var_level = unique_levels[i]

print("\n1. Course level with widest variation in session duration:")
print("The", var_level, "level shows the widest variation of", max_var, "minutes.")

print("\n2. Consistency of advanced learners vs beginners:")
beg_var = variations[0]
adv_var = variations[2]
if adv_var < beg_var:
    print("Yes, advanced learners are more consistent (variation:", adv_var, "mins) compared to beginners (variation:", beg_var, "mins).")
else:
    print("No, advanced learners are not more consistent.")

print("\n3. Engagement pattern interpretation:")
print("Average session duration increases with course level (Beginner:", round(averages[0], 2), "mins, Intermediate:", round(averages[1], 2), "mins, Advanced:", round(averages[2], 2), "mins). This suggests that advanced learners are much more engaged and spend more time on the platform.")

plt.bar(unique_levels, averages, color=["gray", "blue", "orange"])
plt.title("Average Session Duration by Course Level")
plt.xlabel("Course Level")
plt.ylabel("Average Duration (minutes)")
plt.show()
