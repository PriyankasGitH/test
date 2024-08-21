"""

-- Add an item as can't change an item
-- Add one set to another set
-- Add another iterable into set

"""

def addSpace():
    print()

print("============== Add an item in a set ===============")
testSet = {"apple", "banana", "cherry"}
print(testSet, ": Set before adding the value")
testSet.add("Pear")
print(testSet, ": Set after adding the value")
addSpace()

print("============== Add one set into another set ===============")
testSet = {"apple", "banana", "cherry"}
tropicalSet = {"pineapple", "mango", "papaya"}

testSet.update(tropicalSet)
print(testSet, ": Adding one set into another set")
addSpace()

print("============== Add any iterable set ===============")
testSet = {"apple", "banana", "cherry"}
myList = ["kiwi","orange"]
testSet.update(myList)
print(testSet, ": Set created by adding list into set")