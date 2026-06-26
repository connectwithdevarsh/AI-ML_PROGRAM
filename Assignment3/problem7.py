import matplotlib.pyplot as plt

subjects = ["Math", "Math", "Math", "Science", "Science", "Science", "English", "English", "English"]
scores = [65, 72, 88, 60, 70, 85, 68, 75, 90]

unique_subjects = []
for s in subjects:
    if s not in unique_subjects:
        unique_subjects.append(s)

print("--- Student Exam Results ---")

sub_mins = []
sub_maxs = []
sub_sums = []
sub_counts = []

for us in unique_subjects:
    s_min = 9999
    s_max = -1
    s_sum = 0
    s_count = 0
    for i in range(len(subjects)):
        if subjects[i] == us:
            val = scores[i]
            s_sum += val
            s_count += 1
            if val < s_min:
                s_min = val
            if val > s_max:
                s_max = val
    sub_mins.append(s_min)
    sub_maxs.append(s_max)
    sub_sums.append(s_sum)
    sub_counts.append(s_count)

variations = []
averages = []

for i in range(len(unique_subjects)):
    var = sub_maxs[i] - sub_mins[i]
    avg = sub_sums[i] / sub_counts[i]
    variations.append(var)
    averages.append(avg)
    print("Subject:", unique_subjects[i], "| Score Variation:", var, "| Average:", round(avg, 2))

max_var = variations[0]
var_subject = unique_subjects[0]
for i in range(len(unique_subjects)):
    if variations[i] > max_var:
        max_var = variations[i]
        var_subject = unique_subjects[i]

print("\n1. Subject with the greatest variation in student scores:")
print(var_subject, "shows the greatest variation of", max_var, "marks.")

print("\n2. Unusually low or high scores:")
for i in range(len(scores)):
    if scores[i] <= 60:
        print("Unusually low score of", scores[i], "in", subjects[i])
    if scores[i] >= 90:
        print("Unusually high score of", scores[i], "in", subjects[i])

min_var = variations[0]
con_subject = unique_subjects[0]
for i in range(len(unique_subjects)):
    if variations[i] < min_var:
        min_var = variations[i]
        con_subject = unique_subjects[i]

print("\n3. Subject with the most consistent performance:")
print(con_subject, "demonstrates the most consistent performance with a score range of only", min_var, "marks.")

plt.bar(unique_subjects, averages, color=["orange", "blue", "green"])
plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.show()
