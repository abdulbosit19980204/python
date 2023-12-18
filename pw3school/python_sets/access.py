# Access Set Items

# You cannot access items in a set by referring to  an index or a key
# But you can loop through  the set items using a for loop, or ask if a  specified value is present in a set, by using
# the in keyword

thisLoopSet = {"apple", "banana", "cherry","cherry"}

for x in thisLoopSet:
    print(x, end=" ") #banana apple cherry


# Check if "banana" is present in the set
print("banana" in thisLoopSet) #True

# Change Items
# Once a set is created, you cannot change its items, but you can add new items