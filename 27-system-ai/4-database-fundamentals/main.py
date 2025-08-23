# Database Fundamentals - Python example (SQLite)

import sqlite3

def create_db():
    conn = sqlite3.connect(':memory:')  # In-memory database
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    cursor.execute('''INSERT INTO users (name, age) VALUES ('Alice', 30), ('Bob', 25)''')
    conn.commit()

    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    create_db()
