"""
-- Use remove()

-- Use discard()

-- pop() : This removes a random item

-- clear : empties set

-- del : delete set completely

"""
def addSpace():
    print()

print("============== Removing an item from set with remove ===============")
testSet = {"Strawberry","Pineapple","Banana"}
testSet.remove("Pineapple")
print(testSet, ": After removing the item pineapple with remove")
addSpace()

print("============== Removing an item from set with discard ===============")
testSet = {"Strawberry","Pineapple","Banana"}
testSet.discard("Pineapple")
print(testSet, ": After removing the item pineapple with discard")
addSpace()

print("============== Removing an item from set with pop ===============")
testSet = {"Strawberry","Pineapple","Banana"}
testSet.pop()
print(testSet, ": After removing the item pineapple with pop - a random item")
addSpace()

print("============== Emptying a set with clear ===============")
testSet = {"Strawberry","Pineapple","Banana"}
testSet.clear()
print(testSet, ": Emptied set with clear method")
addSpace()

print("============== Delete a set c ompletely ===============")
testSet = {"Strawberry","Pineapple","Banana"}
del testSet
# print(testSet, ": set is deleted") : Throws an error
addSpace()