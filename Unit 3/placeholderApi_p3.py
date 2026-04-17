import requests

query = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(query)

# print(response)
# print(response.json())

# url = 'https://jsonplaceholder.typicode.com/posts'
# myobj = { "title": 'testing api',
#          "body": 'this is a test post for my social media app',
#          "userId": 139209302
#          }

# x = requests.post(url, json = myobj)
# print(x.text)

query = "https://pokeapi.co/api/v2/evolution-chain/52/"
response = requests.get(query)

print(response)
print(response.json())

