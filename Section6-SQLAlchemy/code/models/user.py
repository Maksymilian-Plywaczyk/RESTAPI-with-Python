import sqlite3

# User class is not the resource, only RegisterUser is resource
import sqlite3
from db import db


class UserModel(
    db.Model):  # this UserModel is thing that we are going to be saving to a database, create mapping between database and these objects
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    something = 'hi something'

    def __init__(self, _id, username, password):
        # using _id because id is a Python Keyword and we don't want to use that as a variable name
        self.id = _id  # self.parameter is the instance of class attribute
        self.username = username
        self.password = password

    def save_to_db(self):
        try:
            db.session.add(self)
        except:
            db.rollback()
            raise
        else:
            db.session.commit()
    @classmethod
    # that means we are using the current class, not hard coding User class name
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
