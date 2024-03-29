#You can use ""(double) and ''(single) quotation for printing.
print("hello")
print('hello')

''' This is a multiline string.
    Python will ignore it. '''
""" This is also a multiline string. 
    It's a '''comment''' too. """

print('hello! This is "My first code."')
#print('hello! This is 'My first code.'') -This won't work. 
#print("hello! This is "My first code."") - This won't work too.
#So, to use "" & '' inside print function properly, you've to use multiline strings.
print('''hello! This is 
        "My first code."''')
print("""hello! This is 
"My first code." """) 
#print("""hello! This is "My first code."""") -This won't work because of 4("""").

#Now learn the use of \(escape)
print("\"The thief\" did not escape.")
print('\'The thief\' did not escape.')

#Now see the use of \n (new line)
print('The thief escaped.\nI let him escape.\tHaha') #\t is tab.

print('1','2','3') #3 arguments used. Automatic space is given when more than one argument is used.
print("I am fine."); print('He is fine too.') #This is the way of using many functions in one line.

#This time you're manually setting the end of the function.
print("I am fine.", end=" \t"); print('He is fine too.')  

#sep="" is seperator. If not used, a space will automatically be created. 
#If you need to use a specific string in between every argument, use sep.
print("hello Work!","How're you?","Working is great.","That's why I like your name.", sep="*|_|*\n")

#Now, check the use of f string = f"{}". For variables, use {}. If you want to write things your way, it's best to use this.
M = 0
print(f"{M}^0 = 0") # But things like \n will do their normal jobs here.

# If you wanna show \n or \t, use raw string literal = r"".
# Here backslashes \ are treated as literal characters instead of having special meaning as escape characters.
print(r"C:\Users\John\Documents\file.txt and \n \t {M} m[0]") # {} don't work like they do in f"". [] also don't work.

# If you don't want to use r"" to print \n, you can always use escape characters.
print('\\n and \\t, \'M')
help(print)

print("""
##             #############     ###     ########    ##           ##            ##############     #######                   ######     #######     ## ##       #############
##             ##              ##   ##   ##    ##    ## ##        ##                  ##         ##       ##               ##         ##       ##   ##    ##    ##
##             ##             ##     ##  ##    ##    ##   ##      ##                  ##        ##         ##            ##          ##         ##  ##      ##  ##
##             ########       #########  ##   ##     ##     ##    ##                  ##        ##         ##            ##          ##         ##  ##      ##  ########
##             ##             ##     ##  ##    ##    ##       ##  ##                  ##        ##         ##            ##          ##         ##  ##      ##  ##
##             ##             ##     ##  ##     ##   ##         ## #                  ##         ##       ##               ##         ##       ##   ##    ##    ##
#############  #############  ##     ##  ##      ##  ##           ##                  ##           #######                   ######     #######     ## ##       #############
""")