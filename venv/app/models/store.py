
from db import db

class StoreModel(db.Model):

    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(80))
# dico a sqla che ho una relazione con item 
# di tipo uno a molti !  1 store  + items
    items = db.relationship("ItemModel", lazy= "dynamic")
    


    def __init__ (self, name):
        self.name= name
        
        
    
    def json(self):
        # ritorno una rappresentazione json del model 
        return {'name':self.name, 'items': [item.json() for item in self.items.all()]}
    

    @classmethod
    def find_by_name(cls, name):
        # fai una query nel ItemModel cerca il primo nome
        return StoreModel.query.filter_by(name=name).first()


    def save_to_db(self):
        #inserisco un oggetto nel db
        db.session.add(self)
        db.session.commit()
    

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
