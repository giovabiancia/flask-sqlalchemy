from flask import jsonify
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel




class Item(Resource):
    #cambia solo alcuni elementi non tuutti
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type= float,
        required=True,
        help= " questo campo è richiesto"
        )
    parser.add_argument('store_id',
        type= int,
        required=True,
        help= " ogni item deve avere uno store_id"
        )
    
    # @jwt_required()
    def get(self, name):
        
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        else:
            return{'message': 'item not found'}, 404

        


    def post(self, name):
        
        if ItemModel.find_by_name(name):
            return {'message': "an item whit name '{}' already exist".format(name)}, 400
        # ottengo il file json da js
        #data = request.get_json()
        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])
        #items.append(item)
        try:
            item.save_to_db()
        except:
            return {'message': "An error occurred"}, 500
    
        return item.json(), 201 

    
    
    def delete(self,name):
        item= ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return{ 'message': 'Item deleted'}

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)
        

        if item is None:
            item= ItemModel(name, data['price'], data['store_id'])

        else:
            item.price= data['price']
        
        item.save_to_db()

        return item.json()
    
    
        



class ItemList(Resource):
    def get(self):

        return {'items': [item.json() for item in ItemModel.query.all()]}