# List Comprehension

numbers =[22,55,33,77,88,99,222,2222,]
newNumber = []

for x in numbers:
    if x%2==0:
        newNumber.append(x)

print(newNumber) #[22, 88, 222, 2222]

# With list comprehension you can do all that with only one line of code

numbers = ["2121","5454","8787","9898","454"]
newNumber = [x for x in numbers if "5" in x]
print(newNumber) #['5454', '454']
