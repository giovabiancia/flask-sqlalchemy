from flask import Flask, render_template, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key = 'jose'
api = Api(app)

# sql alchemy crea le tabelle
@app.before_first_request
def create_table():
    db.create_all()

jwt = JWT(app, authenticate, identity)


api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(UserRegister, "/register")

@app.route('/')
def index():
    return render_template('ajax1.html')

# python assegna il nome main al file che esegue
# quindi se magari eseguiamo un altro file all interno del progetto
#non vogliamo magari che questo faccia partire l' app, per questo
# si usa la condizione if
if __name__ == '__main__':
# importiamo sqlalchemy qui per evitare cirular import
    from db import db
    db.init_app(app)
    app.run(host='127.0.0.1', port=8000, debug=True)
