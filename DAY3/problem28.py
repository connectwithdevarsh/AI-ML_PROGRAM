import matplotlib.pyplot as plt

online = {"Course": ["Python", "Data Science", "JavaScript", "AI"], "Students": [50, 40, 35, 30]}

plt.bar(online["Course"], online["Students"])
plt.title("Online Course Student Enrollments")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.show()

print("Python is the most popular course with 50 students enrolled, and AI has the fewest with 30 students.")
