"""

--- Join Two tuples

    -- Using concatination operator
    -- Using * operator


"""
def addSpace():
    print()

print("========== Joining Two Tuples using + operator ==========")

testTuple1 = ("a", "b", "c")
print(testTuple1, ": This is tuple1")
testTuple2 = (1, 2, 3)
print(testTuple2, ": This is tuple2")

testTuple3 = testTuple1 + testTuple2
print(testTuple3, ": Tuple created after concatinating 2 tuples")
addSpace()

print("========== Multiply Tuples ==========")
testTupleFruites = ("Apple", "Banana", "Cherry")
print(testTupleFruites, ": Printing tuple before multiplication")
myTuple = testTupleFruites * 2
print(myTuple, ": Printing tuple after multiplication")




