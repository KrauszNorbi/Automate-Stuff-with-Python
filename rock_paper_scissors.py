import random, sys

print('ROCK, PAPER, SCISSORS')
wins = 0
draws = 0
loses = 0 
while True:
    print('Your scores are: %s wins, %s loses, %s draws.' %(wins, loses, draws))

    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors, or (q)uit')
        playerChoice = input()
        
        if playerChoice == 'r' or playerChoice == 'p' or playerChoice == 's':
            break
        elif playerChoice == 'q':
            print('Goodbye, GGs!')
            sys.exit()
        else:
            print('You have enter incorrect value.')
        
    if playerChoice == 'r':
        print('Rocks VS ...')
    elif playerChoice == 'p':
        print('Paper VS ...')
    elif playerChoice == 's':
        print('Scissors VS ...')


    randomChoice = random.randint(1,3)
    computerChoice = ''

    if randomChoice == 1:
        computerChoice = 'r'
        print('Rock')
    elif randomChoice == 2:
        computerChoice = 'p'
        print('Paper')
    elif randomChoice == 3:
        computerChoice = 's'
        print('Scissors')

    if playerChoice == 'r' and computerChoice == 'r':
        print('It\'s a draw.')
        draws = draws + 1
    elif playerChoice == 's' and computerChoice == 's':
        print('It\'s a draw.')
        draws = draws + 1
    elif playerChoice == 'p' and computerChoice == 'p':
        print('It\'s a draw.')
        draws = draws + 1
    elif playerChoice == 'r' and computerChoice == 'p':
        print('You lost.')
        loses = loses + 1
    elif playerChoice == 'r' and computerChoice == 's':
        print('You won.')
        wins = wins + 1
    elif playerChoice == 's' and computerChoice == 'r':
        print('You lost.')
        loses = loses + 1
    elif playerChoice == 's' and computerChoice == 'p':
        print('You won.')
        wins = wins + 1
    elif playerChoice == 'p' and computerChoice == 's':
        print('You lost.')
        loses = loses + 1
    elif playerChoice == 'p' and computerChoice == 'r':
        print('You won.')
        wins = wins + 1


