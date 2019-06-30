from flask import Flask, request

from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from datetime import datetime

#ast is for converting text to dictionary
import ast

from models.store import StoreModel
from db import db

######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################

class Store(Resource):
    #@jwt_required()
    def get(self, name, date):
        store = StoreModel.find_by_name(name, date)
        if store:
            return store.json()
        return {"message":"{} store is not found".format(name)}, 404

    def post(self, name, date):

        store = StoreModel.find_by_name(name, date)
        #print("##################      BEFORE CHECKING THE NAME...")
        if store:
            return {"message":"{} store is already exist.".format(name)}, 400

        #print("##################      AFTER CHECKING THE NAME...")
        sql = db.text('SELECT (NVL(MAX(EMPNO),0)+1) FROM EMP')
        my_store_id = db.engine.execute(sql).fetchone()
        #print("######################    ", my_store_id)

        #datetime_object = datetime.strptime(date, '%d-%m-%Y')
        datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #print("######################    ", datetime_object)

        ################################################################################################
        # IF we use encrypted data then we have to use this part

            # my_data = request.get_json()
            # print("#########################   ",my_data)

            # #######################################################################
            # #### Converting Decrypted data into Dictionary
            # ######################################################################
            # data = ast.literal_eval(my_data)
            # print("###### text_to_dict : ", data)
            # print(type(data))
        ################################################################################################

        data = request.get_json()
        print("#########################   ",data)
        print("Type of data : ",type(data))

        new_store = {"name":data["name"], "designation":data["designation"], "manager_id":data["manager_id"],
                "date_of_birth":data["date_of_birth"], "salary":data["salary"], "commission":data["commission"],
                "department_no":data["department_no"]}
        #print("#########################   ",new_store)
        store = StoreModel(my_store_id[0], new_store["name"], new_store["designation"], new_store["manager_id"], datetime_object.date(),
                            int(new_store["salary"]), int(new_store["commission"]), int(new_store["department_no"]))
        print(" *********************   ",store)
        try:
            store.save_to_db()
        except Exception as e:
            return {"message":"Unexpected error occured in Stroe insertion. please see the post method of store Resource."}, 500
        return store.json(), 201

    def delete(self, name, date):
        store = StoreModel.find_by_name(name, date)
        if store:
            store.delete_from_db()
            return {"message":"{} store is deleted successfully.".format(name)}
        else:
            return {"message":"employee {} is not found.".format(name)}


class StoreList(Resource):
    #@jwt_required()
    def get(self):
        return {"store":[store.json() for store in StoreModel.query.all()]}


######################################################################################################
########### STLBAS DB | shifullah:shifullah@10.11.201.251:1521/stlbas ################################
######################################################################################################

# class Store(Resource):
#     def get(self, name, date):
#         store = StoreModel.find_by_name(name, date)
#         if store:
#             return store.json()
#         return {"message":"{} store is not found".format(name)}, 404
#
#     def post(self, name, date):
#         store = StoreModel.find_by_name(name, date)
#         if store:
#             return {"message":"{} store is already exist.".format(name)}, 400
#
#         sql = db.text('SELECT (NVL(MAX(ID),0)+1) FROM STORES6')
#         my_store_id = db.engine.execute(sql).fetchone()
#
#         datetime_object = datetime.strptime(date, '%d-%m-%Y')
#
#         store = StoreModel(my_store_id[0], name, datetime_object.date())
#         try:
#             store.save_to_db()
#         except Exception as e:
#             return {"message":"Unexpected error occured in Stroe insertion. please see the post method of store Resource."}, 500
#         return store.json(), 201
#
#     def delete(self, name):
#         store = StoreModel.find_by_name(name)
#         if store:
#             store.delete_from_db()
#             return {"message":"{} store is deleted successfully.".format(name)}
#         else:
#             return {"message":"{} store unable to delete.".format(name)}
#
#
# class StoreList(Resource):
#     def get(self):
#         return {"store":[store.json() for store in StoreModel.query.all()]}
