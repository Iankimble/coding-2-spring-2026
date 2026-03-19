import requests

# Coordinate for New York City (Look up philly lat/long)
lat = 40.71
lon = -74.01

# no "apikey="
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

response = requests.get(url)
data = response.json()

print(data)
