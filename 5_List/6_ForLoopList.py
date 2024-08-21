"""

-- You can loop within a list with

    -- for loop
    -- while loop
    -- List comprehension

    -- for loop
        --  USe range() & len() functions to create a suitable iterable

    -- while loop
        -- len()

    -- List comprehension

-- Get the index number of the list

"""

# Loop

def addSpace():
    print()

print("========= Iterating in the list with for loop by referring to items =========")

fruits = ["Apple","Banana","Cherry"]
print("For loop : Printing the items in the list ")
for x in fruits:
    print("--",x)

print("========= Iterating in the list with for loop by referring to index number =========")
print("For loop : Printing items in the list with length function")
for x in range(len(fruits)):
    print("--",fruits[x])