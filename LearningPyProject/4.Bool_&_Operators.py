#Check if an expression is true or false:
print(9>11)
Cat= 10
print(Cat==11)

#Checking the same thing with if-else statements:
if Cat>=10:
    print("You are something more than a newbie.")
else:
    print("You are something more than a fool.")

''' The bool() function allows you to evaluate any value, and give you True or False in return:
Almost any value is evaluated to True if it has some sort of content. Any string is True, except empty strings.
Any number is True, except 0. Any list, tuple, set, and dictionary are True, except empty ones.'''
print(bool(Cat))
print(bool("Hello!"))
print(bool(["apple", 66, "banana"]))

'''The following will return false:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

#If you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#You can create functions that returns a Boolean Value:
def m() :
  return 9==9
print(m())

#You can execute code based on the Boolean answer of a function. Print "YES!" if the function returns True, otherwise print "NO!":
def j():
    b=input("Enter any value: ") #Remember: the entered value is a str.
    return b
if j():
    print("YES!")
else:
    print("NO!")

#Check if an object is of a certain data type:
x= 21
print(isinstance(x, float))

'''To learn about operators, check this website: https://www.w3schools.com/python/python_operators.asp '''