x= ''' Apurbo likes to go around. 
He is used to studying, and he sometimes wants to die.
Sometimes he feels really bored of life. '''

print(len(x)) # This shows the length of the text.
'''
Number system with strings: (You're gonna learn slicing here.)
In Strings,
0 1 2 3 4 5 6
S t r i n g s
Here, if you use x[1:3], python always skips the last value. So, it will show: tr

Now, if you use minus(-), 0 won't exist, and it'll count backwards like this:
-1 -2 -3 -4 -5 -6 -7
 s  g  n  i  r  t  S
If you don't input a value and keep it like this: x[::], by default it'll count left to right like this: x[0:last number:1].
x[Start:End:Step] this is the formula.

And if it is x[::-1], it'll count from right to left.
So, x[6:4] won't show a value (won't show error) because it counts from left to right, and you gave no value to the right. Instead, you entered a value which is at the left.
But x[6:4:-1] is possible because it counts from right to left. 

Now, if you use x[::2], it'll count from left to right and take every 2nd element.
x[::-3] means it'll count from right and take every 3rd element.
'''
print(x[:], '\n')
print(x[::], '\n')
print(x[:6]) 
print(x[-118::-1])
print(x[-2:-9:-2], '\n')

# Now see some nice functions: (To check more, see: https://www.w3schools.com/python/python_ref_string.asp )

print(x.isalnum()) # This checks if the str is alphanumeric(meaning alphabet letter (a-z) and numbers (0-9)) or not.
print(x.isalpha()) # This checks if all the characters are alphabet letters (a-z).
print(x.endswith('ife.')) # Checks if the str ends with the letters I've given here.
print(x.count('a')) # Checks how many 'a's are in the str.
print(x.count('')) # Counts how many letters are there, but it adds 1 more to the count. For example: For 'Y', answer is: 2.
print(x.capitalize(), '\n') # This capitalizes only the 1st letter of the text. But I've already capitalized that.
print(x.lower(), '\n') # This will convert the str into lowercase letters.
print(x.upper(), '\n') # This will convert the str into uppercase letters.
print(x.find('is')) # This will show where the word 'is' is by showing me the position number of the str.
print(x.replace('Apurbo', 'Apurba'))
print(x.strip()) # This method removes any whitespace from the beginning or the end.
b=x.split('o')
print(b) # This method splits the string into substrings if it finds instances of the separator. Here, 'o' is set as a separator, so, it will be removed.
print(x.split()) # Here spaces were detected as separators, so, all spaces were removed, and substrings were created.
print(len(x.split())) # Now you will be able to see how many words you wrote.

# To check if a certain phrase or character is present in a string, we can use the keyword in:
print('Apurba' in x)
print('Apurbo' in x)
print('God' not in x)

# Now see some if-else functions:
if 'life' in x:
    print("Yes, 'life' is present in the text.")
if 'God' not in x:
    print("No, 'God' is not present in the text.")

# Now see some looping functions:
for p in 'Rock':
    print(p)
for y in 'Yo', 'Yeah', 'Boom!':
    print(y)
for z in '''Nice strings!
Very nice!''':
    print(z)

# Now learn the format() method. We can combine strings and numbers by using this method!
q= 20
print('My age is: {}'.format(q))

jsc= 5.00
ssc= 4.83
hsc= '5.00(Golden)'
result= "I achieved gpa {:.2f} in jsc, {} in ssc, and {} in hsc examination."
print(result.format(jsc, ssc, hsc))

price= 2.550
pencil_pen= 3
rubber= 1
r= "I wanna buy {1} pencils, {2} rubber, and {1} {0:.3f}$ pens." # You can use index numbers {0} to be sure the arguments are placed in the correct placeholders.
print(r.format(price, pencil_pen, rubber)) 

s= 'My name is {name}; I am {age} years old. My height is {height}.'
print(s.format(name= 'Apurba', age=20, height= "5'7\""))