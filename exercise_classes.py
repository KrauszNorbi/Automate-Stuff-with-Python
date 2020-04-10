class Restaurant():
    # Superclass defines restaurant name, its cuisine type and contains methods to open the restaurant and show the number of servings
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the name of the restaurant and the cuisine type"""
        print('\nThe restaurant name is ' + self.restaurant_name.title() + '.' )
        print('The cuisine type is ' + self.cuisine_type + '.')
        print(self.restaurant_name.title() + ' has served ' + str(self.number_served) + ' guests so far.')

    def open_restaurant(self):
        '''Opens the restaurant'''
        print(self.restaurant_name.title() + ' is now OPEN.')

    def set_number_served(self, serve):
        self.number_served = serve

    def increment_number_served(self, serves):
        self.number_served += serves


restaurant1 = Restaurant('The Rubicon', 'exotic food')
restaurant2 = Restaurant('The Echelon', 'sushi')
restaurant3 = Restaurant('Mythra', 'indian food')

restaurant1.set_number_served(5)
restaurant1.increment_number_served(15)

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
print('\n')

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()


class User():
    def __init__(self, first_name, last_name, user_name, password, premium):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
        self.premium = premium
        self.login_attempts = 0

    def describe_user(self):
        # prints a summary of user's information
        print('\nFirst Name: ' + self.first_name.title() + ', Last Name: ' + self.last_name.title() + ', Username: ' + self.user_name + ', Password: ' + self.password + ', Premium: ' + str(self.premium))

    def greet_user(self):
        # prints a personalized welcome message
        print('Hello ' + self.user_name + ', have a nice coding.')
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

norbi = User('Norbert', 'Krausz', 'Vain', '*******', True)
#peasant = User('Peasant', 'McPeasant', 'n00b', '12345', False)

norbi.describe_user(), norbi.greet_user()
norbi.increment_login_attempts()
norbi.increment_login_attempts()
norbi.increment_login_attempts()
print(norbi.login_attempts)
norbi.reset_login_attempts()
print(norbi.login_attempts)

#peasant.describe_user(), peasant.greet_user()


class IceCreamStand(Restaurant):
    # Inheritance from Restaurant class
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'oreo', 'banana', 'cream', 'strawberry']

    def icecream_flavours(self):
        print(self.flavours)

myStand = IceCreamStand('IscreamYouscream', 'icecream')
myStand.icecream_flavours()


class Admin(User):
    # Subclass of User
    def __init__(self, first_name, last_name, user_name, password, premium):
        super().__init__(first_name, last_name, user_name, password, premium)
        self.privileges = Privileges()
    

class Privileges():
    # stores a list of privileges
    def __init__(self):
        super().__init__()
        self.privileges = ['can add posts', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        for i in self.privileges:
            print('- ' + i)

superAdmin = Admin('Norbi', 'K', 'Vain', '123', True)
superAdmin.privileges.show_privileges()

