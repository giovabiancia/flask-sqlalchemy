import sqlite3
from db import db

# un model è la rappresentazione interna di un entità: quello che salvi in db
#  il back end
# una risorsa è una rappresentazione esterna di un entità: quello che vede l' utente chiamando l' api
#  il front end

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id= _id).first()
