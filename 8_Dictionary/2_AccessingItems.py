"""

-- You can access the items of a dictionary by refering to it's key name inside square brackets
-- Operations
    -- Values
        -- Get the values of the keys with index
        -- Get the values of the keys with get()

    -- Keys
        -- Get the keys in the dictionary : will return list of the keys in the dictionary
            --  List of keys is a view of the dictionary, any changes made to the dictionary will be reflected in the keys list

    -- Values
        -- Get all the values from the llst

    -- Add a key value pair
        -- check for added key
        -- check for added value

    -- Change an exsisting value
        -- check for the updated value

    -- get all items as tuple in dictionary
        -- see all the items
        -- make a change & see it reflected as item

    -- in keyword
        -- check if the specific key exist



"""

def addSpace():
    print()

# Access the items
print("================  Using index Get the value of the key of the dictionary   ================")

car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car["make"]
y = car["modal"]
z = car["year"]
print(x, ": This is the value of the first key in the dictionary")
print(y, ": This is the value of the second key in the dictionary")
print(z, ": This is the value of the third key in the dictionary")
addSpace()

print("================  Using get(), Get the value of the key of the dictionary   ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.get("make")
y = car.get("modal")
z =car.get("year")
print(x, ": This is the value of the first key in the dictionary")
print(y, ": This is the value of the second key in the dictionary")
print(z, ": This is the value of the third key in the dictionary")
addSpace()

print("================  Get keys only   ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.keys()
print(x, ": All the keys from the dictionary")
addSpace()

print("================  Add a key value pair & check for keys  ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.keys()
print(x, ": All the keys from the dictionary before adding a new key")
car["color"] = "Black"
x = car.keys()
print(x, ": All the keys from the dictionary after adding a new key")
addSpace()

print("================  Add a key value pair & check for values  ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.values()
print(x, ": All the values from the dictionary before adding a new key")
car["color"] = "Black"
x = car.values()
print(x, ": All the values from the dictionary after adding a new key")
addSpace()

print("================  Update an exsisting key & check for updated value  ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.values()
print(x, ": All the values from the dictionary before updating the exsisting value")
car["modal"] = "Elantra Preferred"
x = car.values()
print(x, ": All the values from the dictionary after updating the value")
addSpace()

print("================  Get each item in dictionary as a tuple  ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.items()
print(x, ": Get each item in dictionary as a tuple")
addSpace()

print("================  Update each item in dictionary as a tuple & see the change within the tuple ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.items()
print(x, ": Get each item in dictionary as a tuple before updating")
car["color"] = "Black"
print(x, ": Get each item in dictionary as a tuple after updating")
addSpace()

print("================ Check if specific key exsist with in keyword ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
if "make" in car:
    print("Yes, make is one of the keys in the dictionary")
addSpace()