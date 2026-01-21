def  city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"
city_country1 = city_country('santiago', 'chile')
print(city_country1)
city_country2 = city_country('paris', 'france')
print(city_country2)