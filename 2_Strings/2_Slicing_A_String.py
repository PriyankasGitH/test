"""

# Slicing - > Returns a range of characters by using the slice syntax

-- You need to provide start index & end index to get that specific part of string

-- The end idex is always excluded : in both positive & negative indexing
"""
def addSpace():
    print()

print("========== Slicing a string with only start & end index ==========")

a = "Hello World!"

print(a[2:5])
addSpace()

print("========== Slicing from the start till specified range ==========")

b = "Hello World!"
print(b[:5])
addSpace()

print("========== Slicing from the specified index till end ==========")

c = "Hello World!"
print(c[2:])
addSpace()

print("========== Slicing with negative indexing ==========")

d = "Hello World!"
print(d[-5:-2])

