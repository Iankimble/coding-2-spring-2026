# Use ONE of the following APIs to pull and access the data. 
import requests
import json

# Dog API -> return at least 3 types of dogs images
# https://dog.ceo/dog-api/
url_1= 'https://dog.ceo/api/breed/hound/images'
data = requests.get(url_1)
#print(data.json())

if data.status_code == 200:
    data= ["message",[0]]
    #print(data)

# Cat API -> return at least 3 types of cats
# https://http.cat/

req= '200'
url_3= 'https://http.cat/'+req
cat= requests.get(url_3)
print(cat.status_code)
print(cat)


# # Rick and Morty API -> return at least 3 rick and morty characters
# # https://rickandmortyapi.com/

# url_2 = 'https://rickandmortyapi.com/api/character/4'
# res = requests.get(url_2)
# #print(res.status_code)

# if res.status_code == 200:
#     charData = res.json()
#     filtData= {
#         "name": charData["name"],
#         "gender":charData["gender"],
#         "image":charData["image"]
#     }
#     #print(filtData)
# else:
#     #print("something went wrong...")
#     #print(res.status_code)

# #url_2 = 'https://rickandmortyapi.com/api/character/32'
# #res = requests.get(url_2)
# print(res.status_code)

# if res.status_code == 200:
#     charData = res.json()
#     filtData= {
#         "name": charData["name"],
#         "gender":charData["gender"],
#         "image":charData["image"]
#     }
#     print(filtData)
# else:
#     print("something went wrong...")
#     print(res.status_code)

# url_2 = 'https://rickandmortyapi.com/api/character/60'
# res = requests.get(url_2)
# print(res.status_code)

# if res.status_code == 200:
#     charData = res.json()
#     filtData= {
#         "name": charData["name"],
#         "gender":charData["gender"],
#         "image":charData["image"]
#     }
#     print(filtData)
# else:
#     print("something went wrong...")
#     print(res.status_code)