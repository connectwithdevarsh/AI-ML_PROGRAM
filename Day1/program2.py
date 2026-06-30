mydata = {
    "school":[
        {"class":"10TH","fees":{"annual":"35000"}},
        {"subjects":["MATHS","SCIENCE",["ENGLISH","HINDI"]]},
        {"principal":"MR SHAH"}
    ],
    "students":["RAHUL","PRIYA","AMAN"]
}

print(mydata.keys())
print(len(mydata))
print(mydata["school"][0]["fees"]["annual"])
print(mydata["school"][1]["subjects"][2][1])
print(mydata["school"][1]["subjects"][1])
print(mydata["school"][2]["principal"])
print(mydata["students"][1])
