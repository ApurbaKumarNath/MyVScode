# List Basics
print('Showing list basics:')
List_Example = ['abc', 123, 12.3, True, False, 123]
print(List_Example)
print(len(List_Example))
print(type(List_Example)) #From Python's perspective, lists are defined as objects with the data type 'list'. Data type of a list = list.

'''List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.
When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
If you add new items to a list, the new items will be placed at the end of the list.
There are some list methods that will change the order, but in general: the order of the items will not change.
The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
Since lists are indexed, lists can have items with the same value.
A list can contain different data types.'''

List_Constructor = list(('abc', 123, 12.3, True, False)) # It is also possible to use the list constructor when creating a new list.
OneItem = ['One itemed list.',]; print(OneItem)
print('\n')
'''
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''



# Accessing List items
print('Accessing List items:')
print(List_Example[1], List_Example[2], List_Example[-2]) # List items are indexed and you can access them by referring to the index number. 
print(List_Example[0:3], List_Example[-1:-4:-1]) # Specified range of indexes.
if "apple" in List_Example:
  print("Yes, 'apple' is in the fruits list") 
print('\n')





# Changing List item values
print('Changing List item values:')
def a(): # I'm using def cz I don't wanna change the global variable.
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example[1]= 'acb'
  print(List_Example)
a()

def b():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example[2:4] = 'e3w', 'b4e'
  print(List_Example)
b()

def c():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example[1:2] = "avc", 'acv'
  print(List_Example)
c()  

def d():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example[1:3] = "I"
  print(List_Example)
d()

def e():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example.insert(2, 'G') # If u don't wanna replace, use insert. This is basically for adding items.
  print(List_Example)
e()
print('\n')






# Adding items
print('Adding items:')
def f():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example.append("T") # Wanna add something at the last of the list, use append.
  print(List_Example)
f()

def g():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example.extend(List_Constructor)
  print(List_Example)
g()

def h():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  Listtuple = ("12", 13)
  List_Example.extend(Listtuple) # The extend() method can append any iterable object (tuples, sets, dictionaries etc.).
  print(List_Example)
h()
print('\n')





# Removing items
print('Removing items:')
def i():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example.remove(123) # This is for removing specific items.
  print(List_Example)
i()

def j():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example.pop(2) # This is also for removing items, but you've to mention the index here.
  print(List_Example)
j()

def k():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example.pop() # Now it'll only remove the last item.
  print(List_Example)
k()

def l():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  del List_Example[1] # This also removes specified indexes.
  print(List_Example)
l()

'''def m():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  del List_Example # This will completely remove the list, and this will cause an error because you have succsesfully deleted "List_Example".
  print(List_Example)
m()'''

def n():
  List_Example = ['abc', 123, 12.3, True, False, 123]
  List_Example.clear() # List will remain, but with no content.
  print(List_Example)
n()
print('\n')








# Looping through lists
print('For Loop examples')
for x in List_Example:
  print(x)

print('\n')
# Explaining range() function
print("Range Function examples")
for i in range(5):
  print(i)

for a in range(2, 5):
  print(a)

for b in range(2, 9, 2):
  print(b)

# It basically works like this: range(Starting number, Stopping number(The sequence will stop one number before this value.), Steps)

# Now see how it works with letters
for c in range(len('Length')):
  print(c) # It'll only loop over the numbers.

for d in range(len(List_Example)):
  print(d) # It'll also iterate over the numbers.

for e in range(len(List_Example)):
  print(List_Example[e]) # But this time, it'll loop over the list.

# You could say what's the benefit of this! I could just use the line 146 and 147 for it. But no, there is more to it.

print('Now showing the main lesson from range function:')
for f in range(0, len(List_Example), 2):
  print(List_Example[f]) # This time it'll basically work like line 157, 158, but with the list, not numbers.

print('\n')







# Now see some while loop concept
print('While Loop examples')
i= 2
while i<6:
  print(i)
  i += 1 # this means i = i + 1
# Here i has to be less then 6. So, ans: 2, 3, 4, 5.

j = 5
while j>len('ABC'):
  print(j)
  j -= 1 # j = j - 1
# Here j has to be more than 3 which is the length of 'ABC'. So, ans: 5, 4.

k = 0
while k<len(List_Example):
  print(k)
  k += 1

print('Now showing the main lesson from while loops:')
l = 0
while l<len(List_Example):
  print(List_Example[l])
  l += 1
print('\n')








# Now explaining List comprehension:
print('List comprehension examples:')
# 1st example:
[print(x) for x in List_Example] # This will iterate in way.
# 2nd example of the same thing. But this will iterate differently. 
x = [x for x in List_Example]
print(x) # This basically shows the list normally. 

# List comprehension with range():
[print(y*y) for y in range(1,11)]

# You can also break it down like this:
y = range(1,11)
t = [v*v for v in y]
print(t) # But remember that printing like this only shows you the answer like a list.

rr = [x for x in range(10) if x<5] # Using if.
print(rr)

# Now, let's see more uses of if here:
'''
v = [x for x in List_Example if 'a' in x]
print(v)
This won't work because List_Example has different data types in it. 
To make it work, we need a variable with same data type.
'''

value = ['b', 'abc', '54rh', 'kakaTrue']
v = [x for x in value if 'a' in x]
print(v)

c = [x for x in value if x != "b"] # This means only show the values except b.
print(c)

s = [y if y != "b" else "ball" for y in value] # This will replace b with ball.
print(s)

u = ['Hi' for x in value] # You can choose to print anything.
print(u)

o = [x.upper() for x in value] # All outcome will be in uppercase.
print(o)
print('\n')






# Now we will see sorting lists:
print('Sorting list examples:')

abc = ['b', 'd', 'cat', 'abc']
abc.sort() # This will sort alphabetically. 
print(abc) # The output will be: None if you do this: print(abc.sort())

a12 = [2, 13, 212, 1, 0, 0.9, -21]
a12.sort() # Numerical sorting.
print(a12)

# Now if you want it reversed:
abc.sort(reverse= True); a12.sort(reverse= True)
print(abc); print(a12)

# Now if you want to reverse the order and not the sort:
abc.reverse(); print(abc)

# Capital letters sort before smaller letters.
ab = ['B', 'a', 'C', 'b']; ab.sort(); print(ab)

# To avoid this and sort alphabetically and have capital and small letters at the same time:
ab.sort(key= str.lower) # You can also customize your own function by using the keyword argument key = function.
print(ab)

def exm(n): # Here exm(n) is a function.
  return n*n
print(exm(10))

# Now using a different type of function with key argument:
def ex(x):
  return abs(x - 10) # Here abs = absolute. This means absolute value. e.g. abs(-50)= 50.

a12.sort(key= ex) # ex function will be used to sort here. The numbers closest to 10 will appear first and so on.
print(a12) # Remember you aren't subtracting here.







print('\n')
# Now we will see Copying lists:
print('Copying lists examples:')

copy1 = abc.copy(); print(copy1) # This is one way of copying. Another is:

copy2 = list(abc); print(copy2) # There are other ways too.







print('\n')
# Now we will see joining lists:
print('Joining lists examples:')

joined = copy1 + a12
print(joined) # This is one way of joining. Similarly,

copy1 += a12 # This means copy1 = copy1 + a12
print(copy1)

# Another way of joining:
for x in a12:
  ab.append(x)
print(ab)
'''Be careful about the indentation here. If you did this:
for x in a12:
  ab.append(x)
  print(ab)
The result would be different.'''

# One more way of joining:
abc.extend(a12)
print(abc) 




# See more list methods from here: https://www.w3schools.com/python/python_lists_methods.asp