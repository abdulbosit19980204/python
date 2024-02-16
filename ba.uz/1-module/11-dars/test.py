d = {
    "lst": [
        {"key1": [1, 2, 3]},
        {"key2": [1, 3]},
        {"key3": [2, 3]},
        {"key4": [1, ]},
    ]
}

f = {
    "lst": [
        {"key1": 1},
        {"key3": 3},
        {"key2": 2},
        {"key4": 1},
    ]
}
key = ""
for i in d["lst"]:
    key = list(i.keys())[0]
    for j in f["lst"]:
        jkey = list(j.keys())[0]
        if key == jkey:
            if j[key] in i[key]:
                print("ok")
            else:
                print("no")

