import matplotlib.pyplot as plt

routes = ["Route A", "Route A", "Route B", "Route B", "Route C", "Route C", "Route D", "Route D", "Route E", "Route E"]
delays = [5, 12, 18, 25, 8, 15, 30, 45, 10, 20]

unique_routes = []
for r in routes:
    if r not in unique_routes:
        unique_routes.append(r)

route_avgs = []
route_diffs = []

print("--- Public Bus Route Punctuality Evaluation ---")
for ur in unique_routes:
    total = 0
    count = 0
    rmin = 99999
    rmax = -1
    for i in range(len(routes)):
        if routes[i] == ur:
            total += delays[i]
            count += 1
            if delays[i] < rmin:
                rmin = delays[i]
            if delays[i] > rmax:
                rmax = delays[i]
    avg = total / count
    diff = rmax - rmin
    route_avgs.append(avg)
    route_diffs.append(diff)
    print("Route:", ur, "| Average Delay:", avg, "mins | Variation (Max-Min):", diff, "mins")

print("\n1. Route with the most frequent/highest delays:")
max_avg = route_avgs[0]
max_route = unique_routes[0]
for i in range(len(unique_routes)):
    if route_avgs[i] > max_avg:
        max_avg = route_avgs[i]
        max_route = unique_routes[i]
print("Route", max_route, "has the highest average delay of", max_avg, "minutes.")

print("\n2. Inconsistency across routes:")
max_diff = route_diffs[0]
inc_route = unique_routes[0]
for i in range(len(unique_routes)):
    if route_diffs[i] > max_diff:
        max_diff = route_diffs[i]
        inc_route = unique_routes[i]
print("Route", inc_route, "is the most inconsistent with a delay variation of", max_diff, "minutes.")

print("\n3. Focus areas for scheduling/route optimization:")
print("Priority 1: Route D (highest average delay and highest inconsistency)")
print("Priority 2: Route B (second highest average delay)")

plt.bar(unique_routes, route_avgs, color="brown")
plt.title("Average Bus Arrival Delay by Route")
plt.xlabel("Bus Route")
plt.ylabel("Average Delay (minutes)")
plt.show()
