"""

-- Join two lists by

    -- Concatinate
    -- append()
    -- extend()

"""
def addSpace():
    print()


print("=============   Join lists with concatinate  ============")
fruits = ["Apple", "Banana", "Cherry"]
numbers = [0,1,2]

concatinated_list = fruits + numbers
print(concatinated_list, ": List made with concatination")
addSpace()


print("=============  Append one list onto other  ============")
list1 = ["Blueberry", "Pear", "Raspberry"]
list2 = [0, 1, 2]

for x in list2:
    list1.append(x)
print(list1, ": The appended list ")
addSpace()

print("=============  Extend one list onto other  ============")
day = ["Morning", "Evening", "Nigh"]
time = [7,12,8]

day.extend(time)
print(day, ": The extended list")
addSpace()