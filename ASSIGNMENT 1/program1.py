mydata = [
    {
        "states": [
            "GUJARAT",
            "RAJASTHAN",
            {"PORTION": "WEST INDIA"},
            {"LANGUAGES": ["GUJARATI", "MARWADI", ["HINDI", "ENGLISH"]]}
        ]
    },
    {
        "CODES": {
            "GUJARAT": "GJ",
            "RAJASTHAN": "RJ"
        }
    },
    ["7.07 CR", "8.5 CR"]
]

keys = [list(mydata[0])[0], list(mydata[1])[0]]
print("Total number of main keys:", len(keys))
print("Names of all main keys:", keys)
print("GJ:", mydata[1]["CODES"]["GUJARAT"])
print("GUJARAT:", mydata[0]["states"][0])
print("MARWADI:", mydata[0]["states"][3]["LANGUAGES"][1])
print("ENGLISH:", mydata[0]["states"][3]["LANGUAGES"][2][1])
print("WEST INDIA:", mydata[0]["states"][2]["PORTION"])
print("7.07 CR:", mydata[2][0])
