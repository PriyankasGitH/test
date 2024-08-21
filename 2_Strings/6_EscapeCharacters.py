"""

Using escape characters so that you can add double quotes within double quotes


"""

def addSpace():
    print()

print("======== Using escape sequence for double quotes ========")

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
addSpace()

print("======== Using escape sequence for single quotes ========")
txt2 = 'It\'s alright.'
print(txt2)
addSpace()

print("======== Using escape sequence for backslash ========")
txt3 = "This will insert one \\ (backslash)."
print(txt3)
addSpace()

print("======== Using escape sequence for new line ========")
txt4 = "Hello\nWorld!"
print(txt4)
addSpace()

print("======== Using escape sequence for Carriage Return ========")
txt5 = "Hello\rWorld!"
print(txt5)
addSpace()

print("======== Using escape sequence for Tab ========")
txt6 = "Hello\tWorld!"
print(txt6)
addSpace()

print("======== Using escape sequence for backspace ========")
#This example erases one character (backspace):
txt7 = "Hello \bWorld!"
print(txt7)
addSpace()

print("======== Using escape sequence for octal value ========")
#This example erases one character (backspace):
#A backslash followed by three integers will result in a octal value:
txt8 = "\110\145\154\154\157"
print(txt8)

print("======== Using escape sequence for hex value ========")
#A backslash followed by an 'x' and a hex number represents a hex value:
txt9 = "\x48\x65\x6c\x6c\x6f"
print(txt9)