"""

1. Boolean values : True and False, to evaluate an expression and get the answers

2. Evaluate values and variables

3. Most values are True

4. Some values are False

5. Functions can return aBoolean

"""

def addSpace():
    print()

# 1. Boolean values : True and False, to evaluate an expression

# The expression is evaluated when you compare two values
print("=============== Evaluating expression as Tre or False ===============")
print(0 > 1)
print(0 == 1)
print(0 < 1)
addSpace()

#2. Evaluate values and variables

print("=============== Evaluating expression with bool function ===============")
print(bool("Hello"))
print(bool(15))
addSpace()

print("===== bool() returns False for empty sequences and collections, zero values, and None =====")
print(bool(""))       # Empty string
print(bool(0))        # Zero integer
print(bool(0.0))      # Zero float
print(bool([]))       # Empty list
print(bool(()))       # Empty tuple
print(bool({}))       # Empty dictionary
print(bool(set()))    # Empty set
print(bool(None))     # None
addSpace()

print("=============== Object of a class that returns length as zero ===============")
'''
The bool() function relies on the __len__() method to determine the truthiness of an object. 
Since myclass's __len__() method returns 0, the instance myobj is considered "falsy", and thus bool(myobj) returns False.
'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
addSpace()

print("=============== Function can return a Boolean ===============")
def myFunction() :
  return True

print(myFunction())
addSpace()

print("=============== Execute code based on the boolean answer ===============")
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

