from flask_restful import reqparse, abort, Api, Resource

class UserRegistrationFacebook(Resource):
    def get(self, todo_id):    
        return {'Id': todo_id}
        
    def post(self):
        return {'message': 'User registration with Facebook'}