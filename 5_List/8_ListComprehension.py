"""

Looping Using list comprehension



"""
def addSpace():
    print()

print("=========== Printing list items with list comprehension ===========")

fruits = ["apple", "banana", "Kiwi"]
[print(i) for i in fruits ]
addSpace()

"""

List comprehension offers a shorter syntax when you want to create a new list

newlist = [expression for item in iterable if condition == True]

"""
print("=========== Creating a new list with for loop ===========")

fruitsBasket = ["apple", "banana", "Kiwi","Cherry"]
newList1 = []

for x in fruitsBasket:
    if "a" in x:
        newList1.append(x)

print(newList1, ": New list Created with for loop")
addSpace()

print("=========== Creating a new list with list comprehension ===========")

fruitsBasket = ["apple", "banana", "Kiwi","Cherry"]

newList2 = [x for x in fruitsBasket if "a" in x]
newList3 = [x for x in fruitsBasket if x != "apple"]
newList4 = [x for x in fruitsBasket]
newList5 = [x.upper() for x in fruitsBasket]
newList6 = ['Hello' for x in fruitsBasket]
newlist7 = [x if x != "banana" else "orange" for x in fruits] #Return the item if it is not banana, if it is banana return orange

print(newList2, ": New list Created with list comprehension")
print(newList3, ": New list Created with list comprehension")
print(newList4, ": New list Created with list comprehension")
print(newList5, ": New list Created with list comprehension")
print(newList6, ": New list Created with list comprehension")
print(newlist7, ": New list Created with list comprehension")
addSpace()

print("=========== Creating a new list with list comprehension & range function ===========")
newList8 = [x for x in range(3)]
print(newList8, ": New list Created with list comprehension")
addSpace()

newList9 = [x for x in range(7) if x < 4]
print(newList9, ": New list Created with list comprehension")
addSpace()