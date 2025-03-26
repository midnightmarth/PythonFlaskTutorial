import mysql.connector
import sqlite3

myDatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="halolord8",
    database="firstdatabase"
)

mycursor = myDatabase.cursor()

mycursor.execute("SELECT * FROM people")
data = mycursor.fetchall()

print(data[1])

myDatabase.commit()

print(data)

conn = sqlite3.connect("example.db")
cursor = conn.cursor() 
cursor.execute('''DROP TABLE policy''')
sql = ''' CREATE TABLE policy (
    id INTEGER PRIMARY KEY,
    PolicyPrompt TEXT NOT NULL
    )'''
    # isUserPolicy BOOL NOT NULL, 
    # isActive BOOL NOT NULL 
cursor.execute(sql)
conn.commit()