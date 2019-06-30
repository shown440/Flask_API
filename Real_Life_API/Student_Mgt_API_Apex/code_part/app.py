import cx_Oracle

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "ShifullaAhmedKhan"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

class Item(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument("ID",
    #     type=int,
    #     required=True,
    #     help="Field can't be empty..."
    # )

    @jwt_required()
    def get(self, name):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "SELECT * FROM STUDENT_INFO WHERE NAME=:name"
        result = cursor.execute(query, (name,)) #.fetchone()
        row = result.fetchone()
        #print(result)
        connection.close()
        if row:
            return {"student":{"Name":row[1], "ID":row[0], "Roll":row[2],
                    "Class":row[3], "Mobile":row[4], "Address":row[5],
                    "Father Name":row[6], "Mother Name":row[7], "Created by":row[8], "Entry Time":str(row[9])}}, 200 #,"Entry Time":str(row[9])
        else:
            return{"Message":"Student not found... "}, 404

    @jwt_required()
    def post(self, name):
        #if self.get(name):
            #return {"Message":"{} is exist. No need to create it again.".format(name)}, 400
        #print("Post Method .... Start...")
        #parser = reqparse.RequestParser()
        #data = parser.parse_args()
        data = request.get_json()
        #print(data)
        #print("Post Method .... After data variable")
        item = {"id":data["ID"], "name":name, "roll":data["Roll"], "class":data["Class"], "mobile":data["Mobile"],
                "address":data["Address"], "father_name":data["Father_Name"], "mother_name":data["Mother_Name"],
                "created_by":data["Created_by"], "entry_time":data["Entry_Time"]}
        # print("Post Method .... After item dictionary")
        # print(item)
        # print("##########")
        # print(type(int(item["id"])))

        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "INSERT INTO STUDENT_INFO VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)"
        cursor.execute(query, (int(item["id"]), item["name"], int(item["roll"]), int(item["class"]), int(item["mobile"]),
                                item["address"], item["father_name"], item["mother_name"],
                                item["created_by"], None, None)) #, item["entry_time"]
        connection.commit()
        connection.close()
        return item, 201
        # if aded_item.len > 0:
        #     return "Data added successfully..."
        # else:
        #     return "Data Rejected !"

    @jwt_required()
    def delete(self, name):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "DELETE FROM STUDENT_INFO WHERE name=:name"
        cursor.execute(query, (name,))
        connection.commit()
        connection.close()
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
    @jwt_required()
    def get(self):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "SELECT * FROM STUDENT_INFO"
        result = cursor.execute(query)
        students = []
        for row in result:
            students.append({"Name":row[1], "ID":row[0], "Roll":row[2],
                    "Class":row[3], "Mobile":row[4], "Address":row[5],
                    "Father Name":row[6], "Mother Name":row[7], "Created by":row[8], "Entry Time":str(row[9])})
        #print(students)
        connection.close()
        return {"Students" : students} #str(items)

api.add_resource(Item, "/item/<string:name>") ### http://127.0.0.1:5000/student/Shifullah
api.add_resource(ItemList, "/items/")


if __name__ == '__main__':
    app.debug=True
    app.run()
