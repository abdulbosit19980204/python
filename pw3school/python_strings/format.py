# String Format

# We can combine strings and numbers using the format() method.

age=25
name="Abdulbosit"
text = "My name is {}. I am {} years old "
print(text.format(name, age)) #My name is Abdulbosit. I am 25 years old

# The format() methods takes unlimited number of arguments

text = "My name is {}. I am {} years old. I am from {}. I have about {}$ salary."
salary=2500
country="Uzbekistan"

print(text.format(name, age, country, salary)) #My name is Abdulbosit. I am 25 years old. I am from Uzbekistan. I have about 2500$ salary.

# We can use index number to be sure the arguments are placed in the correct placeholders:
text = "My name is {0}.  I am from {2}. I am {1} years old. I have about {3}$ salary."
print(text.format(name, age, country, salary)) #My name is Abdulbosit. I am 25 years old. I am from Uzbekistan. I have about 2500$ salary.

