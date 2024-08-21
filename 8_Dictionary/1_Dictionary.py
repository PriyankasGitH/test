"""

-- Use to store data values in key value pair
-- Nature
    -- Ordered, changeable, don't allow duplicates
    -- Within curely brackets and have keys abd values
    -- Ordered :Order will not change
    -- Unordered : Don't have a defined order, you can't refer to an item by using an index
    -- Changeable : we can change, add or remove
    -- Duplicates keys are not allowed : Can't have two items with the same key
        -- Duplicate keys, the latest value will overwrite the exsisting values
    -- Duplicate values are allowed : different keys can hav same value
-- Operations
    -- Create a dictionary
    -- Duplicate keys
    -- Dictionary length : gives total count of key value pair
    -- The values can be of any data type
    -- Get the type of dictionary
    -- USing dict() constructor, create a dictionary
    --
"""
def addSpace():
    print()


#  Create a dictionary
print("================ The dictionary ================")

car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
print(car["Make"], ": is the value of the key Make")
addSpace()


print("================  The dictionary with duplicate keys  ================")

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(car, ": most recent value of the duplicate key")
addSpace()

print("================  The dictionary length   ================")

car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
print(len(car), ": This is the length of the dictionary")

print("================  The dictionary different values   ================")
car = {
  "brand": "Hyundai",
  "electric": "Elantra",
  "year": 2024,
  "colors": ["red", "white", "blue", "Black"]
}
print(car, ": Different data types values of dictionary")

print("================  Get teh type of the dictionary   ================")
car = {
  "brand": "Hyundai",
  "electric": "Elantra",
  "year": 2024,
  "colors": ["red", "white", "blue", "Black"]
}
print(type(car), ": Type of the dict")

print("================ Create the dict with dict() constructor   ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
print(car)
