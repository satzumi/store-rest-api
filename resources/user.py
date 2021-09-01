from flask_restful import Resource,reqparse
from models.user import UserModel
        
class UserRegister(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'username',
            required=True,
            help='This field cannot be left blank'
        )
        parser.add_argument(
            'password',
            required=True,
            help='This field cannot be left blank'
        )        
        
        data = parser.parse_args()
        
        user = UserModel.find_by_username(data['username'])
        if user:
            return {'message': '{} already exists.Try another name'.format(data['name'])} 
        
        user = UserModel(**data)
        user.save_to_db()
        
        return {'message': 'user created successfully'},201
        