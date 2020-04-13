def cityFunction(city_name, country_name, population = ''):
    if population:
        getCityCountry = city_name.title() + ', ' + country_name.title() + ', ' + str(population)
    else:
        getCityCountry = city_name.title() + ', ' + country_name.title()

    return getCityCountry

print(cityFunction('kosice', 'slovakia', 240000))
print(cityFunction('roskilde', 'denmark'))

class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount = 5000):
        self.raise_amount = raise_amount
        if raise_amount:
            raised_salary = int(self.annual_salary) + self.raise_amount
        else:
            raised_salary = int(self.annual_salary) + raise_amount
        return raised_salary

norbi = Employee('Norbi', 'K', 2000)
print(norbi.give_raise())
print(norbi.give_raise(1000))