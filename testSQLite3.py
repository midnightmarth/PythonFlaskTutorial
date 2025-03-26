import sqlite3
 
# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('SomeOtherDB.db')
cursor = conn.cursor()
 
# Create the 'people' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
''')
 
# Insert random data into the 'people' table
people_data = [
    ('John', 'Doe', 28),
    ('Jane', 'Smith', 34),
    ('Michael', 'Johnson', 45),
    ('Emily', 'Davis', 22),
    ('Daniel', 'Brown', 30),
    ('Sophia', 'Wilson', 27),
    ('James', 'Jones', 40),
    ('Olivia', 'Garcia', 25),
    ('Matthew', 'Martinez', 35),
    ('Emma', 'Anderson', 29)
]
 
cursor.executemany('''
INSERT INTO people (first_name, last_name, age) VALUES (?, ?, ?)
''', people_data)
 
# Commit the transaction
conn.commit()
 
# Select all data from the 'people' table to verify the inserts
cursor.execute('SELECT * FROM people')
rows = cursor.fetchall()
for row in rows:
    print(row)
 
# Close the connection
conn.close()