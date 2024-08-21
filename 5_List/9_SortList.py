"""

-- Sort Alphanumerically by default ascending : String list, int list

-- Sort Descending

-- Customize sort function

-- Case Insensitive Sort : can give an unexpected result [ can make case sensitive ]

-- Reverse Order

"""

def addSpace():
    print()

"""
-- Sort Alphanumerically

-- Sort() method sorts the list alphanumerically ascending by default

"""
print("============= Sorting String list with sort function alphanumerically =============")
fruits = ["Apple", "Mango", "Kiwi", "Pineapple", "Banana"]
print(fruits, ": String List before sorting")
fruits.sort()
print(fruits, ": String List after sorting with sort function")
addSpace()

print("============= Sorting int list with sort function alphanumerically =============")
Numbers = [0,4, 55, 78, 45]
print(Numbers, ": Number List before sorting")
Numbers.sort()
print(Numbers, ": Number List after sorting")
addSpace()

print("============= Sorting string list with sort function alphanumerically in desc =============")
fruits = ["Apple", "Mango", "Kiwi", "Pineapple", "Banana"]
print(fruits, ": String List before sorting")
fruits.sort(reverse=True)
print(fruits, ": String List after sorting in desc")
addSpace()

print("============= Sorting int list with sort function alphanumerically in desc =============")
Numbers = [0,4, 55, 78, 45]
print(Numbers, ": Number List before sorting")
Numbers.sort(reverse=True)
print(Numbers, ": Number List after sorting in desc")
addSpace()

print("============= Customize sort function =============")
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist, ": Sortd with key argument")
addSpace()

print("============= Case Insensitive sort =============")
FruitsToBuy = ["Apple", "Orange", "Kiwi", "cherry", "Banana"]
FruitsToBuy.sort()
print(FruitsToBuy, ": Case Insensitive sorted list")
addSpace()

print("============= Case sensitive sort =============")
FruitsOnShelf = ["Apple", "Orange", "Kiwi", "cherry", "Banana"]
FruitsOnShelf.sort(key = str.lower)
print(FruitsOnShelf, ": Case sensitive sorted list")
addSpace()

print("============= Reverse order =============")
FruitsOnShelf = ["Apple", "Orange", "Kiwi", "cherry", "Banana"]
FruitsOnShelf.reverse()
print(FruitsOnShelf, ": Reverse order sorted list")
addSpace()