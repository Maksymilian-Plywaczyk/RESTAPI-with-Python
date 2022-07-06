from flask_restful import Resource
from models.store import StoreModel
from flask_jwt import jwt_required

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_storeName(name)
        if store:
            return store.json()
        return {'message': "Store not found"}, 404

    def post(self, name):
        store = StoreModel.find_by_storeName(name=name)
        if store:
            return {'message': "That store '{}'already exists in our database.".format(name)}
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating a new store'}, 500

        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_storeName(name=name)
        if store:
            store.delete_from_db()
            return {'message': 'Store successfuly deleted'}
        else:
            return {'message': "Store '{}' doesn't exists".format(name)}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
