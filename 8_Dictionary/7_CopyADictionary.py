"""

-- Copy a dictionary
    -- YOu can't just copy one dictionary to other by dict2 = dict1
        -- It will be a reference to dict1 & changes made in dict1 will automatically alsp be made in dict2

    -- ways to copy
        -- With copy()

        -- Use built in method dict()


"""
def addSpace():
    print()

print("================ Copy a dictionary with copy() ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
car_copy1 = car.copy()
print(car, ": Copied dictionary with copy()")
addSpace()


print("================ Copy a dictionary with dict() ================")
car = {
    "Make": "Hyndai",
    "Model": "Elantra",
    "year":"2024"
}
car_copy2 = dict(car)
print(car_copy2, ": Copied dictionary with dict()")
addSpace()