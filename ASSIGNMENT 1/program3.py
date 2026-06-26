mydata = {
    "category": [
        {
            "A": "FIRST",
            "package": {
                "data": "2lacs"
            }
        },
        {
            "B": "Second",
            "data": {
                "new": [
                    100
                ]
            }
        },
        {
            "C": "Third",
            "Tests": [
                45,
                75,
                25
            ]
        }
    ]
}

keys = list(mydata)
print("All keys:", keys)
print("Total number of keys:", len(keys))
print("Package data:", mydata["category"][0]["package"]["data"])
print("Test value:", mydata["category"][2]["Tests"][2])
print("New data value:", mydata["category"][1]["data"]["new"][0])
