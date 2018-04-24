from flask_restful import reqparse, Resource

parser = reqparse.RequestParser()
parser.add_argument('email', required=True, help="Email can not be blank")
parser.add_argument('password', required=True, help="Email can not be blank")


class UserRegistration(Resource):
    def get(self):
        args = parser.parse_args()
        return {'Id': args['email']}

    def post(self):
        return {'message': 'User registration'}