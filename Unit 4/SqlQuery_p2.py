import _sqlite3

def getData():
    # this establishes a connection from our python file
    # to our DB file
    connect = _sqlite3.connect("testDb_p2.db")
    
    # this variable lets us send and recieve data back and forth from
    # our file to our database
    cursor = connect.cursor()

    # the actual data we want to get from the database
    query1= "SELECT model FROM computers"
#    query2= "SELECT color FROM computers"

    # this is telling the program to fetch the query above
    cursor.execute(query1)

    # storing the fetched data inside of results
    results = cursor.fetchall()
    
    # printing out data
    print(results)
    
# getData()

def getSingleData():
    computerSearch = input("what computer are you looking please type an ID number? ")
       
    connect = _sqlite3.connect("testDb_p2.db")

    cursor = connect.cursor()

    query1= f"SELECT price FROM computers WHERE id ={computerSearch}"

    # this is telling the program to fetch the query above
    cursor.execute(query1)

    # storing the fetched data inside of results
    results = cursor.fetchone()
    
    # printing out data
    print(results)

# getSingleData()