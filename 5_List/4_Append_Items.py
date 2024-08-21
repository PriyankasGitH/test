"""

-- Add List items
    -- append()
    -- insert()
    -- extend()
    -- add any iterable : List, tuple, sets, dictionaries

"""

def addSpace():
    print()

print("=================   Add items with append method  ==============")
fruits = ["Apple", "Banana", "Mango"]
fruits.append("Orange")
print(fruits, ": Items added with append method")
addSpace()

print("=================   Add items with insert method   ==============")
fruits.insert(1, "Kiwi")
print(fruits, ": Items added with insert method")
addSpace()

print("=================   Add items from another list   ==============")
fruitsBasket1=["Cherry","Apple","Peach"]
fruitsBasket2=["Guava","Pineapple","Cherry"]
fruitsBasket1.extend(fruitsBasket2)
print(fruitsBasket1)
addSpace()

print("=================   Add items from another list   ==============")
fruitsBasket1=["Cherry","Apple","Peach"]
fruitsBasket2=["Guava","Pineapple","Cherry"]
fruitsBasket1.extend(fruitsBasket2)
print(fruitsBasket1)
addSpace()

print("=================   Add items from any other iterable : tuple   ==============")
thisList =["Cherry","Apple","Peach"]
thisTuple =["Guava","Pineapple"]
fruitsBasket1.extend(thisTuple)
print(fruitsBasket1)