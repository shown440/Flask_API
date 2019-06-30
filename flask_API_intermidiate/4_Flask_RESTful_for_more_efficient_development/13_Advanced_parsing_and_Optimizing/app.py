from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "jose"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

items = [
        {
            "name": "Saucer",
            "price": "999999"
        },
        {
            "name": "Star Ship",
            "price": "999999"
        }
]

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="Field can't be empty..."
    )

    #@jwt_required()
    def get(self, name):
        item = next(filter(lambda x:x["name"]==name, items), None)
        print(item)
        return {"item":item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x:x["name"]==name, items), None) is not None:
            return {"Message":"{} is exist. No need to create it again.".format(name)}, 400

        data = Item.parser.parse_args()

        item = {"name":name, "price":data["price"]}
        aded_item = items.append(item)
        return item, 201
        # if aded_item.len > 0:
        #     return "Data added successfully..."
        # else:
        #     return "Data Rejected !"

    def delete(self, name):
        global items
        items = list(filter(lambda x: x["name"] != name, items))
        #print("MY Items : ", items)
        return {"message" : "Item {} deleted successfully".format(name)}

    def put(self, name):

        data = Item.parser.parse_args()

        item = next(filter(lambda x: x["name"]==name, items), None)
        if item is None:
            item = {"name":name, "price":data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item

class ItemList(Resource):
    #@jwt_required()
    def get(self):
        return {"items" : items}

api.add_resource(Item, "/item/<string:name>") ### http://127.0.0.1:5000/student/Shifullah
api.add_resource(ItemList, "/items/")


if __name__ == '__main__':
    app.debug=True
    app.run()
