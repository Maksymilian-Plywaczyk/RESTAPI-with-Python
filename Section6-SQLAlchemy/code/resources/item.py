from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


# Every Resource has to be a class
# Item class is CRUD APIs (create,read,update,delete)
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="This field cannot be left blank")

    @jwt_required()  # when the user is not log in doesn't pass JWT token we cannot get this method
    def get(self, name):  # get method is GET HTTP Method
        try:
            item = ItemModel.find_by_itemName(name)
            return item.json()
        except:
            return {'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_itemName(name):
            return {'message': 'Item already exists'}
        data = Item.parser.parse_args()
        # in get_json() we can put force=True and silent = True
        # request_data = request.get_json()  # if content-type is not Json and you put wrong type (not JSON) it gives
        # you an error
        # request_data is dictionary
        item = ItemModel(name, data['price'])
        try:
            item.save_to_db()
        except:
            return {'message': 'Something goes wrong with insert'}
        return item.json(), 201  # Tell the client that we have processed this, we have created this item and added it to
        # our database (list of item)

    def delete(self, name):
        item = ItemModel.find_by_itemName(name)
        if item:
            item.delete_from_db()
        return {'message': 'Item deleted'}

    def put(self, name):

        data = Item.parser.parse_args()
        item = ItemModel.find_by_itemName(name)

        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()


class ItemList(Resource):
    def get(self):
        ItemList = ItemModel.query.all()
        # example with lambda function
        # return {'items':list(map(lambda x: x.json(),ItemModel.query.all()))}
        return {'items': [item.json() for item in ItemList]}
