import requests
import sqlite3

# 1. Fetch the data from the API
url = "https://rickandmortyapi.com/api/character/1,183"
response = requests.get(url)
characters = response.json()

# 2. Connect to (or create) a local SQLite database
conn = sqlite3.connect('rick_and_morty.db')
cursor = conn.cursor()

# 3. Create a table structured for the character data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS characters (
        id INTEGER PRIMARY KEY,
        name TEXT,
        status TEXT,
        species TEXT,
        gender TEXT,
        origin_name TEXT
    )
''')

# 4. Loop through the API results and insert them
for char in characters:
    cursor.execute('''
        INSERT OR REPLACE INTO characters (id, name, status, species, gender, origin_name)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        char['id'], 
        char['name'], 
        char['status'], 
        char['species'], 
        char['gender'], 
        char['origin']['name'] # Nested data: origin is a dict
    ))

# 5. Save (commit) and close
conn.commit()
conn.close()

print("Data successfully loaded into rick_and_morty.db")