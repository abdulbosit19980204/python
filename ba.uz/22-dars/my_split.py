txt = "1 2 3 4 5"


# txt = "1.2.3.4.5.6"


def my_splitter(txt, sep=" "):
    new_lst = []
    s = 0
    f_ind = 0
    s_ind = 0
    for i in range(len(txt)):
        if txt[i] == sep:
            f_ind = s_ind
            s_ind = i
            new_lst.append(txt[f_ind: s_ind])
    new_lst.append(txt[s_ind:])
    return new_lst


print(my_splitter(txt))
