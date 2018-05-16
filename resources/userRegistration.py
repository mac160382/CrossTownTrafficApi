from flask import jsonify, request, abort, make_response
from flask_restful import reqparse, Resource, fields, marshal_with
from models.user import User

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('username')
parser.add_argument('password')

user_fields = {
    'id': fields.Integer,
    'username': fields.String   
}

class UserRegistration(Resource):   
    @marshal_with(user_fields)
    def get(self):   
        args = parser.parse_args()
        id = args['id']
        result = User.query.filter_by(id = id).first()
        return result

    def post(self):
        args = parser.parse_args()
        id = args['id']
        username = args['username']
        password = args['password']
        user = User.query.filter_by(id = id).first()

        user.username = username
        user.password = password 
        user.save()
        
        return {'message': 'User registration'}
    
    