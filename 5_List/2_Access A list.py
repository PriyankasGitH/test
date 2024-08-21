"""

-- Access a list item with it's index numbers

-- The first index is zero
-- The last index is -1
-- 3 indexes to consider : Start, End, Step
-- When you don't mention start & edn index we consider it all

-- Locating item
    -- Exclude the last index
    -- Positive index
    -- Negative index
    -- Within a range

-- Negative indexing starts with -1 from right to left


"""

def addSpace():
    print()

print(" =============== Locating item from a list with Positive index =============== ")

fruits = ["Mango","Strawberry","Raspberry"]
print(fruits[1], ": This is the second item in the list")
addSpace()

print(" =============== Locating item from a list with negative index =============== ")

print(fruits[-1], ": This is the last item in the list")
addSpace()

print(" =============== Locating item from a list within a range =============== ")

fruitsBasket = ["Mango","Strawberry","Raspberry","Banana","Kiwi"]
print(fruitsBasket[2:5], ": Items starting from 2nd till 4th position")
addSpace()

print(" =============== Locating item from start till a specified index =============== ")
print(fruitsBasket[:4], ": Items starting from start till 3rd position")
addSpace()

print(" =============== Locating item from a specified index till end =============== ")
print(fruitsBasket[2:], ": Items starting from 2nd till last position")
addSpace()


print(" =============== Locating item with range of negative indexes =============== ")
print(fruitsBasket[-4:-1], ": Items starting from -4 till 2nd last position")
addSpace()

print(" =============== Check if item exsist =============== ")
if "Strawberry" in fruitsBasket:
    print("Yes strawberry is present in fruitsBasket list")
addSpace()
