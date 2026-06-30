mydata = {
    "hospital":{
        "departments":[
            "CARDIO",
            "NEURO",
            {"emergency":"24 HOURS"},
            {"staff":["DOCTORS","NURSES",["SURGEON","THERAPIST"]]}
        ],
        "patients":"450"
    },
    "city":["AHMEDABAD","SURAT","VADODARA"]
}

print(mydata.keys())
print(len(mydata))
print(mydata["hospital"]["departments"][2]["emergency"])
print(mydata["hospital"]["departments"][3]["staff"][2][0])
print(mydata["hospital"]["departments"][3]["staff"][1])
print(mydata["city"][1])
print(mydata["hospital"]["patients"])
