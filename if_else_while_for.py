# if / elif / else

name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Are you a vampire?')
elif age > 100:
    print('You are not Alice, grannie.')



print('Enter a name.')
name = input()
if name: # Truthy / Falsey values - blank sting = Falsey, all non-sting = Truthy
    print('Thank you for entering a name.')
else:
    print('You did not enter a name.')

# for integers or floats: 0, 0.0 = Falsey

#------------------------------------------------------
# while loop:

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank You!')


name = ''
while True: # infinite loop
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break # execution jumps out of the loop
print('Thank You!')


spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # execution jumps back to the start of the while loop
    print('spam is ' + str(spam))


#-------------------------------------------------------
# for loops:

print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

print('My name is')
for i in range(12, 16): # (from -> upto, not included)
    print('Jimmy Five Times ' + str(i))

print('My name is')
for i in range(0, 10, 2): # third argument = step argument 
    print('Jimmy Five Times ' + str(i))

print('My name is')
for i in range(5, -1, -1):
    print('Jimmy Five Times ' + str(i))

