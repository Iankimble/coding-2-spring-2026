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

# x = requests.post(url, jsonh= myobj)
# print(x.text)

def pokedex():
    search = input("would you like to search pokemon")
    while search == 'y':
        pokename = input("please enter a pokemon name: ")
        query = "https://pokeapi.co/api/v2/pokemon/"+pokename+"/"
        response = requests.get(query)
        # print(response)
        # print(response.json())

        if response.status_code == 200:
            data= response.json()

            filtered_data = {
                "name": data["name"],
                "height": data["height"],
                "weight": data["weight"],
                "types": data["types"],
                "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
            }
     
            print(filtered_data)
            search =input("would you like to find another pokemon? ")
        else:
            print("data not found")
            print(response.status_code)
        
pokedex()












# if response.status_code == 200:
#      data = response.json()

#      # Extracting only what you need
#      filtered_data = {
#          "name": data["name"],
#          "height": data["height"],
#          "weight": data["weight"],
#          "type":data["type"],
#          "abilities": [ability["ability"]["name"] for ability in data["abilities"]],
#          "sprites":data["sprites"]
#      }
#      print(filtered_data)
# else:
#      print(f"Error: {response.status_code}")

# # # create a pokedex