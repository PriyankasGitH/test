"""

-- Cant copy list2 == List1 , it will only be reference to the list
-- In above example, changes made in list1 automatically also be made in list2

-- To copy use built in
    -- copy()
    -- list()

"""

def addSpace():
    print()

print("=============   Copying a list with copy() ============")
fruits = ["Apple", "Banana", "Cherry"]
copied_fruits = fruits.copy()
print(copied_fruits, ": List copied from fruits with copy()")
addSpace()

print("=============   Copying a list with list() ============")
fruitsBasket = ["Apple", "Banana", "Cherry", "Mango", "Peach"]
copied_fruitsBasket = list(fruitsBasket)
print(copied_fruitsBasket, ": List copied from fruits with copy()")
