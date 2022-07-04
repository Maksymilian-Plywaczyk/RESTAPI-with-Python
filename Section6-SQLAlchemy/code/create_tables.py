import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()  # it allows you to start things and select things

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"

cursor.execute(create_table)
create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, itemname text, price real )"

cursor.execute(create_table)
connection.commit()
connection.close()
