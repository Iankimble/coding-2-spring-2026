import requests 

url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(url)

# print(response)
# print(response.json()) 

url = 'https://bored-api.appbrewery.com/random'
# response = requests.get(url)

# print(response)
# print(response.json()) 

endpoint = 'pokemon'

url = 'https://pokeapi.co/api/v2/generation/3/'
response = requests.get(url)

print(response.json())
