"""

    -- Conditional operators
        -- equal
        -- not equal
        -- greater than & greater than equal to
        -- less than & less than equal to

    -- conditional
        -- if
        -- if .. elif
        -- if .. elif .. else
        -- if ... else
        -- Multiple else statement
        -- short hand if
        -- short hand if else
        -- And .. or .. not
        -- Nested if
        -- The pass statement


"""
def addSpace():
    print()

print("========== Printing types of conditional operators ============")
print("Equals: a == b ")
print("Equals: a != b ")
print("Equals: a < b ")
print("Equals: a <= b ")
print("Equals: a > b ")
print("Equals: a >= b ")
addSpace()

print("========== Using if ============")
a = 0
b = 1
if b > a:
    print("b is greater than a")
addSpace()

print("========== Using Elif ============")
a = 0
b = 1
if b == a:
    print("a is equal to b")
elif b > a:
    print("b is greater than a")
addSpace()

print("========== Using else ============")
a = 0
b = 1
if b < a:
    print("b is less than a")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")
addSpace()

print("========== Using if .. else ============")
a = 0
b = 1
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
addSpace()

print("========== Short Hand if ============")
a = 1
b = 0
if a > b: print("a is greater than b")
addSpace()

print("========== Short Hand if else ============")
a = 0
b = 1
print("a is greater") if a > b else print("b is greater")
addSpace()

print("========== Multiple else statements ============")
a = 0
b = 0
print("a is greater than b") if a > b else print("a is equal to b") if a == b else print("b is greater than a")
addSpace()

print("========== And ============")
a = 0
b = 1
c = 2
if a < b and c > a:
    print("Both conditions are True")
addSpace()


print("========== OR ============")
a = 0
b = 1
c = 2
if a < b or a > a:
    print("One of the condition is True")
addSpace()

print("========== Not ============")
a = 0
b = 1
if not a > b:
    print("a is not greater than b")
addSpace()

print("========== Nested If ============")
a = 40
if a > 10:
    print("Above ten")
    if a > 20:
        print("Also above 20")
    else:
        print("But not above 50")
addSpace()

print("========== Pass ============")
a = 0
b = 1
if b > a:
   pass
print("Above if clause has a pass keyword")
addSpace()