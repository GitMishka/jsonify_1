import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')

c.execute("INSERT INTO data (name, age) VALUES (?, ?)", ("John Doe", 25))
c.execute("INSERT INTO data (name, age) VALUES (?, ?)", ("Jane Smith", 30))

conn.commit()
conn.close()
