'''

-- Use: Lists are used to store multiple items in a single variable.

--  4 built in data types to store collections of data

-- List
    -- Nature : Ordered, changeable, allows duplicate, indexed
    -- Length
    -- Contains Items with same & different data types, indexed
    -- Getting the type of the list
    -- List constructor to create a list

-- Tuple
    -- Nature : Ordered, Unchangeable, allows duplicate

-- Set
     -- Nature : Unordered, Unchangeable but can remove or add, unindexed, No duplicate

-- Dictionary
    -- Nature : ordered, changeable, unindexed, No duplicate

'''
def addSpace():
    print()


print("================ Creating a list ================")

fruits = ["apple", "banana", "cherry"]
print(fruits, ": The Fruits list contains these items")
addSpace()

print("================ Nature of lists ================")

print("-- Ordered : ")
print(
     "  -- The items have defined order & the order will not change", "\n",
     " -- new item gets added to the end of the list", "\n",
     " -- There are some exception like insert() ",
     "\n"
      )

print("-- Changeable")
print(
     "  -- We can change, add, remove items in a list", "\n",
      )
print("-- Allow Duplicate values")
print(
     "  -- WCan have items with same value", "\n",
      )


print("================ Nature of lists with e.g. ================")
fruitsBasket = ["apple", "banana", "cherry", "apple", "cherry"]
print(fruitsBasket)
addSpace()


print("================ Calculating length of list ================")

print(len(fruitsBasket), ": This is the length of the list")
addSpace()


print("================ Separate List with different data types of items ================")
listA = ["apple", "banana", "cherry", "Mango"]
listB = [0,4,5,1,0,4]
listC = [True, True, False]

print(listA, ": List of string items")
print(listB, ": List of int items")
print(listC, ": List of boolean items")
addSpace()

print("================ Single List with different data types of items ================")
listD = [0, "Hi", False , 0, "Female"]
print(listD, ": Single List with different data types")
addSpace()

print("================ Getting the type of the list ================")
print(type(listD), ": This is the list type")
addSpace()

print("================ Creating list with constructor ================")
listE = list(("Mango", "Blueberry", "Banana")) # note the double round-brackets
print(listE, "This is the list created with the constructor")
addSpace()