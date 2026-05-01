# 1. bring in the sql lite module to get access to all the sql methods (functions) to work with our database.
import sqlite3

# 2. we need to establish an actual database file using the connect method. 
connect= sqlite3.connect('myDb_3.db')

# 3. create a object that will be sent to the new database
cursor=  connect.cursor()

# 4. we need to create a schema (structure) for our data. 
cursor.execute('''
               CREATE TABLE gameSales(
               id INTERGER PRIMARY KEY,
               name TEXT, 
               platform TEXT,
               developer TEXT,
               price INTEGER,
               genre TEXT,
               totalSales INTEGER
               )
               ''')

# 5. we can now create our first databas object
# cursor.execute('''
#                INSERT INTO gameSales(name, platform, developer, price, genre, totalSales)
#                VALUES('Crimson Desert','PS5', 'pearl abyss', 70, 'action/ adventure', 500000000 )
#                ''')

# cursor.execute('''
#                INSERT INTO gameSales(name, platform, developer, price, genre, totalSales)
#                VALUES('Smash Bros.','Switch 2', 'Nintendo', 80, 'Fighting', 700000000)
#                ''')

cursor.execute('''
               UPDATE gameSales
               SET  = ""
               WHERE  = ""
               ''')

# 6. once we have a new data object, we can commit this to our database
connect.commit()
connect.close()

