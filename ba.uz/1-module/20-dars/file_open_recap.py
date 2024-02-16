# "read readline readlines"

"""
read, readline, readlines
"""
with open("students.txt", 'r') as file:
    students = file.readlines()

lst = []
for student in students:
    lst.append(student.replace("\n", '').split())

lst.sort(key=lambda x: (-float(x[1]), x[0]))
print(lst)
text = ""
for i in lst:
    text = text + " ".join(i) + "\n"
print(text)
with open("sorted_students.txt", 'w') as file:
    file.write(text)
