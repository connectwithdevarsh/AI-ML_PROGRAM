import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
domestic = [220, 250, 290, 340]
international = [140, 160, 190, 230]
charter = [40, 55, 70, 95]

print("--- Airline Passenger Load Growth ---")

dom_growth = domestic[3] - domestic[0]
int_growth = international[3] - international[0]
cha_growth = charter[3] - charter[0]

print("1. Growth from Jan to Apr:")
print("Domestic:", dom_growth)
print("International:", int_growth)
print("Charter:", cha_growth)

if dom_growth > int_growth and dom_growth > cha_growth:
    print("Domestic flight segment shows the strongest contribution to passenger growth.")
elif int_growth > dom_growth and int_growth > cha_growth:
    print("International flight segment shows the strongest contribution to passenger growth.")
else:
    print("Charter flight segment shows the strongest contribution to passenger growth.")

print("\n2. Even distribution of growth:")
print("Passenger growth is not evenly distributed. Domestic grew by", dom_growth, ", International by", int_growth, ", and Charter by", cha_growth)

print("\n3. Segment requiring capacity expansion:")
print("Domestic segment has the largest volume and highest absolute growth, indicating a need for capacity expansion.")

plt.plot(months, domestic, marker="o", label="Domestic")
plt.plot(months, international, marker="s", label="International")
plt.plot(months, charter, marker="^", label="Charter")
plt.title("Airline Passenger Load Trends")
plt.xlabel("Month")
plt.ylabel("Passenger Load")
plt.legend()
plt.show()
