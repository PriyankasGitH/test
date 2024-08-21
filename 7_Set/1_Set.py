"""

# Print a set:
    -- Unordered, unchangeable, don't allow duplicates, unordered
    -- Duplicate values are ignored
    -- True and 1 are same values : whichever is first gets precedence
    -- False and 0 are same values : whichever is first gets precedence
    -- Get length
    -- Data types
    -- Finding the type of set
    -- Using set() constructor to create a set


"""

def addSpace():
    print()

print("============== Printing set ==============")
myset = {"apple", "banana", "cherry"}
print(myset, ": This is a set")
addSpace()

print("============== Duplicate values are ignored ==============")
testSet = {"apple", "banana", "cherry", "apple"}
print(testSet, ": This is a set")
addSpace()

print("============== True and 1 are same values ==============")
testSet1 = {"apple", "banana", 1, True, "cherry", 1}
testSet2 = {"apple", "banana", True, "cherry", 1}
print(testSet1, ": This is a set with 1 preceeding True")
print(testSet2, ": This is a set with True preceeding 1")
addSpace()

print("============== True and 1 are same values ==============")
testSet1 = {"apple", "banana", 0, False, "cherry", 1}
testSet2 = {"apple", "banana", False, "cherry", 0}
print(testSet1, ": This is a set with 0 preceeding False")
print(testSet2, ": This is a set with False preceeding 0")
addSpace()

print("============== Get Length of set ==============")
testSet = {"apple", "banana", 0, False, "cherry", 1}
print(len(testSet), ": Length of Tuple")
addSpace()

print("============== Same Data types set : separate ==============")
testSet1 = {"apple", "banana", "cherry" }
testSet2 = {1,5,7,9,3}
testSet3 = {True, False}
print(testSet1, ": Data set of string")
print(testSet2, ": Data set of int")
print(testSet3, ": Data set of boolean")
addSpace()

print("============== Different Data types within a set ==============")
testSet = {"abc", 0, 5.5, False, 1+1j}
print(testSet, ": Data set of different types within a set")
addSpace()

print("============== Getting type of set ==============")
myset = {"Mango","Apple","Banana"}
print(type(myset), ": DataType of given set")
addSpace()

print("============== Using set() constructor to create a set ==============")
testSet =set( ( "Mango", "Apple", "Banana" ) )
print(testSet, ": Set created using constructor")
addSpace()
