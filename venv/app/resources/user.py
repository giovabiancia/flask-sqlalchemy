import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help= "this field cannot be blank"
    )
    parser.add_argument('password',
        type=str,
        required=True,
        help= "this field cannot be blank"
    )
    def post(self):
        data = UserRegister.parser.parse_args()
        # utilizza la classe User per prendere data dal db 
        if UserModel.find_by_username(data['username']):
            return {'message': "Un User con questo nome già esiste"}, 400
        # creo un nuovo utente 
        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully"}, 201
