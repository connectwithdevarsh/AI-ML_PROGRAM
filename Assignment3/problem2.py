import matplotlib.pyplot as plt

teams = ["Backend", "Backend", "Backend", "Frontend", "Frontend", "Frontend", "QA", "QA", "QA"]
times = [4, 6, 9, 3, 5, 7, 2, 3, 4]

unique_teams = []
for t in teams:
    if t not in unique_teams:
        unique_teams.append(t)

print("--- Software Bug Resolution Time ---")

team_maxs = []
team_mins = []
team_sums = []
team_counts = []

for ut in unique_teams:
    t_min = 9999
    t_max = -1
    t_sum = 0
    t_count = 0
    for i in range(len(teams)):
        if teams[i] == ut:
            val = times[i]
            t_sum += val
            t_count += 1
            if val < t_min:
                t_min = val
            if val > t_max:
                t_max = val
    team_mins.append(t_min)
    team_maxs.append(t_max)
    team_sums.append(t_sum)
    team_counts.append(t_count)

variabilities = []
averages = []

for i in range(len(unique_teams)):
    var = team_maxs[i] - team_mins[i]
    avg = team_sums[i] / team_counts[i]
    variabilities.append(var)
    averages.append(avg)
    print("Team:", unique_teams[i], "| Range:", var, "hours | Average:", round(avg, 2), "hours")

max_var = variabilities[0]
var_team = unique_teams[0]
for i in range(len(unique_teams)):
    if variabilities[i] > max_var:
        max_var = variabilities[i]
        var_team = unique_teams[i]

print("\n1. Team with highest variability:")
print(var_team, "team has the highest variability of", max_var, "hours.")

print("\n2. Unusually long resolution times:")
long_time = 8
for i in range(len(times)):
    if times[i] > long_time:
        print("Bug resolved by", teams[i], "took an unusually long time of", times[i], "hours.")

min_avg = averages[0]
eff_team = unique_teams[0]
for i in range(len(unique_teams)):
    if averages[i] < min_avg:
        min_avg = averages[i]
        eff_team = unique_teams[i]

print("\n3. Most efficient team:")
print(eff_team, "team is the most efficient with an average resolution time of", round(min_avg, 2), "hours.")

plt.bar(unique_teams, averages, color=["red", "blue", "green"])
plt.title("Average Bug Resolution Time by Team")
plt.xlabel("Team")
plt.ylabel("Average Resolution Time (Hours)")
plt.show()
