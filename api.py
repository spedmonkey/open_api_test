from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Simple API', description='A simple API')

ns = api.namespace('hello', description='Hello operations')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        '''Fetch a greeting message'''
        return {'message': 'goodbye world!'}

if __name__ == '__main__':
    app.run(debug=True)