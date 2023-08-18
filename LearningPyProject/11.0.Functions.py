def call():
  print('You can call a function as many times as you want.')
call()
call()

x = 10
def parameter(x = 2): # The default value of x is 2.
  x = 3
  print(x)       # It'll print 3. Not 2 nor 10.
  return x       # This means that the value of x will be returned to parameter() function.
  print(111)     # It simply doesn't print because a value is returned. To print it, write it before returning.
y = parameter(x) # Guess what will be y. Here, y = parameter(10)
print(parameter(x)) 
'''
Here, x was 10.(Global var) and default value x was 2, but, parameter(any value) = 3 as returned value is 3.
To conclude, python ignores global variables and default values when a value is returned.
Python even ignored the argument given. Because locally x was set as 3.
'''

print(f'y has the value of parameter(any value), and that is {y}. \n')

'''
Imagine the previous code in this way:
def parameter():
  return 3
print(parameter()) # Simply prints 3. Both codes work similarly.
'''

def default(x = int(input('Number: ')), y = 'haha.'):
  print('If we call the function without argument, it uses the default value:', x, y)
default()
default('One argument given this time,')

print('\nThe order of the arguments does not matter if you use key = value syntax.')
def order(x, y, z):
  return (x*y)/z
Value = order(z = 111, x = 33, y = int(input('Number: ')))
print(Value, '\n')


val = 11
def globe(val):
  # global val # you can't make the parameter name global inside the function.
  print('You can set a global variable as an argument:', val, '\n') # Here, val = 11
globe(val)


print('Using Loop in a function:')
def loop(L):
  for x in L:
    print(x)
list1 = [True, 'str', 1.01, 55]
loop(list1)
loop({'Tea': 'Nothing'})


print('\nUsing * means the function will receive a tuple of arguments.')
def tup(*t): 
  print(t[1:3])
tup('string', 123, ('More', 'tuple'), ['A', 'list'])


print('\nUsing ** means the function will receive a dictionary of arguments.')
def dic(**d):
  print(d.items())
dic(string = 'Keys of a dict', num = 'can be', tuples = 'str, numbers and tuples.')
# Here, string, num and tuples will be set as keys of dictionary d. ['string', 'num', 'tuples']

print('\nThe pass Statement: passed')
def passing(x):
  pass