import matplotlib.pyplot as plt

categories = ["Technology", "Business", "Design", "Personal Development", "Marketing", "Data Science", "Finance", "Language", "Healthcare", "Others"]
enrollments = [4200, 3100, 1800, 2400, 1500, 3600, 2000, 1700, 1300, 900]

max_enroll = enrollments[0]
max_cat = categories[0]
for i in range(1, len(enrollments)):
    if enrollments[i] > max_enroll:
        max_enroll = enrollments[i]
        max_cat = categories[i]

tech_categories = ["Technology", "Data Science"]
tech_sum = 0
non_tech_sum = 0
for i in range(len(categories)):
    if categories[i] in tech_categories:
        tech_sum += enrollments[i]
    else:
        non_tech_sum += enrollments[i]

gap = abs(tech_sum - non_tech_sum)

promo_cats = []
for i in range(len(categories)):
    if enrollments[i] < 1800:
        promo_cats.append(categories[i])

print("Question 1: Which course category attracts the most learners?")
print("Top category:", max_cat, f"({max_enroll} enrollments)")
print()
print("Question 2: How significant is the enrollment gap between technical and non-technical courses?")
print(f"Technical: {tech_sum}, Non-Technical: {non_tech_sum}")
print(f"Enrollment gap: {gap}")
print()
print("Question 3: Which categories may need promotional focus?")
print("Categories needing promotion (< 1800 enrollments):", ", ".join(promo_cats))

plt.pie(enrollments, labels=categories, autopct='%1.1f%%')
plt.title("Online Course Category Enrollment Share")
plt.show()
