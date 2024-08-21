"""

Updating value of the list item

-- Change item value

    -- A single item
    -- A range of items
    -- Insert more than mentioned
    -- Insert less than mentioned
    -- Insert method

"""

def addSpace():
    print()

# Change item value

print("=================   Updating 2nd list item  ==============")
fruits = ["Straberry","Blueberry","Raspberry"]
fruits[1]="Kiwi"
print(fruits)
addSpace()

print("=================   Updating a range of list item  ==============")
fruits = ["Straberry","Blueberry","Raspberry","Apple","Banana","Cherry"]
fruits[1:4]=["Kiwi","watermelon","Blackcurrent"]
print(fruits)
addSpace()

print("=================   Inserting more items than mentioned  ==============")
fruits = ["Straberry","Blueberry","Raspberry"]
fruits[1:2]=["Kiwi","Blackcurrent"]
print(fruits)
addSpace()

print("=================   Inserting less items than mentioned  ==============")
fruits = ["Straberry","Blueberry","Raspberry"]
fruits[1:3]=["Kiwi"]
print(fruits)
addSpace()


print("=================   Use insert method with index number  ==============")
fruits = ["Straberry","Blueberry","Raspberry"]
fruits.insert(2,"Pear")
print(fruits)
addSpace()