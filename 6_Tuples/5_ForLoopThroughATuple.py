"""
-- Loop through a tuple with
    -- a for loop
    -- index number : range & len
    -- while loop
    --

"""

"""

Loop thorugh a for loop

"""
def addSpace():
    print()

print("========== Looping through a tuple with for loop ==========")
testTuple = ("apple","banana","cherry")
for x in testTuple:
    print(x)

print("Above are values of tuple printed through loop")
addSpace()

print("========== Looping through the index numbers to print tuple values ==========")
testTuple = ("apple","banana","cherry")
for x in range(len(testTuple)):
    print(testTuple[x])
print("Above are values of tuple printed through loop with length function")




