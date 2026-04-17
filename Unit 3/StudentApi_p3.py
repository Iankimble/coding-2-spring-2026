# Use ONE of the following APIs to pull and access the data. 
import requests
import json

# Dog API -> return at least 3 types of dogs images
# https://dog.ceo/dog-api/

# Cat API -> return at least 3 types of cats
# https://http.cat/

# Rick and Morty API -> return at least 3 rick and morty characters
# https://rickandmortyapi.com/

url ='https://rickandmortyapi.com/api/character/1'
res = requests.get(url)
status = res.status_code
#print(res.status_code)
#print(res.json())

if status == 200:
    data = res.json()

    filterData = {
        "name": data["name"],
        "status":data["status"],
        "image":data["image"],
    }

    print(filterData)
else:
    print("Something went wrong")
    print(res.status_code)

url ='https://rickandmortyapi.com/api/character/2'
res = requests.get(url)
status = res.status_code
#print(res.status_code)
#print(res.json())

if status == 200:
    data = res.json()

    filterData = {
        "name": data["name"],
        "status":data["status"],
        "image":data["image"],
    }

    print(filterData)
else:
    print("Something went wrong")
    print(res.status_code)

url ='https://rickandmortyapi.com/api/character/10'
res = requests.get(url)
status = res.status_code
#print(res.status_code)
#print(res.json())

if status == 200:
    data = res.json()

    filterData = {
        "name": data["name"],
        "status":data["status"],
        "image":data["image"],
    }

    print(filterData)
else:
    print("Something went wrong")
    print(res.status_code)