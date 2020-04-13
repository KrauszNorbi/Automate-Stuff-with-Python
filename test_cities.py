import unittest
from city_functions import cityFunction

class CityCountryTests(unittest.TestCase):
    def test_city_country(self):
        city_function = cityFunction('kosice', 'slovakia')
        self.assertEqual(city_function, 'Kosice, Slovakia')

    def test_city_country_population(self):
        city_function_pop = cityFunction('kosice', 'slovakia', 240000)
        self.assertEqual(city_function_pop, 'Kosice, Slovakia, 240000')

unittest.main()