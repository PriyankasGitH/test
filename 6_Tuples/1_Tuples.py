"""

 -- Use to store multiple values

 -- Nature : Ordered , Unchangeable, indexed,  allow duplicate values

 -- Order : order will not change
 -- Unchangeable : Can't add or remove
 -- Allow duplicates

 -- written with round brackets

 -- OPerations
    -- Create a tuple
    -- Calculate length
    -- Create tuple with one item : which is a tuple & not a tuple
    -- Tuple constructor : To create a tuple

"""
def addSpace():
    print()

print("============ Creating tuple ==============")

fruits = ("apple", "banana", "cherry")
print(fruits, ": This is a tuple")
addSpace()

print("============ Calculate tuple length to know the no of items  ==============")

fruits = ("apple", "banana", "cherry")
print(len(fruits), "This is the tuple's item count")
addSpace()

print("============  Create a tuple with one item   ==============")

fruitsTuple = ("apple",)
print(type(fruitsTuple))

fruitsNotATuple = ("apple")
print(type(fruitsNotATuple))
addSpace()

print("============  Tuple items Data types   ==============")

TupleWithDiffDataTypes =(0, "xyz", False, 0.00)
print(TupleWithDiffDataTypes, "Tuple with different data types")

TupleWithSamefDataTypes = (True, False, False)
print(TupleWithSamefDataTypes, "Tuple with same data types")
addSpace()

print("============  Tuple constructor   ==============")
fruitBasket = tuple(("Apple", "Banana", "Cherry"))
print(fruitBasket, "This is a tuple created by constructor")
addSpace()

