"""

-- We can also use a for loop to iterate through an iterable object

-- The for loop actually creates an iterator object and executes the next() method for each loop.

"""
print("========= Iterating the values of a tuple ===========")
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)