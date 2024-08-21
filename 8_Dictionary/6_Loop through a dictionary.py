"""

-- Loop through a
    -- for loop
            -- Keys
              -- Looping gives keys
              -- Print keys with keys()

            -- Values
                -- To get the values, need to use specific methods
                -- Print values one by one with for loop
                -- Print values one by one with for values()

            -- Both keys and values
                -- Using items()


"""
def addSpace():
    print()

print("================ Loop through a dictionary ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
for x in car:
    print(x)
print("Above are Keys from dictionary with a for loop")
addSpace()

print("================ Print values one by one with for loop ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
for x in car:
    print(car[x])
print("Above are values from dictionary with a for loop")
addSpace()


print("================ Print values one by one with values() ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
for x in car.values():
    print(x)
print("Above are values from dictionary with a for loop with values()")
addSpace()

print("================ Print values one by one with keys() ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
for x in car.keys():
    print(x)
print("Above are keys from dictionary with a for loop with keys()")
addSpace()

print("================ Print keys & values one by one with items() ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
for x,y in car.items():
    print(x,y)
print("Above are keys & values from dictionary with a for loop with items()")
addSpace()