def display_message():
    print('Trying to do exercises in Functions chapter.')

display_message()

def favourite_book(title):
    print('One of my favourite books is ' + title + '.')

favourite_book('Lord of the Rings: The Fellowship of the Ring')

# default values in arguments
def make_shirt(size='Large', text='I love Python'):
    print('The printed shirt will be the size: ' + str(size) + ' and the printed text will be: ' + text + '.')

make_shirt('XXL', 'Blaze it')                     # positional arguments
make_shirt(size = 37, text = 'Imagine Dragons')   # keyword arguments
make_shirt('Large')
make_shirt('Medium')
make_shirt(text='AYAYA')

def describe_city(city_name, country_name='Denmark'):
    print(city_name.title() + ' is in ' + country_name.title() + '.')

describe_city('Kosice', 'Slovakia')
describe_city('Copenhagen')
describe_city('Helsingor')

# returns a formatted string
def city_country(city, country):
    cityAndCountry = '"' + city + ', ' + country + '"'
    return cityAndCountry.title()
    

KinS = city_country('Kosice', 'Slovakia')
print(KinS)

# returns a dictionary with optional argument
def make_album(artist_name, album_title, number_of_tracks=''):
    album = {'Artist' : artist_name, 'Album' : album_title}
    if number_of_tracks:
        album['Number of Tracks'] = number_of_tracks        
    return album

album_one = make_album('Linkin Park', 'Hybrid Theory')
album_two = make_album('Insomnium', 'Winter\'s Gate', 8)
album_three = make_album('Soilwork', 'Stabbing the Drama')

print(album_one, album_two, album_three)

# while loop to ask for album details and then print them
# while True:
#     print('Please enter album details below:')
#     print('Enter "q" anytime to quit.')

#     album_artist = input('Enter the artist name: ')
#     if album_artist == 'q':
#         break

#     album_title = input('Enter album title: ')
#     if album_title == 'q':
#         break

#     album_tracks = input('Enter number of tracks:')
#     if album_tracks == 'q':
#         break

#     album_details = make_album(album_artist, album_title, album_tracks)
#     print('The album created is: Artist: ' + album_artist + ', Title: ' + album_title + ', Number of Tracks: ' + album_tracks + '.')


# priting the items of the list
magicians = ['Houdini', 'Copperfield', 'Lim', 'Teller']
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# editing items in the list
def make_great(magicians): 
    magicians[:]=[i + ' the Great' for i in magicians]
    print(magicians)

make_great(magicians)
show_magicians(magicians)

# arbitrary amount of arguments
def sandwich_maker(*items):
    print('\nThe sandwich will contain these items:')
    for item in items:
        print('- ' + item)

sandwich_maker('tuna', 'olives', 'mozzarela')
sandwich_maker('pickels')
sandwich_maker('ham', 'egg', 'mayo', 'corn')

# name-value pairs = ** before info 
def build_profile(first, last, **info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in info.items():
        profile[key] = value
    return profile

norbi_profile = build_profile('Norbert', 'Krausz', location='Denmark', age='32', sex='Male')
print(norbi_profile)




