def cityFunction(city_name, country_name, population = ''):
    if population:
        getCityCountry = city_name.title() + ', ' + country_name.title() + ', ' + str(population)
    else:
        getCityCountry = city_name.title() + ', ' + country_name.title()

    return getCityCountry

