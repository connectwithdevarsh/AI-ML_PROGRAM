mydata = {
    "maharashtra": {
        "mumbai": {
            "city": "metro city",
            "metro": "yes"
        },
        "population": "20 cr"
    },
    "gujarat": [
        "AHMEDABAD",
        "SURAT",
        "RAJKOT"
    ],
    "rajasthan": [
        "AJMER",
        "JAISALMER",
        {
            "capital": "jaipur"
        },
        [
            "MEWAD",
            "RJ",
            "INR"
        ]
    ]
}

keys = list(mydata)
print("All main keys:", keys)
print("Total number of main keys:", len(keys))
print("Metro City:", mydata["maharashtra"]["mumbai"]["city"])
print("Capital of Rajasthan:", mydata["rajasthan"][2]["capital"])
print("City in Gujarat:", mydata["gujarat"][2])
print("State code for Rajasthan:", mydata["rajasthan"][3][1])
