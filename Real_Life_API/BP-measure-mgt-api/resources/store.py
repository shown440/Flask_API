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

        datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #print("######################    ", datetime_object)


        data = request.get_json()
        print("#########################   ",data)
        print("Type of data : ",type(data))

        new_cus = {"cuscode":data["cuscode"], "age":data["age"], "height":data["height"],
                "lower_bp":data["lower_bp"], "higher_bp":data["higher_bp"]}
        print("#########################   ",new_cus)

        sql = db.text('SELECT (NVL(MAX(SN),0)+1) FROM BP_INFO')
        my_store_id = db.engine.execute(sql).fetchone()
        store = StoreModel(new_cus["cuscode"], int(new_cus["age"]), int(new_cus["height"]), int(new_cus["lower_bp"]), 
                            int(new_cus["higher_bp"]), datetime_object.date(), my_store_id[0])
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
        return {"blood-pressure-details":[store.json() for store in StoreModel.query.all()]}


