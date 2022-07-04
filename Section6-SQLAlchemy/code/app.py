from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import Authenticate, Identity
from resources.items import Item, ItemList
from resources.user import UserRegister
from datetime import timedelta
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = "maks"  # that has be secret, is used to ecrypt the JWT.
api = Api(app)  # that is just going to allow us to very easily add these resources to it.

# changing /auth to /login, we need to do this before creating the JWT instance it is important
app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False
jwt = JWT(app, Authenticate, Identity)  # /auth

# name in this <string:name> is going to name of our dictionary {'student':name}
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/Maks(<string:name>)
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
if __name__ == '__main__':
    db.init_app(app)
    app.run(port=4998, debug=True)
