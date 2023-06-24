''' Arrays
 To work with arrays in Python you will have to import a library, like the NumPy library.
 An array is a special variable, which can hold more than one value at a time.
 It is basically lists.
 To see array methods, use: https://www.w3schools.com/python/python_arrays.asp'''



# Now, see some basics of strings, Lists, Tuples, Sets and Dictionaries.
b = 1

'''
m = 'bvc'
m[b] = 'h'
print(m)
''' # As it's a string, it won't support something like m[b].
# TypeError: 'str' object does not support item assignment.

'''
v = (0,1)
v[b] = 0
print(v)
''' # TypeError: 'tuple' object does not support item assignment. Tuples also don't support this.



# Sets are unordered, so it won't work on sets either.


# But lists do support this.
v = [0, 'hh', '8']
v[b] = 'h'
print(v)
v[b] = b+12
print(v)

# But in a dictionary, it'll work differently.
m = {
    'a' : 'bb',
    'b' : 'hh'
}
m[b]= 0
print(m)