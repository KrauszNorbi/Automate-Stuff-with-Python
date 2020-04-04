import random, sys

possibilities = ['rock', 'paper', 'scissors']
print('ROCK, PAPER, SCISSORS')
wins = 0
draws = 0
loses = 0 
while True:
    print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
    pInput = input()

    if pInput == 'r':
        print('Rock VS ...')
    elif pInput == 'p':
        print('Paper VS ...')
    elif pInput == 's':
        print('Scissors VS ...')
    elif pInput == 'q':
        print('Goodbye, GGs!')
        sys.exit()
    else:
        print('You entered invalid option.')