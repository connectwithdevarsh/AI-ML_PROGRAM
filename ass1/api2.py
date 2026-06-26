import requests

# API URL
url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"

# Send GET request
response = requests.get(url)

if response.status_code == 200:
    # Convert JSON response to Python list
    metro_data = response.json()

    # Retrieve first metro line status record
    line = metro_data[0]

    # Count total keys
    total_keys = len(line)

    # Print all key names
    print("=============== AVAILABLE KEYS ===============")
    for key in line.keys():
        print(key)

    print("\nTotal Keys:", total_keys)

    # Metro Status Report
    print("\n================ METRO STATUS REPORT =================")
    print(f"Line Name          : {line.get('name')}")
    print(f"Current Status     : {line['lineStatuses'][0].get('statusSeverityDescription')}")
    print(f"Severity Level     : {line['lineStatuses'][0].get('statusSeverity')}")
    print(f"Reason Description : {line['lineStatuses'][0].get('reason', 'No issues reported')}")
    print(f"Line Identifier    : {line.get('id')}")

else:
    print("Failed to retrieve data.")
    print("Status Code:", response.status_code)