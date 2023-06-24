# A lambda function can take any number of arguments, but can only have one expression.
# lambda arguments : expression
x1 = lambda a : a + 'Kumar' + " Nath"
print(x1('Apurbo '))
print(x1('Apurba '))
# print(x1(10 )) will be wrong here. Because I used + in expression.

print('\nLambda functions can take any number of arguments:')
x2 = lambda a, b : f'({a}+{b})^2 = {a**2 + 2*a*b + b**2}'
print(x2(a = int(input()), b = int(input())))

print('\nUsing lambda as an anonymous function inside another function:')
def x3(a):
  return lambda x: a+x
b = x3(10)   # Here b is the function of the lambda, and 10 is the value of a.
print(b(11)) # Here 11 is the value of the lambda b.

print('\nSeveral functions in a function:')
def x4(a):
  return lambda x: a*x

b1 = x4(2)
b2 = x4(3)

print(b1(3))
print(b2(2))
