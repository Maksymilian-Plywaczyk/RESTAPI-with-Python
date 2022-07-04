from db import db


class ItemModel(db.Model):  # this ItemModel is thing that we are going to be saving to a database
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    itemname = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, itemname, price):
        self.itemname = itemname
        self.price = price

    def json(self):
        return {'name': self.itemname, 'price': self.price}

    @classmethod
    def find_by_itemName(cls, name):
        return cls.query.filter_by(itemname=name).first()  # Do the same like SELECT * FROM items WHERE name=name LIMIT 1

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
