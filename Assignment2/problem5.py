import matplotlib.pyplot as plt

stations = ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10"]
rainfall = [42, 55, 38, 70, 90, 48, 110, 60, 35, 85]

print("--- Weather Station Rainfall Variability Study ---")
print("1. Stations with highest rainfall levels (>= 85):")
for i in range(len(rainfall)):
    if rainfall[i] >= 85:
        print(stations[i], "with", rainfall[i], "mm")

print("\n2. Stations with extreme rainfall deviations:")
total_rain = 0
for r in rainfall:
    total_rain += r
avg_rain = total_rain / len(stations)
print("Average rainfall across all stations:", avg_rain, "mm")

print("Significant deviations from average (deviation > 20 mm):")
for i in range(len(rainfall)):
    dev = rainfall[i] - avg_rain
    if dev > 20 or dev < -20:
        print(stations[i], "has rainfall of", rainfall[i], "mm (Deviation:", round(dev, 2), "mm)")

print("\n3. Rainfall distribution variability:")
min_rain = rainfall[0]
max_rain = rainfall[0]
for r in rainfall:
    if r < min_rain:
        min_rain = r
    if r > max_rain:
        max_rain = r
print("Rainfall varies widely across locations, from a minimum of", min_rain, "mm (S9) to a maximum of", max_rain, "mm (S7).")

plt.bar(stations, rainfall, color="teal")
plt.title("Rainfall Level per Weather Station")
plt.xlabel("Weather Station")
plt.ylabel("Rainfall (mm)")
plt.show()
