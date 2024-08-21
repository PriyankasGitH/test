"""

-- Unpack a tuple

    Packing : When we create a tuple & assign values to it, it's called as packing

    Unpacking : Extracting values back into variables is called unpacking


"""
def addSpace():
    print()

print("==============  Unpacking a tuple with exact variables as values  =============")
fruits = ("Apple", "Banana", "Cherry")

(item1, item2, item3) = fruits

print(item1, "Unpacked first item of tuple")
print(item2, "Unpacked second item of tuple")
print(item3, "Unpacked third item of tuple")
addSpace()

print("==============  Unpacking a tuple with asterisks for the last variable  =============")
fruits = ("Apple", "Banana", "Cherry")

(item1, item2, *itemall) = fruits

print(item1, ": Unpacked first item of tuple")
print(item2, ": Unpacked second item of tuple")
print(itemall, ": Unpacked all items of tuple")
addSpace()

print("==============  Unpacking a tuple with asterisks for the middle variable  =============")

fruits = ("Apple", "Banana", "Cherry")

(item1, *item2, item3) = fruits

print(item1, ": Unpacked first item of tuple")
print(item2, ": Unpacked second item of tuple")
print(item3, ": Unpacked all items of tuple")
addSpace()
