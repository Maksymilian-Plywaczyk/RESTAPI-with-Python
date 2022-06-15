from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)  # that is just going to allow us to very easily add these resources to it.


# Every Resource has to be a class
class Student(Resource):
    def get(self, name):  # get method is GET HTTP Method
        return {'student': name}


# name in this <string:name> is going to name of our dictionary {'student':name}
api.add_resource(Student, '/student/<string:name>')  # http://127.0.0.1:5000/student/Maks(<string:name>)

if __name__ == '__main__':
    app.run(port=5000)
