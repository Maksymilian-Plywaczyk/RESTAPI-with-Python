from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.item import Item, ItemList
from resources.user import UserRegister
from datetime import timedelta
from resources.store import Store, StoreList
from db import db
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('MY DATA BASE FROM HEROKO ', 'sqlite:///data.db')
app.secret_key = "maks"  # that has be secret, is used to ecrypt the JWT.
api = Api(app)  # that is just going to allow us to very easily add these resources to it.

# changing /auth to /login, we need to do this before creating the JWT instance it is important
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    # create all tables in our Database for us
    db.create_all()


jwt = JWT(app, authenticate, identity)  # /auth but in our case /login

# name in this <string:name> is going to name of our dictionary {'student':name}
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/Maks(<string:name>)
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=4998, debug=True)
