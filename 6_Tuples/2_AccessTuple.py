"""

-- Access a tuple: By referring to index number
    -- Positive + Negative index

-- Accessing tuple items within range
    -- with start & end index
    -- with end index only
    -- with start index only
    -- range of negative index
    -- check if item exsit


"""
def addSpace():
    print()

print("===========  accessing the tuple with positive index  ===========")
fruits = ("apple", "banana", "cherry")
print(fruits[1], ": Accessing second item of the tuple")
addSpace()

print("===========  accessing the tuple with negative index  ===========")
fruits = ("apple", "banana", "cherry")
print(fruits[-1], ": Accessing first item of the tuple")
addSpace()

print("===========  accessing the items of tuples within range of specified index  ===========")
fruits = ("apple", "banana", "cherry", "Pear", "Strawberry", "Peach")
print(fruits[2:5], ": Accessing items from 2 to 4")
addSpace()

print("===========  accessing the items from the begining till specified index  ===========")
fruits = ("apple", "banana", "cherry", "Pear", "Strawberry", "Peach")
print(fruits[:4], ": Accessing items from start till 3rd item")
addSpace()

print("===========  accessing the items from the begining till specified index  ===========")
fruits = ("apple", "banana", "cherry", "Pear", "Strawberry", "Peach")
print(fruits[2:], ": Accessing items from 2nd index till last item")
addSpace()

print("===========  accessing the items from the range of negative index  ===========")
fruits = ("apple", "banana", "cherry", "Pear", "Strawberry", "Peach")
print(fruits[-4:-1], ": Accessing items from -4 till -2")
addSpace()

print("===========  accessingif the items exsit in the tuple  ===========")
fruits = ("apple", "banana", "cherry", "Pear", "Strawberry", "Peach")
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits tuple")





