def f1():
    print('1st function.\n')
f1()

def f2(a):
    print(a**2, '\n')
f2(10)
f2(2)

def f3(x, y):
    print((x+y)**2, '\n')
f3(2, 3)

print('User input examples:')
def f4(x = int(input('Input a number: '))):
    print(f"{x} x 2 =", x*2, '\n')
f4()

print('If you do not know how many keyword arguments that will be passed into your function, add: *')
def f5(*x): # the function will receive a tuple of arguments
    print('Your 3rd input was: ', x[2], '\n') 
f5(input(), input(), input(), input())

print('The order of the arguments does not matter if you use key = value syntax')
def f6(a, b, c):
  print('The variable b is:', b, '\n')
f6(b = 66, a = 10.09, c = '22')

print('If you do not know how many keyword arguments that will be passed into your function, add: **')
def f7(**x): # the function will receive a dictionary of arguments
  print(x, x['x'], x['a'], '\n')
f7(a = 10, x = 99)

print('If we call the function without argument, it uses the default value:')
def f8(x = True):
  print('The default value is', x)
f8()
f8('not False')

print('\nUsing Loop in a function:')
def f9(L):
  for x in L:
    print(x)
list1 = [True, 'str', 1.01, 55]
f9(list1)
f9(['Tt',])

print('\nTo let a function return a value, use the return statement:')
def f10(x):
  return 33 + x
print(f10(2))
print(f10(3))

print('\nThe pass Statement: passed')
def f11(x):
  pass