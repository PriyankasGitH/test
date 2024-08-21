"""

-- Add items
    -- By adding a new index key and assigning a value to it

-- Update dictionary
    -- update as


"""

def addSpace():
    print()

print("================  Adding an item in a dict by using a new index key ================")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
print(car, ": All the values from the dictionary before updating the exsisting value")
car["color"] = "Black"
print(car, ": All the values from the dictionary after updating the value")
addSpace()

print("============ Update value with update function ============")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
print(car, ": All the values from the dictionary before updating the exsisting value")
car.update({"modal": "Elantra Preferred"})
print(car, ": All the values from the dictionary after updating the value")
addSpace()