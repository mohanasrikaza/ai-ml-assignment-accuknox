
import sqlite3
import csv
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT
)
""")
with open("users.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header
     for row in reader:
        cursor.execute("INSERT INTO users VALUES (?, ?)", (row[0], row[1]))
conn.commit()
conn.close()


