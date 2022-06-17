from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3


# Every Resource has to be a class
# Item class is CRUD APIs (create,read,update,delete)
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")

    @classmethod
    def find_by_itemName(cls, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row is not None:
            return {'item': {'name': row[0], 'price': row[1]}}

    @jwt_required()  # when the user is not log in doesn't pass JWT token we cannot get this method
    def get(self, name):  # get method is GET HTTP Method
        try:
            item = self.find_by_itemName(name)
        except:
            return {'message': 'Item not found'}, 404
        return item

    def post(self, name):
        if self.find_by_itemName(name):
            return {'message': 'Item already exists'}
        data = Item.parser.parse_args()
        # in get_json() we can put force=True and silent = True
        # request_data = request.get_json()  # if content-type is not Json and you put wrong type (not JSON) it gives
        # you an error
        # request_data is dictionary
        item = {'name': name, 'price': data['price']}
        try:
            self.insert(item)
        except:
            return {'message': 'Something goes wrong with insert'}
        return item, 201  # Tell the client that we have processed this, we have created this item and added it to
        # our database (list of item)

    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES(?,?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()

    def delete(self, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "DELETE FROM items WHERE name=?"
        if cursor.execute(query, (name,)):
            return {'message': 'item  successfully deleted'}
        connection.commit()
        connection.close()
        return {'message':'Something goes wrong with deleting item'},400

    def put(self, name):

        data = Item.parser.parse_args()
        item = self.find_by_itemName(name)
        update_item = {'name': name, 'price': data['price']}
        if item is None:
            try:
                self.insert(update_item)
            except:
                return {'message': 'Something goes wrong with inserting new item'}, 500
        else:
            try:
                self.update(update_item)
            except:
                return {'message': 'Something goes wrong with updating item'}, 500
        return update_item

    @classmethod
    def update(cls, updateItem):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (updateItem['price'], updateItem['name']))
        connection.commit()
        connection.close()


class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price': row[1]})

        connection.close()
        return {'List of items':items}