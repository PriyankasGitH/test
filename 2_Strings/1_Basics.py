"""

1) -- String can be printed in single and double quotes

2) -- Quotes inside quotes

3) -- Strings are arrays

4) -- Loping through a string

5) -- String length

6) -- Check string

7) -- Check if in & Not in

8 ) -- if condition with string

"""
def addSpace():
    print()

# 1) -- String can be printed in single and double quotes

print("=========== Printing strings with single & double quotes ===========")

print("Hi:", "Printed in double quotes")

print('Hello:', "Printed in single quotes")

addSpace()

print("=========== Quotes inside quotes ===========")

print("It's alright")

print("He's called 'Johnny'")

print('He is called "Johnny"')

addSpace()

print("=========== Assign String to a variable ===========")

a = "Hello"
print(a)

addSpace()

print("=========== Multiline strings ===========")
b = """lorem ipsum """
print(b)

addSpace()

print("=========== Single line strings ===========")
c = '''Lorem ipsum '''
print(b)

addSpace()

print("=========== Strings are arrays ===========")
e = "Hello world!"
print(a[0])

addSpace()

print("=========== Looping through a string ===========")
for x in 'banana':
    print(x)
print("Printed each string character with loop")

addSpace()

print("=========== String length ===========")
a = "Hello World!"
print("The length of the string is", len(a))

addSpace()

print("=========== Check String : Present & not present ===========")
text = "The best things in life are free!"
print("free" in text)

text2 = "The best things in life are free!"
print("abc" not in text2)

text3 = "The best things in life are free!"
if "abc" not in text3:
    print("No, abc is not present in the given string")



