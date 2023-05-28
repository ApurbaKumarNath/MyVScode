'''
A set is a collection which is unordered, unchangeable*, and unindexed.
Set items are unchangeable, but you can remove items and add new items.
Sets are unordered, so you cannot be sure in which order the items will appear.
'''
'''Remember one thing: in sets and dictionaries, 0 = False and 1 = True'''

s = {'abc', -2, True, False}; print(s, type(s), len(s))

s1 = set((1,)); print(s1)

# Duplicates not allowed: Sets cannot have two items with the same value.
d = {'a', 'a'}; print(d)

# The values True and 1 are considered the same value in sets, and are treated as duplicates:
d1 = {True, 1}; print(d1, '\n')




print('Checking Set items:')
print('Checking if 1 exists in d1:', 1 in d1, '\n')




print('Looping sets:')
for x in s:
    print(x)
print('\n')




print('Adding items:')
s1.add('True'); print(s1, '\n')



print('Removing items:')
'''
To remove an item in a set, use the remove(), or the discard() method.
If the item to remove does not exist, remove() will raise an error.
If the item to remove does not exist, discard() will NOT raise an error.
'''

s1.remove('True'); print(s1)
s1.discard('False'); print(s1) # It won't show any error.

# Use pop method if you want to remove a random item. 
r = {1, 2, 3, 4}
r.pop(); print(r)

r.clear(); print(r, '\n') # This method empties the set.

# del r will completely delete the set, and if printed, it'll show an error.




print('Joining sets:')
r1 = ['a', 'b']
r2 = {5, 6, 'a'}

r.update(r1); print(r) # update() method can be used for any iterable object. 

r3 = r.union(r2); print(r3) # union() is used for returning a new set. Here it's r3.

# Both union() and update() will exclude any duplicate items.

# To get the duplicate items:
r.intersection_update(r3); print(r)
r4 = r.intersection(r3); print(r4) # intersection() is for a new set.

# To completely exclude duplicates:
r.symmetric_difference_update(r3); print(r)
r5 = r4.symmetric_difference(r3); print(r5) # This is for a new set. 

# To learn more about set methods, see this: https://www.w3schools.com/python/python_sets_methods.asp