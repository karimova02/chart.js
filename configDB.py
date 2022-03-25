import sqlite3
connection = sqlite3.connect("mydatabase.db")
cursor= connection.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS fruits(
type TEXT,
price INTEGER,
color TEXT
    )
""")
cursor.execute("""
INSERT INTO Fruits VALUES
("Apple", 23000 , "Green"),
("Banana", 34000 , "Yellow"),
("Kiwi", 50000,  "Green"),
("Tangerine", 34000, "Orange"),
("Pineapple", 60000, "Yellow")
""")
cursor.execute("""SELECT * FROM fruits
WHERE color = "Yellow" OR price = 34000
""")
cursor.execute("""
SELECT * FROM fruits
WHERE Price <= 40000
""")
print(cursor.fetchall())

