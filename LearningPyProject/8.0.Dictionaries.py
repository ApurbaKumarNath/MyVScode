'''
Dictionaries are like key:value
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''
'''Remember one thing: in sets and dictionaries, 0 = False and 1 = True'''

types = {
    1: True,
    False: 0,
    "C": 10,
    'D': 'Dad'
}

print(types[1]) #The values in dictionary items can be of any data type.

wrong = {
    1: [4, 3, 'A'],
    True: ('abc', ''),
    # {1, 2,3}: {2, 3, 'N'} you cannot do this.
    False: {'G', 'V'}
}

print(wrong, 'and the length is:', len(wrong), 'and the type:', type(wrong)) # Dictionaries cannot have two items with the same key. 1 = True

construct = dict(name = "Apurba", age = '18+'); print(construct, '\n')






print('Access Dictionary Items:')
print('using get():', types.get('D'))
print('Using keys():', types.keys())
print('Using values:', types.values())
print('Using items():', types.items(), '\n') # Will look like tuples in a list.




print('Change Dictionary Items:')
changing = {
    'Rui': 'Fish',
    'Apurbo': 'Human'
}
changing['Rui'] = "Fi.."
print(changing['Rui'])
changing.update({'Apurbo': 'Meta_Human'})
print(changing['Apurbo'], '\n')





print('Add Dictionary Items:')
changing['chicken'] = ['Food', 'Tasty']
print(changing)
changing.update({5:'Chill!'})
print(changing, '\n')





print('Remove Dictionary Items:')
changing.pop(5)
print('Using pop():', changing)
changing.popitem()
print('Using popitem():', changing) # The popitem() method removes the last inserted item.
# del keyword can also delete the dictionary completely: del changing
changing.clear() # The clear() method empties the dictionary.
print(changing, '\n')





print("Checking if 10 exists in types:", 10 in types, '\n') # Didn't work cz it's a value, not a key.




print('Loop Dictionaries:')
for x in types:
    print(x) # Only loops keys. 
print('\n')

for x in types.keys():
    print(x) # This does the same.
print('\n')

for x in types:
    print(types[x]) # Only loops values.
print('\n')

for x in types.values():
    print(x) # This does the same.
print('\n')

for x, y in types.items():
    print(x, '=', y) # Loops both keys and values.
print('\n')






print('Copy Dictionaries:')
'''You cannot copy a dictionary simply by typing dict2 = dict1, 
   because: dict2 will only be a reference to dict1, 
   and changes made in dict2 will automatically also be made in dict1.'''

right = wrong.copy()
print('Using copy():', right)

copy = dict(right) 
print('Another way is dict():', copy, '\n')






print('Nested dictionaries:')
numbers = {
    'num1': {
        'a': "10",
        'b': '11',
        'c': '12'
    },

    'num2': {
        'd': 10,
        'e': 11,
        'f': 12
    },

    'num3' : {
        'g': 100,
        'h': 101,
        'i': 102
    }
}

print('Now I want "a":', numbers['num1']['a'])

# Now you can also do it in this way if you don't want to make a nested dictionary:
num4 = {
    'ab': "10",
    'bc': '11',
    'ca': '12'
}

num5 = {
    'da': 10,
    'eb': 11,
    'fc': 12
}

num6 = {
    'ga': 100,
    'hb': 101,
    'ic': 102
}

mynumbers = {
    'num4': num4,
    'num5': num5,
    'num6': num6  # Don't forget to keep the variables at the right side. It gives error if variables are kept at left.
}

print(mynumbers['num6']['ga']) # Now it'll print exactly like a nested dictionary.

# To check out other dictionary methods, check: https://www.w3schools.com/python/python_dictionaries_methods.asp