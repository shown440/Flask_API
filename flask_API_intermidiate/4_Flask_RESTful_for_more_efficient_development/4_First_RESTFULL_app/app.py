from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# stores = [
#     {
#         "name":"My wonderful Store",
#         "items":[
#             {
#                 "name":"my item",
#                 "price": 19.99
#             }
#         ]
#     }
# ]

class Student(Resource):
    def get(self, name):
        return {"student" : name}

api.add_resource(Student, "/student/<string:name>") ### http://127.0.0.1:5000/student/Shifullah


if __name__ == '__main__':
    app.debug=True
    app.run()
