# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.


import pandas as pd 
df = pd.read_csv("https://raw.githubusercontent.com/LambdaSchool/Sprint-Challenge--Intro-Python/master/src/cityreader/cities.csv", 
                 names=['city', 'state_name', 'county_name', 'lat', 'lng', 'population', 'density', 'timezone', 'zips']
)
df.head()

class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f'{self.name}, lat: {self.lat}, lon: {self.lon}'


import csv
cities = []

# cities = cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)