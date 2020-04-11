#filename = 'C:\School Stuff\Git_Repos\Automate-Stuff-with-Python\efile.txt'
filename = 'efile.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents + '\n')

with open(filename) as file_object:
    #contents = file_object.readlines() # creates a list stored in 'contents'
    for line in file_object:
        print(line.strip())

with open(filename) as file_object:
    contents1 = file_object.readlines()

    string = ''
    for line in contents1:
        string += line.rstrip() + '\n'
    
    replace = string.replace('Python', 'C#')
    print(replace)

while True:
    print('Hello! Please write down your name.')
    name = input()
    if name == 'quit':
        break
    else:
        print('Welcome, ' + name + ' !')
        with open(filename, 'a') as file_object:
            file_object.write('\n' + name)
    
while True:
    print('Why do you like programming, bro?')
    answer = input()
    if answer == 'quit':
        break
    else:
        print('Interesting!')
        with open(filename, 'a') as file_object:
            file_object.write('\n' + answer)