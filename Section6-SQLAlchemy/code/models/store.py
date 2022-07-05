from db import db


class StoreModel(db.Model):  # this ItemModel is thing that we are going to be saving to a database
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    storename = db.Column(db.String(80))

    items = db.relationship('ItemModel',
                            lazy='dynamic')  # lazy = 'dynamic' change our item variable from list o query object

    def __init__(self, itemname, price):
        self.storename = itemname
        self.price = price

    def json(self):
        return {'name': self.storename, 'items': [items.json() for items in self.items.all()]}

    @classmethod
    def find_by_storeName(cls, name):
        return cls.query.filter_by(
            itemname=name).first()  # Do the same like SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self):
        try:
            db.session.add(self)  # This method save item to database and update it
        except:
            db.session.rollback()
            raise
        else:
            db.session.commit()

    def delete_from_db(self):
        try:
            db.session.delete(self)
        except:
            db.session.rollback()
            raise
        else:
            db.session.commit()
