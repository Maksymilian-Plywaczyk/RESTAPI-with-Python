from db import db


class ItemModel(db.Model):  # this ItemModel is thing that we are going to be saving to a database
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    itemName = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # Putting the foreign key on the child (item) table referencing the parent.relationship() (store)
    # In this case we have a relationship one-to-many it means one store(parent) can have many items(children)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, itemName, price,store_id):
        self.itemName = itemName
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.itemName, 'price': self.price}

    @classmethod
    def find_by_itemName(cls, name):
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
