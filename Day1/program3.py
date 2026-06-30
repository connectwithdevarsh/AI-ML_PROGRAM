mydata = {
    "bank":{
        "accounts":[
            "SAVING",
            "CURRENT",
            {"loan":"HOME LOAN"},
            {"cards":["ATM","CREDIT",["VISA","RUPAY"]]}
        ],
        "branches":"120"
    },
    "cities":["DELHI","MUMBAI","PUNE"]
}

print(mydata.keys())
print(len(mydata))
print(mydata["bank"]["accounts"][2]["loan"])
print(mydata["bank"]["accounts"][3]["cards"][2][1])
print(mydata["bank"]["accounts"][1])
print(mydata["cities"][2])
print(mydata["bank"]["branches"])
