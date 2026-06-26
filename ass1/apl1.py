import requests

# API URL
url = "https://api.openbrewerydb.org/v1/breweries"

# Fetch data from API
response = requests.get(url)

if response.status_code == 200:
    breweries = response.json()

    # Fetch one brewery record (first record)
    brewery = breweries[0]

    # Count total keys
    total_keys = len(brewery)

    # Print key names using loop
    print("=============== KEY NAMES ===============")
    for key in brewery.keys():
        print(key)

    print("\nTotal Keys:", total_keys)

    # Brewery Information Report
    print("\n================ BREWERY INFORMATION REPORT =================")
    print(f"Brewery Name     : {brewery.get('name')}")
    print(f"Brewery Type     : {brewery.get('brewery_type')}")
    print(f"City             : {brewery.get('city')}")
    print(f"Country          : {brewery.get('country')}")
    print(f"Website URL      : {brewery.get('website_url')}")
else:
    print("Failed to fetch data.")