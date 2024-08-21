"""

-- Iterable: An object that can return an iterator. Examples include lists, tuples, strings, and dictionaries.
-- Iterator: An object with a __next__() method, which will return the next item. It keeps state information to know which item comes next.

"""
print("=========  Iterable & Iterator ===========")
# A simple list
my_list = [10, 20, 30, 40, 50]

# Get an iterator from the list
my_iter = iter(my_list)

# Using next() to get items from the iterator
print(next(my_iter))  # Output: 10
print(next(my_iter))  # Output: 20
print(next(my_iter))  # Output: 30
print(next(my_iter))  # Output: 40
print(next(my_iter))  # Output: 50

# If we call next() again, it will raise StopIteration
try:
    print(next(my_iter))  # This will raise StopIteration
except StopIteration:
    print("End of iterator reached.")
