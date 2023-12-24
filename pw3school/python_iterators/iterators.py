# Python Iterators
# An iterator is an object that contains a countable number of values

# An iterator is an object that can be iterated upon, meaning that you can through all the values
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods
# __iter__() and __next__().


# Iterator vs Iterable
# List, Tuple, Set, Dict are all iterable objects. They are iterable containers which  you can get an iterator from
# All these objects have a iter() method which is used to get an iterator

myTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
myIterator = iter(myTuple)
print(next(myIterator))  # 1
print(next(myIterator))  # 2
print(next(myIterator))  # 3

# Even strings are iterable objects, and can return an iterator
myString = "Hello World!"
myIterator = iter(myString)
print(next(myIterator))  # H
print(next(myIterator))  # l
print(next(myIterator))  # o

# Looping through an Iterator
# We can also use a for loop to iterate through an iterable object
# Iterate the values of a tuple
myTuple = ("apple", "banana", "cherry")
for x in myTuple:
    print(x)

# Iterate the characters of a string
myString = "Hello World!"
for x in myString:
    print(x)


# The for loop actually creates an iterator object and executes the next() method for each loop

# Create an Iterator

# To create an object/class as an iterator you have to implement the __iter__ methods and __next__ methods to your object
# As you have learned in the Python Class/Objects chapter, all classes  have a function called __init__(),
# which allows you to do some initializing when the object is being created

# The __iter__() method acts similar, you can do operations (initializing, etc), but must always return the iterator
# object itself

# The __next__() method also allows you to do operations, and must return the next item in the sequence

# Create  an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4...)
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = MyNumbers()
myiter = iter(myClass)
print(next(myiter))  # 1
print(next(myiter))  # 2
print(next(myiter))  # 3


# StopIteration
# Teh example above would continue forever if you had enough next() statements, or if it was used in a for loop
# To prevent the iteration from going on forever, we can use the StopIteration statement

# In the __next__() method, we can add a terminating condition to raise an error  if the iteration is done a specified
# number of times

# Stop after 20 iteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)


