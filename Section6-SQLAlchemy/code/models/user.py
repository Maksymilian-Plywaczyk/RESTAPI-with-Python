import sqlite3

# User class is not the resource, only RegisterUser is resource
class UserModel:
    def __init__(self, _id, username, password):
        # using _id because id is a Python Keyword and we don't want to use that as a variable name
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    # that means we are using the current class, not hard coding User class name
    def find_by_username(cls, username):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # part WHERE username=? is the part of filtering the results. It is going to limit the selection to be only
        # this rows to the username matches the parameter
        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()  # gives us first row out of the result set
        if row is not None:
            user = cls(row[0], row[1], row[2])  # create the user from that row
        else:
            user = None
            # we don't have to commit, because we didn't add any data
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        # part WHERE username=? is the part of filtering the results. It is going to limit the selection to be only
        # this rows to the username matches the parameter
        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()  # gives us first row out of the result set
        if row is None:
            user = None
        else:
            user = cls(row[0], row[1], row[2])  # create the user from that row
        # we don't have to commit, because we didn't add any data
        connection.close()
        return user
