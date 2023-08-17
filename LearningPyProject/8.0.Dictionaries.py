'''
Dictionaries are like dic = {key:value}
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionary keys can be Strings, numbers, and tuples; values can be of any data type.
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
print('using get():\n', types.get('D'), types.get(1, 'FF'))  # get(1, 'FF') = get(1) for this dict.
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
changing['chicken'].append('Fried') # changing['chicken'] was the list ['Food', 'Tasty'], now it's changed.
print(changing)

print(changing.get(1, ['Apurba', 'the', 'great!', 'XD'])) # Will only print the list. Won't add anything in the dict.
var = changing.get(1, ['Apurba', 'the', 'great!', 'XD'])
print(var) # Prints the same thing.
# changing.get(1, ['Apurba', 'the', 'great!', 'XD']) doing this won't add anything in the dict.

changing.update({5:'Chill!'})
print(changing, '\n')





print('Remove Dictionary Items:')
changing.pop(5)
print('Using pop():', changing)
''' Remember that in dict you need atleast one argument for using pop. 
    So, changing.pop() will show an error.
    And changing.pop(0,1) is okay to use. It can take more than one argument. '''

changing.popitem()
print('Using popitem():', changing) # The popitem() method removes the last inserted item.
var2 = changing.popitem() # var2 = last item in a tuple.
print(var2)

# del keyword can also delete the dictionary completely: del changing

changing.clear() # The clear() method empties the dictionary.
print(changing, '\n')





print("Checking if 10 exists in types:", 10 in types, '\n') # Didn't work cz it's a value, not a key.




print('Loop Dictionaries:')
for x in types:
    print(x) # Only loops keys. 
print('\n')

for x in types.keys():       # types.keys() = [1, False, 'C', 'D']
    print(x) # This does the same.
print('\n')

for x in types:
    print(types[x]) # Only loops values.
print('\n')

for x in types.values():      # types.values() = [True, 0, 10, 'Dad']
    print(x) # This does the same.
print('\n')

for x, y in types.items():    # types.items() = [(1, True), (False, 0), ('C', 10), ('D', 'Dad')]
    print(x, '=', y) # Loops both keys and values.
print('\n')






print('Copy Dictionaries:')
'''You should not copy a dictionary simply by typing dict2 = dict1, 
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