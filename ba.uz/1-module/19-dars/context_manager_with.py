with open("names.txt", 'r') as file:
    names = file.readlines()
    Nnames = []
    rates = []
    for i in names:
        name, rate = i.split()
        Nnames.append(name)
        rates.append(float(rate.replace('\n', '')))

    ind = rates.index(max(rates))
    print(names[ind])
