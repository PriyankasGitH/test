"""

-- Loop with
    -- items()

"""

fruits = {

   "Fruit1" : {
       "name" : "Apple",
       "Color" : "red"
   },

    "Fruit2" : {
       "name" : "Banana",
       "Color" : "Yellow"
   },

    "Fruit3" : {
       "name" : "Pear",
       "Color" : "Green"
   }

}

for x, obj in fruits.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])
print("Above is the nested dictionary printed with inner loop")