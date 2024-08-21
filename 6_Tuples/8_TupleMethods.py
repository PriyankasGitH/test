"""
-- Tuple methods

    -- count() : returns a number of times a specified value occurs in a tuple
    -- index() : searches the tuple for a specified value and returns the position of where it was found, returns first index of specified value

"""
def addSpace():
    print()

print("============== Count the repeated items within a tuple ==============")

my_tuple = (1,2,3,2,4)

count_2 = my_tuple.count(2)
print(count_2, ": Count of 2 within my tuple")
addSpace()

print("============== Count the specified index items within a tuple ==============")

my_tuple = (1,2,3,2,4)

index_2 = my_tuple.index(2)
print(index_2, ": first index of 2 within my tuple")
addSpace()

