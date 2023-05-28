# Tuples are similar to Lists. But it's unchangeable. 
print('Basics:')

t1 = (1, 'ba', True, False, 'ba')
print(len(t1))

t2= (1,) # Tuple with one item only.
print(type(t2))

t3 = tuple((2, )) # Tuple construction.
print(t3, '\n')




print("Accessing tuples:")
print(t1[-1:-3:-1]) # Exactly the same as lists.

print("Checking if an item exists:")
if 2 in t1:
    print('Yes, it exists.')
else: 
    print("No, doesn't exist.")

print("For changing, adding, and removing items in a tuple, you have to convert it to a list:")
l1 = list(t1)
l1[:3] = 'Now,', 'changed', 'tuple:'
print(tuple(l1))

l2 = list(t2)
l2.insert(1, 'Added item')
t2 = tuple(l2)
print(t2)

l3 = list(t1)
l3.pop(2)
print('Removed one item:', tuple(l3))

'''
del t3 
print(t3) #If you do this, it'll show an error, and unlike lists, you can't use del to remove specific items.
'''

print('Adding tuple to a tuple:')
t3 += t2 ; print(t3, '\n')




print('Unpacking tuples:')

u1 = ('abc', 'bcd', 'cba')
(a1, b1, c1) = u1 
''' If you didn't want u1 to exist, you could also write: (a1, b1, c1) = ('abc', 'bcd', 'cba')
    we are allowed to extract the values back into variables. This is called "unpacking"      '''
print(a1, b1, c1)

''' If the number of variables is less than the number of values, 
    you can add an * to the variable name and the values will be assigned to the variable as a list: '''

u2 = ('ab', 'bc', 'ca', 'xy', 'yz')
(a2, b2, *c2) = u2
print(a2, b2); print(c2)

'''If the asterisk is added to another variable name than the last, 
   Python will assign values to the variable until the number of values left matches the number of variables left.'''
(a3, *b3, c3) = u2
print(a3, b3, c3, '\n')




print('Loop Tuples:')
for x in t1:
    print(x)

for i in range(1, len(t1), 2):
    print(t1[i])

j = 0
while j < len(t1):
    print(t1[j])
    j += 1
print('\n')




print('Join Tuples:')
t1 += t2
print(t1)


print("Multiplying Tuples:")
m1 = t1* 2
print(m1)


print("Counting 'ba' in t1:", t1.count('ba'))
print("The first occurrence of 'ba' in t1 is index no.:", t1.index('ba'), '\n')
print('I am done with tuples.')
