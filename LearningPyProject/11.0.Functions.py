'''
A function is a block of code which only runs when it is called. 
You can pass data, known as parameters, into a function. A function can return data as a result.

** You cannot use a variable outside of a function inside a function. To use, set the variable locally.
   However, you can use a variable outside of a function as an argument of the function.
**
** 
Similarly, you cannot use a local variable outside of a function. To use, set it to global.
   e.g. global x
        x = 10 
**
'''

def call():
  x = 'Local variable'
  print('You can call a function as many times as you want.')
  return x
call()
print(call())

x = 10
def parameter(x = 2): # The default value of x is 2.
  print(x*2)
  x = 3          # This Local variable(x) is never equal to the parameter x.
  print(x)
  return x
  print(111)     # It simply doesn't print because a value is returned. To print it, write it before returning.
y = parameter(121)
print(parameter(x)) 
'''
Remember: Python prioritizes given argument more than default value.
Only if no argument is given, python uses the default value as argument. See line 66 to 69 for example.

Step by step execution of the code:
1. default value x = 2
2. as y = parameter(121), the function has been called with the argument 121.
3. so, it prints 121*2 = 242; then, it takes the local variable x = 3 and prints 3. 
4. returned value 3 to parameter(121). y = parameter(121) = 3.
5. for print(parameter(x)), the function has been called with the argument 10. (x = 10 global variable)
6. it'll print x*2 = 10 * 2 = 20.
7. x = 3, and prints 3.
8. returned value 3 to parameter(10). parameter(10) = 3.
9. finally prints 3 # Actually, In this function, parameter(any value) = 3 as it only returns 3 to the function.

Conclusion: function call will work first, then, other stuff. 
And a function can be called inside from print(as in line 20 and 30) or a variable(as in line 29) or etc.(as in line 87).
Remember all the print statements inside the function are executed serially when the function is called.
If returned any value, function(argument) = returned value. If not returned, function(argument) = None.
'''

print(f'y has the value of parameter(121), and that is {y}. \n')



val = 11
def globe(val):
  # global val # you can't make the parameter name global inside the function.
  print('You can set a global variable as an argument:', val, '\n') # Here, val = 11
globe(val)





def default(x = int(input('Number: ')), y = 'haha.'):
  print('If we call the function without argument, it uses the default value:', x, y)
default()
default('One argument given this time,')





print('\nThe order of the arguments does not matter if you use key = value syntax.')
def order(x, y, z):
  return (x*y)/z
Value = order(z = 111, x = 33, y = int(input('Number: ')))
print(order(z = 6, x = 33, y = 6))
print(Value, '\n')




print('You can call a function to another function.')
def calling(var):
  return var * order(6, 2, 3)
print(calling(10), '\n')




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
dic(string = ['Keys', 'of a dict'], num = ('can', 'be'), tuples = 'str, numbers and tuples.')
# Here, string, num and tuples will be set as keys of dictionary d. ['string', 'num', 'tuples']




print('\nThe pass Statement: passed')
def passing(x):
  pass