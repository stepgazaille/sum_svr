from flask import Flask
from flask_restful import Api
from resources.lead3 import Lead3


app = Flask(__name__)
api = Api(app)
api.add_resource(Lead3, '/lead3')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
