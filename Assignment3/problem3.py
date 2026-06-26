import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu"]
residential = [120, 130, 140, 155]
commercial = [90, 95, 100, 110]
industrial = [150, 160, 170, 180]

print("--- Smart City Water Consumption ---")

res_total = 0
com_total = 0
ind_total = 0

for v in residential:
    res_total += v
for v in commercial:
    com_total += v
for v in industrial:
    ind_total += v

print("Total consumption:")
print("Residential:", res_total)
print("Commercial:", com_total)
print("Industrial:", ind_total)

if ind_total > res_total and ind_total > com_total:
    print("\n1. Sector that consumes the most water: Industrial")
elif res_total > ind_total and res_total > com_total:
    print("\n1. Sector that consumes the most water: Residential")
else:
    print("\n1. Sector that consumes the most water: Commercial")

print("\n2. Industrial usage trend:")
print("Industrial water usage is increasing steadily day-by-day (from", industrial[0], "to", industrial[3], ").")

print("\n3. Sufficiency of Residential supply:")
print("Residential consumption is increasing from", residential[0], "to", residential[3], ". If supply does not increase proportionally, there could be a shortage.")

plt.plot(days, residential, marker="o", label="Residential")
plt.plot(days, commercial, marker="x", label="Commercial")
plt.plot(days, industrial, marker="d", label="Industrial")
plt.title("Smart City Sector-wise Water Consumption")
plt.xlabel("Day")
plt.ylabel("Water Consumption (Litres/Units)")
plt.legend()
plt.show()
