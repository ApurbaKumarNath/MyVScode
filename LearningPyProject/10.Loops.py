# While Loops:
i = 1
while i< 5:
    print(i)
    i += 2

print('\n')
# Wanna stop or break? Do this:
j = 9
while j > 2:
    print(j)
    if (j == 7):
        break
    j -=2

print('\n')
# Wanna skip only a specific number? Do this:
k = 0
while k< 4:
    k += 1
    if k == 3:
        continue
    print(k)

print('\n')
#Wanna print a message once the condition is false? Do this:
l = 0
while l < 2:
    print(l)
    l += 1
else:
    print("L is no longer smaller than 2.")




print('\n')
# For loops:
# stop after printing 'a'.
a = 'banana'
for x in a:
    print(x)
    if x == 'a':
        break

# Stop before printing 'p'.
b = 'apple'
for x in b:
    if x == 'p':
        break
    print(x)

# Skip l from variable b.
for y in b:
    if y == 'l':
        continue
    print(y)

for x in range(0,len(b),2):
    print(b[x])

for x in range(2, 9, 3):
    print(x)
else: # The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
    print('Finished!')

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Nested Loops:
z = ['good', 'bad']
yu = ['Apple', 'Candy']
for x in z:
    for y in yu:
        print(x, y)

# To keep for loop result empty:
for x in [12, 'good', 'Hi']:
    pass 



# Difference between pass and continue:
def a():
    for i in range(1, 3):
        if 2> i:
            pass   # Pass skips if-else but not the whole loop.
        else:
            num = i
        print('Passed statement successful')
    print(num)
a()

def b():
    for i in range(1, 3):
        if 2> i:
            continue    # Continue skips the loop for the specific value.
        else:
            num = i
        print('Passed statement successful')
    print(num)
b()