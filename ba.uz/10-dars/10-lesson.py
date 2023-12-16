d = {
    "fakultet": "Filologiya",
    "students": [
        {
            "first_name": "Ali",
            "avg_mark": 4.3
        },
        {
            "first_name": "Vali",
            "avg_mark": 5.4
        },
        {
            "first_name": "G'ani",
            "avg_mark": 4.6
        },
        {
            "first_name": "Sherali",
            "avg_mark": 8
        }
    ]
}

# print(d["students"][0]["first_name"])
marks = [d["students"][i]["avg_mark"] for i in range(len(d["students"]))]
info = [d["students"][i] for i in range(len(d["students"]))]

maxRate =marks.index(max(marks))
print(info[maxRate])