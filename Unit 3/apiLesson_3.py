import json

# API = Application Programming Interface

# are methods (functions) that allow computer programs to share
# data between each other over the internet/ a network. 

import requests 
# modules are files of code (objects with methods and parameters) 
# with prewritten code to help us program

countryData = requests.get("https://restcountries.com/v3.1/all?fields=name,capital,currencies")

# JSON - JavaScript Object Notation
# this a object structured for computers and people to easily read 
# sort data. 

# print(countryData.json())

southAmericaCountry = requests.get('https://restcountries.com/v3.1/name/guyana?fields=population,capital,{demonym}')
denonymGuyana = requests.get('https://restcountries.com/v3.1/demonym/guyana')

print(southAmericaCountry.json())
print(denonymGuyana.json())