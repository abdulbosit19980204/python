# d = {
#     "fakultet": "Filologiya",
#     "students": [
#         {
#             "first_name": "Ali",
#             "avg_mark": 4.3
#         },
#         {
#             "first_name": "Vali",
#             "avg_mark": 5.4
#         },
#         {
#             "first_name": "G'ani",
#             "avg_mark": 4.6
#         },
#         {
#             "first_name": "Sherali",
#             "avg_mark": 8
#         }
#     ]
# }
#
# # print(d["students"][0]["first_name"])
# marks = [d["students"][i]["avg_mark"] for i in range(len(d["students"]))]
# info = [d["students"][i] for i in range(len(d["students"]))]
#
# maxRate =marks.index(max(marks))
# print(info[maxRate])
#
#
# d = {
#     "fakultet": "Filologiya",
#     "students": [
#         {
#             "first_name": "Ali",
#             "avg_mark": 4.3
#         },
#         {
#             "first_name": "Vali",
#             "avg_mark": 3.4
#         },
#         {
#             "first_name": "G'ani",
#             "avg_mark": 4.6
#         },
#         {
#             "first_name": "Damir",
#             "avg_mark": 3.2
#         },
#         {
#             "first_name": "Abbos",
#             "avg_mark": 3.1
#         }
#     ]
# }
#
# students = d["students"]
# student_mark = 0
# student_name = ""
#
# for student in students:
#     if student_mark < student["avg_mark"]:
#         student_name = student["first_name"]
#         student_mark = student["avg_mark"]
#
# print(student_name, student_mark)


d = {
    "fakultet": "Filologiya",
    "students": [
        {
            "first_name": "Ali",
            "avg_mark": 4.3
        },
        {
            "first_name": "Vali",
            "avg_mark": 3.4
        },
        {
            "first_name": "G'ani",
            "avg_mark": 4.6
        },
        {
            "first_name": "Damir",
            "avg_mark": 3.2
        },
        {
            "first_name": "Abbos",
            "avg_mark": 3.1
        }
    ]
}

students = d["students"]
student_mark = 0
student_data = {}

for student in students:
    if student_mark < student["avg_mark"]:
        student_data = student
        student_mark = student["avg_mark"]

print(student_data, student_mark)