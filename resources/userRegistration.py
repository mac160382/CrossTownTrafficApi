from flask import jsonify, request, abort, make_response
from flask_restful import reqparse, Resource, fields, marshal_with
from models.user import User

user_fields = {
    'id': fields.Integer,
    'username': fields.String   
}

class UserRegistrationParams():
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id')
        self.parser.add_argument('username')
        self.parser.add_argument('password')

    def getId(self):
        return self.parser.parse_args()['id']
    
    def getUsername(self):
        return self.parser.parse_args()['username']

    def getPassword(self):
        return self.parser.parse_args()['password']

class UserRegistration(Resource):   
    def __init__(self):
        self.parameters = UserRegistrationParams()

    @marshal_with(user_fields)
    def get(self):                   
        return User.query.filter_by(id = self.parameters.getId()).first()        

    def post(self):               
        user = User.query.filter_by(id = self.parameters.getId()).first()
        user.username = self.parameters.getUsername()
        user.password = self.parameters.getPassword()
        user.save()        
        return {'message': 'User registration'}

    def put(self):        
        user = User(self.parameters.getUsername(), self.parameters.getPassword())        
        user.save()
        
        return {'message': 'put'}
    
    

    
    