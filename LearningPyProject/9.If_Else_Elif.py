if 33 <= 32:
    print('You are a fool.')
elif 33 != 32:   # The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
    print("You are right.")
else:
    print('This will not even be printed.')
print('\n')






print("Short hand if-else:")
if 1<=2: print("One line code.")

print("Right!") if 3 == 30-27 else print('Oops!') # This technique is known as Ternary Operators, or Conditional Expressions.

# If you want to use elif in one line, you have write it this way:
print(404) if 1 == 100 else print('OK') if 3==3 else print('Wrong!') # You can't write elif here.





# And Or Not logical operators. 
if 33<34 and 44>12:
    print("Both conditions need to be true.") # And keyword.

if 1<2 or 2<1:
    print('Only one condition needs to be true.') # Or keyword.

if not 1>12:
    print("It reversed the statement.") # Not keyword.





# Nested If:
x = 15
if x>10:
    print('X is above 10', end=" ")
    if x> 14:
        print('and 14.')
else:
    print("Nothing.")





# You cannot keep if statement empty except:
if 1>2:
    pass # Doesn't matter if you're right or wrong. It will pass which means it'll not print anything.
