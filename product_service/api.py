from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class products(Resource):
    def get(self):
        return {'products': ['books', 'foods', 'balls']}

api.add_resource(products, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
