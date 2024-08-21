"""

Use to compare objects not to check if they're equal but to check if they're same objects

"""

print("=========== Identity Operator ===========")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z, ":comparing using is operator") # returns True because z is the same object as x
print(x is y, ":comparing using is operator") # returns False because x is not the same object as y, even if they have the same content
print(x == y, ":comparing using == operator") # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y