cfile_number = int(input())
d = {
    "lst": []
}
o = {
    "lst": []
}
for i in range(cfile_number):
    txt = input().split()
    d_op = {
        "file_name": txt[0],
        "access": txt[1:]
    }
    d["lst"].append(d_op)

oper_num = int(input())

for i in range(oper_num):
    txt = input().split()
    if txt[0] == "read":
        txt[0] = "R"
    elif txt[0] == "write":
        txt[0] = "W"
    elif txt[0] == "execute":
        txt[0] = "X"
    d_o = {
        "command": txt[0],
        "file_name": txt[1]
    }
    o["lst"].append(d_o)

for i in d:
    print(i["access"], i["file_name"])

for command in o["lst"]:
    if command["command"] in d["lst"][0]["access"]:
        # print(command["command"])
        print("OK")
    else:
        # print(command["command"])
        print("Access denied")
