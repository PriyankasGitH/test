"""

--- Remove / Pop
    -- Specified item with remove
    -- First occurance of duplicate item
    -- Specified index with pop : with & without index
    -- Using del keyword : specified index
    -- Using del keyword : entire list
    -- clear method to empty list

"""


def addSpace():
    print()

print("=================   Remove item at specified index  ==============")

fruits = ["Apple", "Banana", "Cherry"]
fruits.remove("Banana")
print(fruits, ": List after a specific item removed")
addSpace()

print("=================   Remove first occurance of the item with remove()  ==============")

fruits = ["Apple", "Banana", "Cherry", "Banana"]
fruits.remove("Banana")
print(fruits, ": List after first occurance of banana is removed")
addSpace()

print("=================   Remove specified item with index with pop()  ==============")

fruits = ["Apple", "Banana", "Cherry", "Banana"]
fruits.pop(1)
print(fruits, ": List after first item removed with pop")
addSpace()

print("=================   Remove specified item without index with pop()  ==============")

fruits = ["Apple", "Banana", "Cherry", "Banana"]
fruits.pop()
print(fruits, ": List after last occurance item removed with pop without index ")
addSpace()

print("=================   Remove specified item without index with del keyword  ==============")

fruits = ["Apple", "Banana", "Cherry", "Banana"]
del fruits[0]
print(fruits, ": List after first item removedwith index with del keyword")
addSpace()

print("=================   Remove entire list with del keyword  ==============")

fruits = ["Apple", "Banana", "Cherry", "Banana"]
del fruits
#print(fruits, ": entire list deleted with del keyword")    # Raises an error
addSpace()

print("=================   Remove entire list with clear()  ==============")

fruits = ["Apple", "Banana", "Cherry", "Banana"]
fruits.clear()
print(fruits, ": entire list deleted with clear()")
addSpace()
