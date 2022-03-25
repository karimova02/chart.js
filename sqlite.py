import sqlite3

connection = sqlite3.connect("mydatabase.db")

cursor= connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS person(
    name TEXT, 
    surname TEXT, 
    age INTEGER
)
""")
cursor.execute("""
INSERT INTO person VALUES
("Abdulaziz", "Karimov", 25),
("Sanjar", "Abdullayev", 22)
""")

cursor.execute ("SELECT * FROM person")

print(cursor.fetchall())

