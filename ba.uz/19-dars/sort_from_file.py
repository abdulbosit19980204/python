"""
read, readline, readlines
"""
with open("names.txt", 'r') as file:
    students = file.readlines()

lst = []
for student in students:
    lst.append(student.replace("\n", '').split())

lst.sort(key=lambda x: (-float(x[1]), x[0]))

print(lst[-1][0])
