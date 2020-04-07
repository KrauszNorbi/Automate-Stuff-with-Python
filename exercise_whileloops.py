# print('\nWhich toppings would you like on your pizza?')
# print('Type "quit" to exit.')
# number_of_toppings = 0

# while True:
#     toppings = input()
#     if toppings == 'quit':
#         break 
#     else:
#         if number_of_toppings < 5:
#             print('I will add ' + toppings + ' on your pizza.')
#             number_of_toppings = number_of_toppings + 1
#         else:
#             print('No more toppings for you my friend.')



# print('What is your age?')
# while True:
#     age = input()
#     if age.isalpha and age == 'quit':
#         break
#     elif age.isalpha():
#         print('You did not enter valid information (number).')
#     elif age.isdigit():
#         if int(age) > 0 and int(age) < 3:
#             print('The ticket is free.')
#         elif int(age) > 3 and int(age) < 12:
#             print('The ticket is 10 Eur.')
#         elif int(age) > 12:
#             print('The ticket is 15 Eur.')


# sandwich_orders = ['tomato_sandwich', 'pastrami_sandwich', 'ham_sandwich', 'avocado_sandwich', 'pastrami_sandwich', 'chicken_sandwich', 'pastrami_sandwich']
# finished_sandwiches = []

# print(sandwich_orders)
# print('\nWe have ran out of pastrami, sorry.')

# while sandwich_orders.__contains__('pastrami_sandwich'):
#     sandwich_orders.remove('pastrami_sandwich')

# for sandwich in sandwich_orders:
#     print('I made your ' + sandwich + '.')
#     finished_sandwiches.append(sandwich)

# print(*finished_sandwiches, sep= ', ')

results = {}
poll_active = True

while poll_active:
    name = input('What is your name?')
    vacation = input('Where would you like to spend your vacation?')

    results[name] = vacation

    repeat = input('Would you like to continue? (y/n)')
    if repeat == 'n':
        poll_active = False
    
print('------Poll results------')
for name, vacation in results.items():
    print(name.title() + ' would like to spend his/her vacation in ' + vacation + '.')





