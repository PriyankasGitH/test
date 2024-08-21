
# Membership operators are used to test if a sequence is presented in an object

def addSpace():
    print()

print("============= in operator =============")
x = ["apple", "banana"]
print("banana" in x, ": Element is present in sequence")
addSpace()

print("============= not in operator =============")
x = ["apple", "banana"]
print("pineapple" not in x, ": Element is not present in sequence")
addSpace()