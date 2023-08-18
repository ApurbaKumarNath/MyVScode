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
  # x = 2  # If you did this, python wouldn't take the default value as x. It will take x = 2.
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



def f11(comments):
   comments = 33 # Here, this comments isn't equal to parameter (comments). This is counted as a separate variable.
   return comments//3 # Now, the value 33 will be returned to f11
f11(17) # Here, you have to give an argument for the parameter (comments)
print('\nPrinting the returned value:', f11(12)) 

'''
If you did the f11() code like this:
def f11():
   comments = 33 
   return comments//3
f11() # This won't print anything.
print(f11()) # This will print 11.

So, basically what I'm saying is: you can simply do the code without passing arguments if you have to do something like this.
'''


inside = 12
def f12(inside):
#  global inside # The parameter name can't be made global. 
   inside = 1
   print('\nPrinting only the local variable:', inside)
f12(11)


def f13(inside):
   return inside*2
print('\nPrinting global variable:', f13(inside)) # Here, inside = 12

print('\nThe pass Statement: passed')
def f14(x):
  pass