x= 4
x= 'Salmon'
print("I like", x, "fish.") #x=4 is removed, because your 2nd assigned value will be counted as the actual value.

y= z= "Apurbo"
print(type(y), z) # Only the type will be shown for y, and value for z.

e= '''
    This is a multiline string.
    And you should learn how to use it with a variable.
    That's it.
    '''
print(e)

a= str(3) # Now it's assigned as a string, not integer.
A= float(3)
print(a, A) # To put different types together, just use comma, and those will be separated with spaces. And for same types, use (+), but these won't be separated with spaces.

"""
Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

"""

b, c, d= 'I ', 'like ', "programming."
print(b + c + d) # b, c & d are in same type, and that's why it(+) will work; otherwise it(+) won't work.

Integer_Float_String= ['4 ', '5.101', 'banana']
p, q, r = Integer_Float_String # Remember: If you try this: "Integer_Float_String= p, q, r", it won't work. p, q, r must be written first at the left side.
print(p + q, r) # This is called unpacking. 

# All you've seen are global variables, and now it's time to see local variables and its uses.
i= "Global variable"
def j():
    i= "Local variable" # This is a local variable.
    print(i) # This will print the local variable because it's inside a function named "j()". It'll only work inside this function, but global variables work everywhere.
j()
print(i) # This will print the global variable.

# It's time to use the global keyword.
def k():
    global j 
    j= ', global variable' #Now it is set as a global variable because of "global j". So, it's(j) not a local variable.
    print(i + j)
k()
print(j + '.')

# This is an example of string partitioning method:
s='subscribe'
print(s.partition('s'))

# It's time to properly learn casting:
m, n= '40', '60'
print(m + n)
print('The sum is', int(m) + int(n))
print('See this:', (int(m) + int(n)), '-', (int(m) + int(n)), '= 0')
print(3 * str(int(m)+int(n)))
print(3 * (int(m)+int(n)))
print(2 * 'This is fun.\n')

k= 2E10 # Here E or e is used to indicate power of 10.
o= 2J # Here J or j is used to indicate complex or imaginary number.
print(pow(o,2), k*5) # Here pow() = 'To the power of any number'.
# Another way of using power is:
print(2J**2)
# To get the floor value or least value:
print(5//2)
print(-5.0//2)
# To get the modulus:
print(5%2) # It basically gives you the remainder.

# Now see the use of random numbers:
import random
print(random.randrange(995,999))

# Now use input:
l, t= input("Enter 1st number: "), input("Enter 2nd number: ")
print("The numbers you gave are strings:", l+ ', ' +t) # Whatever you input are strings. So, you need to change those whenever you need. 
print("The sum of your given numbers is:", int(l)+int(t))
another_way=int(input('Enter: '))
print("Your number: ", another_way)