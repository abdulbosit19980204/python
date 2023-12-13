# Sort  List

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default

# Sort the list alphabetically
thisSortList = ["olma","behi","apple","mandarin","gilos"]
thisSortList.sort()
print(thisSortList) #['apple', 'behi', 'gilos', 'mandarin', 'olma']

# Sort the list numerically
numList = [1,5,7,0,11,9,22,2,4]
numList.sort()
print(numList) #[0, 1, 2, 4, 5, 7, 9, 11, 22]

# Sort descending
# To sort descending, use the keyword argument "reverse=True"
numList.sort(reverse=True)
print(numList) #[22, 11, 9, 7, 5, 4, 2, 1, 0]

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function
# The funnction will return a number that will be used to sort the lsit (the lowest number first)
# Sort the list based on how close the number is to 50
def myFunc(n):
    return abs(n-50)
thisList = [1,50,11,25,144,22]
thisList.sort(key=myFunc)
print(thisList) #[50, 25, 22, 11, 1, 144]

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
thisSensetiveList = ["Abhadshb","sndjs","ajsnjdas ","iuwjndqwijn","Nnsjdnaoi"]
thisSensetiveList.sort()
print(thisSensetiveList) #['Abhadshb', 'Nnsjdnaoi', 'ajsnjdas ', 'iuwjndqwijn', 'sndjs']

# Luckily we can use built-in functions as key functions when sorting a list
# So if you want a case-insensitive sort function, use str.lower as a key fuction
thisInsensitiveList=["asnnbd","sjad","Andsjnjk","SSJDNJ","ndwinduiqnwiu"]
thisInsensitiveList.sort(key=str.lower)
print(thisInsensitiveList) #['Andsjnjk', 'asnnbd', 'ndwinduiqnwiu', 'sjad', 'SSJDNJ']

#REVERSE ORDER
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.
thisReverseList = [11,545,212,848,21,11,848,22,44]
# thisReverseList.reverse()
# print(thisReverseList) #[44, 22, 848, 11, 21, 848, 212, 545, 11]
thisReverseList.sort()
thisReverseList.reverse()
print(thisReverseList) #[848, 848, 545, 212, 44, 22, 21, 11, 11]
