# imports all the methods we will need to send/ receieve data from DB
import sqlite3

# just function
def getAllData():
    # setting up the connection to our db (the road)
    connect= sqlite3.connect('myDb_3.db')
    
    # setting up or vehicle to send/ recieve data 
    # to/from the DB (the vehicle)
    cursor=  connect.cursor()

    # the data we want to get
    # SELECT = our selection 
    query = "SELECT name FROM gameSales"

    # turns the vehicle on to get the data
    cursor.execute(query)
    
    # tells cursor to fetch/ get ALL data
    results = cursor.fetchall()

    # shows our results in terminal
    print(results)

# getAllData()

# just function
def get1data():
    connect= sqlite3.connect('myDb_3.db')
    
    cursor=  connect.cursor()

    query = "SELECT name FROM gameSales WHERE developer = 'Bethesda'"

    cursor.execute(query)
    
    results = cursor.fetchone()

    print(results)

# get1data()

# create a function that will delete an object from the database
# use w3schools as reference for sql queries 

def deleteData():
    connect= sqlite3.connect('myDb_3.db')

    cursor=  connect.cursor()

    query = "DELETE FROM gameSales WHERE name = 'Star Field'"

    cursor.execute(query)
    connect.commit()
    
deleteData()