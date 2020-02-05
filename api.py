from flask import Flask
from flask_restful import Resource, Api
import feedTools

app = Flask(__name__)
api = Api(app)


class feedRetrieve(Resource):
    def get(self):
        return feedTools.getFeed()


api.add_resource(feedRetrieve, '/')

if __name__ == '__main__':
    app.run(debug=True)
