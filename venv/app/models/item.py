
from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80))
    #2 decimali
    price = db.Column(db.Float(precision=2))
#creo una relazione tra tabelle  ( la tabella items e quella store)
# id in store è una PrimaryKey
# store_id in items è una Foreignkey
# perchè ha un valore id identico a quello di un altra tabella 
    store_id= db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')


    def __init__ (self, name, price, store_id):
        self.name= name
        self.price= price
        self.store_id= store_id
    
    def json(self):
        # ritorno una rappresentazione json del model 
        return {'name':self.name, 'price':self.price}
    

    @classmethod
    def find_by_name(cls, name):
        # fai una query nel ItemModel cerca il primo nome
        return ItemModel.query.filter_by(name=name).first()


    

    def save_to_db(self):
        #inserisco un oggetto nel db
        db.session.add(self)
        db.session.commit()
    

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        