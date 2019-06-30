import cx_Oracle
from datetime import datetime

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity

app = Flask(__name__)
app.secret_key = "Shifulla_Ahmed_Khan"
api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

class RetriveItem(Resource):
    #@jwt_required()
    def get(self, name, e_dob):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "SELECT * FROM EMPLOYEE WHERE ENAME=:name and DATE_OF_BIRTH=:e_dob"
        result = cursor.execute(query, (name,e_dob,)) #.fetchone()
        row = result.fetchone()
        #print(result)
        connection.close()
        if row:
            return {"Employee":{"Name":row[1], "ID":row[0], "Designation":row[2],
                    "Manager_id":row[3], "Date_of_birth":str(row[4]), "Salary":row[5],
                    "Commission":row[6], "Department_no":row[7]}}, 200 #,"Entry Time":str(row[9])
        else:
            return{"Message":"Employee not found... "}, 404


class Item(Resource):

    #@jwt_required()
    def post(self, name):

        data = request.get_json()

        item = {"id":data["ID"], "name":name, "designation":data["Designation"], "manager_id":data["Manager_id"],
                "date_of_birth":data["Date_of_birth"], "salary":data["Salary"], "commission":data["Commission"],
                "department_no":data["Department_no"]}

        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "INSERT INTO EMPLOYEE VALUES(:1, :2, :3, :4, :5, :6, :7, :8)"
        cursor.execute(query, (int(item["id"]), item["name"], item["designation"], int(item["manager_id"]),
                                item["date_of_birth"], int(item["salary"]), int(item["commission"]), int(item["department_no"])))
        connection.commit()
        connection.close()
        return item, 201

class DeleteItem(Resource):
    #@jwt_required()
    def delete(self, e_id):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "DELETE FROM EMPLOYEE WHERE EMPNO=:e_id"
        cursor.execute(query, (e_id,))
        connection.commit()
        connection.close()
        return {"message" : "Item {} deleted successfully".format(e_id)}


class ItemList(Resource):
    #@jwt_required()
    def get(self):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query = "SELECT * FROM EMPLOYEE"
        result = cursor.execute(query)
        students = []
        for row in result:
            students.append({"Name":row[1], "ID":row[0], "Designation":row[2],
                    "Manager_id":row[3], "Date_of_birth":row[4], "Salary":row[5],
                    "Commission":row[6], "Department_no":row[7]})
        #print(students)
        connection.close()
        return {"Employees" : students} #str(items)

api.add_resource(RetriveItem, "/employee/Employee_name=<string:name>&DOB=<string:e_dob>")
api.add_resource(Item, "/employee/Employee_name=<string:name>") ### http://127.0.0.1:5000/student/Shifullah
api.add_resource(DeleteItem, "/employee/Employee_id=<int:e_id>")
api.add_resource(ItemList, "/employees/")


if __name__ == '__main__':
    app.debug=True
    app.run()
