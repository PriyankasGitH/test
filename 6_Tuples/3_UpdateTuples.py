"""

-- Tuples are unchangeable
    -- You can't change, add or remove item once created but there are some workarounds
    -- immutable / unchangeable

    -- Operations
        -- Convert tuple into a list & back to a tuple
        -- Add items
            -- Immutabele so don't have built-in append() : same as update, convert to list, add & convert back to tuple
        -- Add tuple to a tuple : same workaround of concerting to list
        -- Remove a tuple : same workaround of concerting to list
        -- using del keyword : delete keyword completely


"""

def addSpace():
    print()

print("=============  Updating a tuple  =============")
testTuple = ("Apple", "Mango", "Banana")
print(testTuple, "Before updating the  tuple")

testList = list(testTuple)
print(testList, "This is a list converted from tuple")

testList[1] = "Kiwi"
print(testList, "Updated item 1 to kiwi in the list")

testTuple = tuple(testList)
print(testTuple, "Converted list to tuple")
addSpace()

print("=============  Adding an item a tuple  =============")
testTuple = ("Apple", "Mango", "Banana")
print(testTuple, "Before adding an item in the tuple")
testList = list(testTuple)
testList.append("Orange")
testTuple = tuple(testList)
print(testTuple, "After adding an item in the tuple")
addSpace()

print("=============  Adding a tuple within a tuple  =============")
testTuple = ("Apple", "Mango", "Banana")
print(testTuple, "Before adding a tuple in the tuple")

addTuple = ("Orange",)
testTuple += addTuple
print(testTuple, "After adding a tuple within exsisting tuple")
addSpace()

print("=============  Remove a tuple with remove =============")
testTuple = ("Apple", "Mango", "Banana")
print(testTuple, "Before removing an item from a tuple")
testList = list(testTuple)
testList.remove("Apple")
testTuple = tuple(testList)
print(testTuple, "After removing an item in the tuple")
addSpace()

print("============= Delete a tuple =============")
testTuple = ("Apple", "Mango", "Banana")
del testTuple
# print(testTuple) : Raises an error






