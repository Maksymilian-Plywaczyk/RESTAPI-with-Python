import sqlite3
from flask_restful import Resource, reqparse


class User:
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


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be left blank")
    parser.add_argument('password', type=str, required=True, help="This field cannot be left blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        if User.find_by_username(data['username']):
            return {'message': 'The username is already exists, put another username.'}, 400
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL,?,?)"  # NULL because id is auto incrementing
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
        return {'message': 'User created successfully.'}, 201
