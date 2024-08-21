"""

# Can't access items in a set with index so find with a loop

-- access all items
-- check if a value is present
-- can't change items but can add new items

"""
def addSpace():
    print()

print("============== Getting a value from set with for loop ===============")
testSet = {"apple", "banana", "cherry"}

for x in testSet:
    print(x)
print("All values of set with a for loop")
addSpace()


print("============== Check if value is present ===============")
testSet = {"apple", "banana", "cherry"}
print(testSet,": This is the given set")
print("banana" not in testSet, ": Checking if banana is not present in set" )
print("banana" in testSet, ": Checking if banana is present in set" )
addSpace()


