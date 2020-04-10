from collections import OrderedDict
from random import randint

glossary = OrderedDict()

glossary['Dictionary'] = 'In Python dictionaries are written with curly brackets, and they have keys and values.'
glossary['List'] = 'A list is created by placing all the items (elements) inside a square bracket [ ], separated by commas.'
glossary['Value'] = 'Values() is an inbuilt method in Python programming language that returns a list of all the values available in a given dictionary.'

for key, value in glossary.items():
    print(key, ' -> ', value)


class Die():
    def __init__(self, sides = 6):
        super().__init__()
        self.sides = sides

    def roll_die(self):
        x = randint(1, self.sides)
        print('The die has ' + str(self.sides) + ' sides, and the rolled number is ' + str(x) + '.')

sixDie = Die()
tenDie = Die(10)
twentyDie = Die(20)

roll = 0
while roll <= 10:
    sixDie.roll_die()
    roll += 1

while roll <= 10:
    tenDie.roll_die()
    roll += 1

while roll <= 10:
    twentyDie.roll_die()
    roll += 1
    