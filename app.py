from flask import Flask
from flask_restful import Api
from resources.userRegistration import UserRegistration
from resources.userRegistrationFacebook import UserRegistrationFacebook

app = Flask(__name__)
api = Api(app)

api.add_resource(UserRegistration, '/UserRegistration', '/registration/app')
api.add_resource(UserRegistrationFacebook, '/UserRegistrationFacebook', '/registration/facebook/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)