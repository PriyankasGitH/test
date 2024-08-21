"""
-- While loop through a tuple with
    -- len()

"""

print("========== Whilele looping through the index numbers to print tuple values with length function ==========")
testTuple = ("Apple", "Banana", "Cherry")
x = 0
while x < len(testTuple):
    print(testTuple[x])
    x = x + 1
print("Above are values of tuple printed through while loop with length function")

