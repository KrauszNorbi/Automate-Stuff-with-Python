import json

favno_file = 'fav_number.json'

with open(favno_file) as f_obj:
    favourite_number = json.load(f_obj)
    print('Your favourite number is: ' + str(favourite_number))