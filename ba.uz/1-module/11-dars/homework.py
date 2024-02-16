from random import randint
d = {
    "cars": []
}
n = int(input("number of cars: "))

for i in range(1, n + 1):
    d_c = {
        "model": f"nexia-{i}",
        "year": 2000 + randint(1, 23),
        "price": randint(7000, 11000),
        "probeg": randint(0, 100000)
    }
    d["cars"].append(d_c)

answer = input("Do you want to sort card by price/year/probeg ?: ")

if answer not in ("price", "year", "probeg"):
    print("Sorry, I didn't understand")
    raise ValueError("You have to choose on of price/year/probeg")

d["cars"].sort(key=lambda x: x[answer])


for i in d["cars"]:
    print(i["model"], i["year"], i["price"], i["probeg"])
