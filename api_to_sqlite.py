import requests
import sqlite3
api_URL = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_URL)
data = response.json()
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")
for item in data[:10]:
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
                   (item['title'], "Unknown Author", 2024))

conn.commit()
cursor.execute("SELECT * FROM books")
rows = cursor.fetchall()

for row in rows:
    print(row)
conn.close()
