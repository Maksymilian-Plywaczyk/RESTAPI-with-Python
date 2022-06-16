from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import Authenticate, Identity
from items import Item,ItemList
from user import UserRegister
app = Flask(__name__)
app.secret_key = "maks"  # that has be secret, is used to ecrypt the JWT.
api = Api(app)  # that is just going to allow us to very easily add these resources to it.

items = []
jwt = JWT(app, Authenticate, Identity)  # /auth

# name in this <string:name> is going to name of our dictionary {'student':name}
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/Maks(<string:name>)
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')
if __name__ == '__main__':
    app.run(port=4999, debug=True)
