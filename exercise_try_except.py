cats_file = 'cats.txt'
dogs_file = 'dogs.txt'

print('Please enter two numbers to add them together.')
print('Type "q" to exit the program.')

while True:
    first_number = input('First number: ')
    if first_number == 'q':
        break
    second_number = input('Second number: ')
    if second_number == 'q':
        break
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print('Please enter numbers only!')
    else:
        print('The result is: ' + str(result))


