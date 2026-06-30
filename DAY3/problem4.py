import matplotlib.pyplot as plt

hospitals = ["Apollo", "Fortis", "AIIMS", "Medanta", "Narayana"]
patients = [620, 580, 700, 540, 500]

plt.bar(hospitals, patients)
plt.title("Patients Treated Per Day at Hospitals")
plt.xlabel("Hospital Names")
plt.ylabel("Number of Patients")
plt.show()

print("AIIMS has the highest patient count per day (700) and Narayana has the lowest patient count (500).")
