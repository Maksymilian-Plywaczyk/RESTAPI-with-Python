from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = "maks" #that has be secret, is used to ecrypt the JWT.
api = Api(app)  # that is just going to allow us to very easily add these resources to it.

items = []


# Every Resource has to be a class
class Item(Resource):
    def get(self, name):  # get method is GET HTTP Method
        # None parameter provide that if the next function doesn't find an item it will just return None
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404
        # return 200 if item is not else return 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name {} already exists.".format(name)}, 400

        # in get_json() we can put force=True and silent = True
        request_data = request.get_json()  # if content-type is not Json and you put wrong type (not JSON) it gives
        # you an error
        # request_data is dictionary
        item = {'name': name, 'price': request_data['price']}
        items.append(item)
        return item, 201  # Tell the client that we have processed this, we have created this item and added it to
        # our database (list of item)


class ItemList(Resource):
    def get(self):
        return {'items': items}


# name in this <string:name> is going to name of our dictionary {'student':name}
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/Maks(<string:name>)
api.add_resource(ItemList, '/items')
if __name__ == '__main__':
    app.run(port=5000, debug=True)
