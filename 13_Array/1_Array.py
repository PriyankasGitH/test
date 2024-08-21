"""
-- An array is a special variable, which can hold more than one value at a time.

-- An array can hold many values under a single name, and you can access the values by referring to an index number.

--  Python does not have built-in support for Arrays, but Python Lists can be used instead.

-- To work with arrays, we need to import NumPy is a Python library.

-- NumPy is used for working with arrays.

-- NumPy is short for "Numerical Python".

"""
import numpy as np

print("============= Printing the entire array as a list : no need to import NumPy =============")
cars = ["Ford", "Volvo", "BMW"]

print(cars)


print("============= Printing the entire array as a list : need to import NumPy =============")
my_array = np.array([1, 2, 3, 4, 5])
print(my_array)
print(my_array[1])