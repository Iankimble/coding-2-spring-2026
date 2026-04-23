import sqlite3

connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS test(
    id INTEGER PRIMARY KEY,
    studentName TEXT,
    studentGrade INTEGER
)''')

connection.commit()
print('db initialized.')

# name = "Ian"
# grade = 10

# cursor.execute("INSERT INTO test (studentName, studentGrade) VALUES (?,?)", (name, grade))
# connection.commit()

# cursor.execute("SELECT * FROM test")
# results = cursor.fetchall()

# for row in results:
#     print(f"ID: {row[0]}, Item: {row[1]}, Qty: {row[2]}")


def add_student(name, grade):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    
    # Passing variables into the query
    cursor.execute("INSERT INTO test (studentName, studentGrade) VALUES (?, ?)", (name, grade))
    
    connection.commit()
    connection.close()
    print(f"Record created for {name}.")

add_student("Alex", 95)

# 4/0Aci98E_8FIYmCx6ivImovkW4AD8WiyHBPkE_3ZzY-78vynU4m6v0XZbIL0pg7rs_n2kavA