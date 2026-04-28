# 1. import sqlite module to be able to use a database
import sqlite3

# 2. the connect method creates/starts our database
connect = sqlite3.connect()

# 3. the cursor variable creates a new object that lets us send objects to our database
cursor = connect.cursor()

# 4. we need to create a schema (structure) for our data
cursor.execute('''
    CREATE TABLE computers(
    id INTEGER PRIMARY KEY,
    model TEXT,
    color TEXT,
    hasWebcam BOOL,
    memory INTEGER,
    price INTEGER                                
               )''')

cursor.execute('''
    INSERT INTO computers(model, color, hasWebcam, memory, price)
    VALUES('apple m4', 'blue', True, 8, 1500)''')

connect.commit()
connect.close()