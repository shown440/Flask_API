from flask import Flask, request

from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from datetime import datetime

#Crypto.Cipher is for data encryption using KEY
from Crypto.Cipher import AES
#ast is for converting text to dictionary
import ast

from models.store import StoreModel
from db import db

######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################

class Store(Resource):

    # parser = reqparse.RequestParser()
    # parser.add_argument("employee_data",
    #     type=bytes,
    #     required=True,
    #     help="Field can't be empty..."
    # )

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

        # data = Store.parser.parse_args()
        # print("NOW THE DATA IS : ",data)
        data = request.get_json()
        print("#########################   ",data)

        hex_data = data["employee_data"]
        print("hex_data : ", hex_data)

        new_rnd_bytes = bytes.fromhex(hex_data)
        print("new_rnd_bytes : ", new_rnd_bytes)
        print(type(new_rnd_bytes))

        #######################################################################
        #### Decrypting data here
        #################################################
        secret_key = 'shifullah1234567'   # create new & store somewhere safe
        cipher1 = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously

        byte_decoded = cipher1.decrypt(new_rnd_bytes)
        decoded = byte_decoded.strip().decode('utf-8')
        print("Decoded text is: ",decoded)
        print(type(decoded))

        #######################################################################
        #### Converting Decrypted data into Dictionary
        ######################################################################
        text_to_dict = ast.literal_eval(decoded)
        print("###### text_to_dict : ", text_to_dict)
        print(type(text_to_dict))


        new_store = { "name":text_to_dict["name"], "designation":text_to_dict["designation"],
            "manager_id":text_to_dict["manager_id"], "date_of_birth":text_to_dict["date_of_birth"],
            "salary":text_to_dict["salary"], "commission":text_to_dict["commission"],
            "department_no":text_to_dict["department_no"]   

        }

        #print("#########################   ",new_store)
        store = StoreModel(my_store_id[0], new_store["name"], new_store["designation"], new_store["manager_id"], datetime_object.date(),
                            int(new_store["salary"]), int(new_store["commission"]), int(new_store["department_no"]))
        #print(" *********************   ",store)
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
