from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


# Every Resource has to be a class
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")

    @jwt_required()  # when the user is not log in doesn't pass JWT token we cannot get this method
    def get(self, name):  # get method is GET HTTP Method
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row is not None:
            return {'item': {'name': row[0], 'price': row[1]}}
        return {'message': 'Item not found'}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "An item with name {} already exists.".format(name)}, 400
        data = Item.parser.parse_args()
        # in get_json() we can put force=True and silent = True
        # request_data = request.get_json()  # if content-type is not Json and you put wrong type (not JSON) it gives
        # you an error
        # request_data is dictionary
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201  # Tell the client that we have processed this, we have created this item and added it to
        # our database (list of item)

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items), None)
        return {'message': 'item deleted'}

    def put(self, name):

        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}
