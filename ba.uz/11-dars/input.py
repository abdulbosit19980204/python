cfile_number = int(input())
d = {
    "lst": []
}

o = {
    "lst": []
}

for i in range(cfile_number):
    f = {}
    txt = input().split()
    f[txt[0]] = txt[1:]
    d["lst"].append(f)

oper_num = int(input())

for i in range(oper_num):
    f = {}
    txt = input().split()
    if txt[0] == "read":
        txt[0] = "R"
    elif txt[0] == "write":
        txt[0] = "W"
    elif txt[0] == "execute":
        txt[0] = "X"

    f[txt[1]] = txt[0]
    o["lst"].append(f)
# print(d["lst"])
# print(o["lst"])
for i in d["lst"]:
    key = list(i.keys())[0]
    for j in o["lst"]:
        jkey = list(j.keys())[0]
        if key == jkey:
            if j[key] in i[key]:
                print("key=>",key, "j[key]=>",j[key], "i[key]=>",i[key])
                print("OK")
            else:
                print("key=>",key, "j[key]=>",j[key], "i[key]=>",i[key])
                print("Access denied")




"""
4
hello.exe R X
ping W R
nya R
gluck X W R
5
read nya
write hello.exe
read ping
execute ping
write nya

"""
