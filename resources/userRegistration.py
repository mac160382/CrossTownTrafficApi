from flask import jsonify, request, abort, make_response
from flask_restful import reqparse, Resource
from models.user import User

parser = reqparse.RequestParser()
parser.add_argument('user_id', required=True, help="Email can not be blank")
#parser.add_argument('password', required=True, help="Email can not be blank")

class UserRegistration(Resource):
    def get(self):        
        args = parser.parse_args()
        #u = User(args['username'], 'pwd')
        #u.save()
        user_id = args['user_id']
        result = User.get_all()
        #res = request.get_json()
        print(result)
        return {'Id': user_id} #jsonify(User.get_all()) # 

    def post(self):
        return {'message': 'User registration'}