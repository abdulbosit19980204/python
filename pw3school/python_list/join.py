# Join two list

# There are several ways to join , or concatenate, two or more lists in Python

# One of the easiest ways are by using the + operator.

list1 = [1,3,5,7,9]
list2 =[2,4,6,8,10]
joinedList = list1+list2
print(joinedList) #[1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

# Another way to join two list is by appending all the items from list2 into list1, one by one
list1=['a','b','c']
list2=[1,2,3]
for x in list2:
    list1.append(x)
print(list1) #['a', 'b', 'c', 1, 2, 3]

# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

list1=[11,22,33,44,55,66]
list2=[1,2,3,4,5,6]
list1.extend(list2)
print(list1) #[11, 22, 33, 44, 55, 66, 1, 2, 3, 4, 5, 6]
