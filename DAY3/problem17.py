import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
attendance = [70, 75, 78, 80, 85, 90, 95]

plt.plot(days, attendance)
plt.title("Weekly Student Attendance")
plt.xlabel("Days of the Week")
plt.ylabel("Attendance Percentage (%)")
plt.show()

print("The student attendance has improved throughout the week from 70% on Monday to 95% on Sunday.")
