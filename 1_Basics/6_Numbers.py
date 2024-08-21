'''

3 Numeric Types

-- int

-- float

-- complex

1. Define & print all types of variables

2. Define the type of the variables

3. Type conversion

-- int to float
-- float to int
-- int to complex

4. Random

'''

print("========== Printing all types of numeric variables ==========")

x=0
y=0.0
z=1+1j

print(x,y,z)

print("========== Converting one type to another ==========")

a = 1
b = 2.8
c = 1.0+1.0j

print("Converting int 1 to float: ", float(a))
print("Converting float 2.8 to int: ", float(b))
print("Converting complex 1j to int: ", int(c.real))

# Get the magnitude of the complex number and convert it to an integer
magnitude = abs(c)
print("Converting complex 1j to int: ", int(magnitude))



