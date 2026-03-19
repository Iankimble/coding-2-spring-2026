import json

# API - Application Programming Interface
# Allows computers to share data between devices 
# via the internet.

# functions that let us share data back and forth over
# the internet

import requests # moudules --> 
# is object with methods and properties that
# were already written/ prewitten for us

#data = requests.get('https://restcountries.com/v3.1/name/peru')
#print(data)
#print(data.json())

# Use the API to find data on 1 African Country, 
# 1 South American Country, and 1 Asian Country. You should have 3
# variables returning data for each type of country.

africanCountry = requests.get('https://restcountries.com/v3.1/name/nigeria?fields=name,capital,currencies')
asianCountry = requests.get('https://restcountries.com/v3.1/name/south korea')
sAmericanCountry = requests.get('https://restcountries.com/v3.1/name/columbia')

print(africanCountry.json())
#print(africanCountry.json())








# Capital 
# Demonyn
# population