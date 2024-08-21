"""
1. Make Strings upper case

2. Make Strings lower case

3. Remove whitespace

4. Replace Strings

5. Split String

"""

def addSpace():
    print()

# 1. Make Strings upper case

print("============== Make Strings upper case ==============")
a = "Hello World!"
print(a.upper())
addSpace()

# 2. Make Strings lower case
print("============== Make Strings lower case ==============")
b = "Hello World!"
print(a.lower())
addSpace()

# 3. Remove whitespace
print("============== Remove whitespace ==============")
c = "Hello World! "
print(c.strip())
addSpace()

# 4. Replace Strings
print("============== Replace Strings ==============")
d = "Hello, World!"
print(a.replace("H", "d"))
addSpace()

# 5. Split String
print("============== Split String ==============")
e = "Hello, World! Welcome To Python"
print(e.split())
addSpace()