#Variables can store data of different types, and different types can do different things

# By default

# Text type: str
# Numeric Types: int, float, complex
# Sequance Types: list, tuple, range
# Mapping Types: dict
# Set Types: set, frozenest
# Boolean Types: bool
# Binary Types: bytes, bytearray, memoryview
# None Type: NoneType


# Getting data type:

# We can get data type of any object by using type() function:4

x=5
y="Hello"
print(type(x)) #<class 'int'>
print(type(y)) #<class 'str'>

# Setting the Data Type

# In Python, the data type is set when you assign a value to a variable

a = "Hello world" # Here seted a str type
z = 5 # And this is a int type

# We can test some unpublic types here

# Complex

x = 1j
print(type(x)) #<class 'complex'>
print(x) #1j


# Range
x=range(6)
print(type(x))
print(x) #range(0, 6)

# Frozenset
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
print(x) #frozenset({'cherry', 'banana', 'apple'})

# Bytes
x = b"Hello"
print(type(x))
print(x) #b'Hello'

# bytearray
x = bytearray(5)
print(type(x))
print(x) #bytearray(b'\x00\x00\x00\x00\x00')

# Memoryview
x = memoryview(bytes(5))
print(type(x))
print(x) #<memory at 0x0000024544C64880>





