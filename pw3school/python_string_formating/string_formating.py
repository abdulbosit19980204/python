# Python String Formating
# To make sure a string will display as expected, we can format the result with the format()  method

# String Format()

# The format() method allows you to format selected parts of a string
# Sometimes there are parts of text that you do not control, maybe they come from a database, or user input?
# To control such values, add placeholders(curly brackets {}) in the text, and run the values through the format() method
# Add a placeholder where you want to display the price

price = 45
txt = "The black notebook's price is {} dollars"
print(txt.format(price))
# The black notebook's price is 45 dollars

# You can add parameters inside the curly brackets to specify how to convert the value
# Format the price to be displayed as a number with two decimals
txt = "The price is {:.2f} dollars"
print(txt.format(price))
# The price is 45.00 dollars

# Multiple Values
# If you want to use more values, just add more values to the format() method
itemno = 2
count = 5
price = 50.22
txt = "The {} item has about {} additional price. So it costs {:.2f} dollars "
print(txt.format(itemno, count, price))
# The 2 item has about 5 additional price. So it costs 50.22 dollars

# Index Numbers
# You can use index numbers (a number inside the curly brackets {0}) to be sure the values are placed in the correct placeholder
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# Also, if you want to refer to the same value more than once, use the index number:

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

# Named Indexes
# You can also use named indexes by entering a name inside the curly brackets {carname},
# but then you must use names when you pass the parameter values txt.format(carname = "Ford"):
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname="Ford", model="Mustang"))
