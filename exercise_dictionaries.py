Miro = {'first_name': 'Miroslav' , 'last_name': 'Hruska', 'age': 30, 'city': 'Kosice'}
print(Miro['first_name'])
print(Miro['last_name'])
print(Miro['age'])
print(Miro['city'])

Rudo = {'first_name': 'Rudolf' , 'last_name': 'Klecun', 'age': 32, 'city': 'Kosice'}
Petka =  {'first_name': 'Petra' , 'last_name': 'Vadaszova', 'age': 31, 'city': 'Prague'}
Kubo =  {'first_name': 'Jakub' , 'last_name': 'Marek', 'age': 32, 'city': 'Poprad'}

People = [Miro, Rudo, Petka, Kubo]
for person in People:
    print(person)

#People.append(Kubo)
#print(People)

favourite_numbers = {'Miro': 'Blue', 'Miska' : 'White', 'Noro' : 'Black', 'Rudo' : 'Red'} 
for name in favourite_numbers:
    print(name, ':', favourite_numbers[name])

Glossary = {'Dictionary' : 'In Python dictionaries are written with curly brackets, and they have keys and values.', 'List' : 'A list is created by placing all the items (elements) inside a square bracket [ ], separated by commas.', 'Value' : 'Values() is an inbuilt method in Python programming language that returns a list of all the values available in a given dictionary.'}
for key in Glossary:
    print(key, '->', Glossary[key], '\n')

Rivers = {'Kosice' : 'Hornad', 'Bratislava' : 'Dunaj', 'Poprad' : 'Poprad'}
for river in Rivers:
    print(Rivers[river], 'runs through', river + '.')

for river in Rivers.values():
    print(river)

for river in Rivers.keys():
    print(river)


cities = {
    'Copenhagen' : {
        'Country' : 'Denmark',
        'Population' : 1000000,
        'Fact' : 'Capital of Denmark'
    },
    'Chicago' : {
        'Country' : 'USA',
        'Population' : 2700000,
        'Fact' : 'City of Lost Heaven'
    },
    'Kosice' : {
        'Country' : 'Slovakia',
        'Population' : 240000,
        'Fact' : 'Its nice'
    }
}
for city, city_info in cities.items():
    print('\nCity: ' + city)
    Country = city_info['Country']
    Population = city_info['Population']
    Fact = city_info['Fact']

    print('\tCountry: ' + Country.title())
    print('\tPopulation: ' + str(Population))
    print('\tFact: ' + Fact.title())

