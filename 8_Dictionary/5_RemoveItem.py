"""

-- Remove item with
    -- pop()
        --- with key
    -- popitem()
        -- removes the last inserted item
    -- del keyword
        -- removes the item with specified key name
        -- deletes entire dictionary
    -- clear()
        -- empties the dictionary


"""

def addSpace():
    print()


print("================ Removing an item with Pop using key ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
print(car, ": Before pop")
car.pop("Model")
print(car, ": After pop")
addSpace()


print("================ Removing an item with Pop item using key ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
print(car, ": Before pop item")
car.popitem()
print(car, ": After pop item")
addSpace()

print("================ Removing an item with del keyword using specified key name ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
print(car, ": Before del keyword for specified index")
del car["Model"]
print(car, ": After del keyword for specified index")
addSpace()

print("================ Deleting an entire dictionary ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
print(car, ": Before del keyword for specified index")
del car
#print(car, ": After del keyword for specified index") # Throws error
addSpace()

print("================ Empties an entire dictionary ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
print(car, ": Before empting a dict")
car.clear()
print(car, ": After empting a dict")
addSpace()