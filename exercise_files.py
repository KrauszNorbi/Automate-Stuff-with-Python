import json
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
    if name == 'q':
        break
    else:
        print('Welcome, ' + name + ' !')
        with open(filename, 'a') as file_object:
            file_object.write('\n' + name)
    
while True:
    print('Why do you like programming, bro?')
    answer = input()
    if answer == 'q':
        break
    else:
        print('Interesting!')
        with open(filename, 'a') as file_object:
            file_object.write('\n' + answer)


favno_file = 'fav_number.json'

fav_number = input('Hello! What is your favourite number? ')
with open(favno_file) as f_obj:
    favourite_number = json.load(f_obj)
    if fav_number == favourite_number:
        print('Your favourite number is already stored. Its: ' + str(favourite_number))
    else:
        with open(favno_file, 'w') as f_obj:
            json.dump(fav_number, f_obj)
            print('Favourite number stored.')


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    
    username = get_stored_username()
    if username:
        check = input('Is this: "' + username + '" the correct username? y/n ')
        if check == 'y':
            print("Welcome back, " + username + "!")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

greet_user()