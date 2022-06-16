# file show have we interact with SQLite
import sqlite3

connection = sqlite3.connect('code/data.db')

cursor = connection.cursor()
# CREATE TABLE is SQL command
createTable = "CREATE TABLE users (id int, username text, password text)"

cursor.execute(createTable)
user = (1, 'maks', 'asdf')
# INSERT INTO is SQL command
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [(2, 'alex', 'qwer'), (3, 'mark', 'abcd')]
cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"
# select_query_id = "SELECT id FROM users" it is going to select only column of id
for row in cursor.execute(select_query):
    print(row)
connection.commit()
connection.close()
