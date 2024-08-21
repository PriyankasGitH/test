"""

-- A dictionary within a dictionary

    -- ways
        -- create 3 dictionaries within a dictionary
        -- create 3 dictionaries & added them as kes within a dictionary

    -- Access items in nested dictionaries

"""

def addSpace():
    print()

print("================== create 3 dictionaries within a dictionary ==================")
fruits = {

   "Fruit1" : {
       "name" : "Apple",
       "Color" : "red"
   },

    "Fruit2" : {
       "name" : "Banana",
       "Color" : "Yellow"
   },

    "Fruit3" : {
       "name" : "Pear",
       "Color" : "Green"
   }

}
print(fruits, ": These are nested dictionaries")
addSpace()

print("================== create 3 dictionaries separately & add them as keys within a dictionary ==================")


Fruit1 = {
    "name" : "Apple",
    "Color" : "red"
   }

Fruit2 = {
    "name" : "Banana",
    "Color" : "Yellow"
   }

Fruit3 = {
    "name" : "Pear",
    "Color" : "Green"
   }

fruits = {
    "Fruit1": Fruit1,
    "Fruit2": Fruit2,
    "Fruit3": Fruit3
}
print(fruits, ": These are nested dictionaries")
addSpace()


print("================== Access items in Nested dictionaries ==================")


Fruit1 = {
    "name" : "Apple",
    "Color" : "red"
   }

Fruit2 = {
    "name" : "Banana",
    "Color" : "Yellow"
   }

Fruit3 = {
    "name" : "Pear",
    "Color" : "Green"
   }

fruits = {
    "Fruit1": Fruit1,
    "Fruit2": Fruit2,
    "Fruit3": Fruit3
}
print(fruits["Fruit1"]["name"], ": First dictionarie's first key")
print(fruits["Fruit2"]["name"], ": Second dictionarie's first key")
print(fruits["Fruit3"]["name"], ": Third dictionarie's first key")
addSpace()