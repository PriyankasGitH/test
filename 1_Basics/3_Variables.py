"""

-- Variable is a container / memory location to hold a value

-- There is no command to declare a variable

-- When you assign a value to it, the variable is created

-- Variables are storing values of different data types

"""

def addSpace():
    divider = "============="
    print()
    print(divider)
print("======== Understanding Variables ========")



x = 5
y = "Hello world"

print(x)
print(y)
addSpace()

"""

-- Operations to be performed on variables

1. Create a variable and assign a value to it, output the variables 

2. Changing the type after variable is declared and created

3. Type casting : specifying data type

4. Getting the type

5. Single or double quotes : String variables can be declared with single or double quotes

6. Case sensitive : lower and upper case will be treated different

7. Variables with more than one word : Camel case, Pascal case , Snake case

8. Assign multiple values to multiple variables

9. Assign 1 value to multiple variables

10. Unpacking from collection

11. Output values which are: Single, multiple using comma & concatination 

-- Comma ( most prefered as support different data types )

-- Concatination for integers

--  Concatination for strings

12. Global variables & golabl keyword

Global variables:
-- Created outside the function 
-- Can be used by everyone by both inside and outside of the function

Global keyword:
-- When a variable is created inside a function, it's called a local variable
-- To create a global variable inside a function, use global keyword

"""

print("======== Performing operations on Variables ========")

# 1. Create a variable and assign a value to it

a = 0
print(x)
addSpace()


# 2. Changing the type after variable is declared and created

b = 0
b = "Hello there"
print(b)
addSpace()


# 3. Type casting

c = str(3)
print(c)

d = int(3)
print(d)

e = float(3)
print(e)

addSpace()
# 4. Getting the type

f = 5
print(type(f))

g = "Hello"
print(type(g))

addSpace()

# 5. Single or double quotes

# String variables can be declared with single or double quotes

h = 'Hi there'
print(h)

i = "Hello there"
print(i)

addSpace()
# 6. Case sensitive

j = 4
J = "Sally"
print(j, "lowercase sensitive letter")
print(J, "Uppercase sensitive letter")
print("===========")
# 7. Variables with more than one word : Camel case, Pascal case , Snake case

# Camel case : Each word starts with upper case except the first

myVarName = "John"
print("Above word is in Camel case ")

# Pascal case : Each word starts with capital letter

MyVarName = "John"
print("Above word is in Pascal case ")

# Snake case : Each word is separated by underscore

my_var_name = "John"
print("Above word is in snake case ")

# 8. Assign multiple values to multiple variables
print("===========  Assign multiple values to multiple variables ==============")
k, l,  m = "Orange", "Banana", "Cherry"
print(k)
print(l)
print(m)


# 9. Assign 1 values to multiple variables
print("===========  Assign 1 values to multiple variables ==============")
k = l = m = "Orange"
print(k)
print(l)
print(m)


# 10. Unpacking from collection
print("===========  Unpacking from collection ==============")
fruits = ["Apple", "Banana", "Cherry"]
n, o, p = fruits
print(n)
print(o)
print(p)

addSpace()
'''
11. Output values which are: Single, multiple using comma & concatination 

-- Comma ( most prefered as support different data types )

-- Concatination for integers

--  Concatination for strings
'''

# Single variable
q = 0
print(q)

# Using comma separator for int & string
r="Hello"
print(q,r)
print("Using comma separator for int & string")

# Concatination for integers
s = 0
print(q+s)
print("Using Concatination for integers")

# Concatination for integers
t="There"
print(r+" "+t)
print("Using Concatination for integers with space")
addSpace()

"""
12. Global variables 

-- Created outside the function 
-- Can be used by everyone by both inside and outside of the function

"""

u="Awesome"

def testFunc():
    print("we are printing a global variable within a function:", u)

testFunc()


"""
Global keyword:
-- When a variable is created inside a function, it's called a local variable
-- To create a global variable inside a function, use global keyword

"""

def testFunc2():
    global v
    v = "Great"

testFunc2()
print("The global variable declared inside a function is:", v )
addSpace()