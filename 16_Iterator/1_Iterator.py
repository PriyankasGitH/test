"""
-- An iterator is an object that contains a countable number of values.

-- An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

-- An iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

-- Lists, tuples, dictionaries, and sets are all iterable objects.
    -- They are iterable containers which you can get an iterator from.
    -- All these objects have a iter() method which is used to get an iterator
    -- Even strings are iterable objects, and can return an iterator:

"""

print("========= Iter & Next : with int within a list ===========")
# Example list
my_list = [1, 2, 3, 4, 5]

# Get an iterator using iter()
my_iter = iter(my_list)

# Use next() to get the next item from the iterator
print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
print(next(my_iter))  # Output: 4
print(next(my_iter))  # Output: 5

# If you call next() again, it will raise a StopIteration error
# print(next(my_iter))  # Uncommenting this line will cause a StopIteration error

print("========= Iter & Next : with String ===========")

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))