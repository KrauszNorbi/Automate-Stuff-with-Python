import unittest
from city_functions import cityFunction, Employee


class CityCountryTests(unittest.TestCase):
    '''Tests for methods from city_functions.py'''
    def setUp(self):
        '''Create an object of Employee class '''
        self.norbi = Employee('Norbi', 'K', 2000)

    def test_city_country(self):
        '''Test cityFunction method with 2 parameters'''
        city_function = cityFunction('kosice', 'slovakia')
        self.assertEqual(city_function, 'Kosice, Slovakia')

    def test_city_country_population(self):
        '''Test cityFunction method with 3 parameters'''
        city_function_pop = cityFunction('kosice', 'slovakia', 240000)
        self.assertEqual(city_function_pop, 'Kosice, Slovakia, 240000')

    def test_give_default_raise(self):
        '''Test give_raise method with default value'''
        self.assertEqual(self.norbi.give_raise(), 7000)

    def test_give_custom_raise(self):
        '''Test give_raise method with custom value'''
        self.assertEqual(self.norbi.give_raise(1000), 3000)

unittest.main()