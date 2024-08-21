'''

    -- Operation
        -- Change the value of specific item by referring to it's key name
        -- Update dictionary
            -- using update()


'''

def addSpace():
    print()

print("============ Change the value of specific item by referring to it's key name ============")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
x = car.values()
print(x, ": All the values from the dictionary before updating the exsisting value")
car["modal"] = "Elantra Preferred"
x = car.values()
print(x, ": All the values from the dictionary after updating the value")
addSpace()


print("============ Update value with update function ============")
car = dict(make = "Hyndai", modal = "Elantra", year = 2024)
print(car, ": All the values from the dictionary before updating the exsisting value")
car.update({"modal": "Elantra Preferred"})
print(car, ": All the values from the dictionary after updating the value")
addSpace()