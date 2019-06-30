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
    def get(self): #, name, date

        data = request.get_json()
        print("#########################   ",data)

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

        new_store = { "HARCOD":text_to_dict["HARCOD"], "SOFCOD":text_to_dict["SOFCOD"]}

        name = new_store["HARCOD"]
        date = new_store["SOFCOD"]


        store = StoreModel.find_by_name(name, date)
        
        if store:
            return store.json()
        return {"message":"{} store is not found".format(name)}, 404

    def post(self):   #, name, date
        
        #print("##################      AFTER CHECKING THE NAME...")
        sql = db.text('SELECT (NVL(MAX(EMPNO),0)+1) FROM EMP')
        my_store_id = db.engine.execute(sql).fetchone()
        #print("######################    ", my_store_id)

        #datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #datetime_object = datetime.strptime(date, '%d-%m-%Y')
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


        new_store = { "HARCOD":text_to_dict["HARCOD"], "SOFCOD":text_to_dict["SOFCOD"],
            "CODDES":text_to_dict["CODDES"], "CORCOD":text_to_dict["CORCOD"],

            "AMOUNT":text_to_dict["AMOUNT"], "MANHRS":text_to_dict["MANHRS"],
            "RTDNON":text_to_dict["RTDNON"], "OPRSTAMP":text_to_dict["OPRSTAMP"],

            "TIMSTAMP":text_to_dict["TIMSTAMP"], "SECCOD":text_to_dict["SECCOD"],
            "ACTFLG":text_to_dict["ACTFLG"], "SEQNUM":text_to_dict["SEQNUM"],

            "INTRT_CHGFLG":text_to_dict["INTRT_CHGFLG"], "REQUIRE_FLG":text_to_dict["REQUIRE_FLG"],
            "ODRSRL":text_to_dict["ODRSRL"], "EFFDAT":text_to_dict["EFFDAT"]
        }
        print("######################### NEW Store is:  ",new_store)

        name = new_store["HARCOD"]
        date = new_store["SOFCOD"]

        store = StoreModel.find_by_name(name, date)
        #print("##################      BEFORE CHECKING THE NAME...")
        if store:
            return {"message":"{} store is already exist.".format(name)}, 400
        #return {"message":"{} store is not found.".format(name)}, 400
        print("##########################################################")
        print("new_store_TIMSTAMP: ", new_store["TIMSTAMP"])
        print(type(new_store["TIMSTAMP"]))
        print("new_store_EFFDAT: ", new_store["EFFDAT"])
        print(type(new_store["EFFDAT"]))

        ################################################################
        # Date Value Handle For POST Method
        ################################################################
        # if (new_store["EFFDAT"] == "None") or (new_store["TIMSTAMP"] == "None"):
        #     my_TIMSTAMP = None
        #     my_EFFDAT = None
        # else:
        TIMSTAMP_datetime_obj = datetime.strptime(new_store["TIMSTAMP"], '%d-%m-%Y') #'%d-%m-%Y'
        my_TIMSTAMP = TIMSTAMP_datetime_obj.date()
        EFFDAT_datetime_obj = datetime.strptime(new_store["EFFDAT"], '%d-%m-%Y')
        my_EFFDAT = EFFDAT_datetime_obj.date()
        # print(type(EFFDAT_datetime_obj), EFFDAT_datetime_obj)
        
        ###################################################################
        # Integer value Handle
        ###################################################################
        if (isinstance(new_store["AMOUNT"], int) == False) or (isinstance(new_store["MANHRS"], int) == False) or (isinstance(new_store["SEQNUM"], int) == False) or (isinstance(new_store["ODRSRL"], int) == False) :
            my_AMOUNT = None 
            my_MANHRS = None
            my_SEQNUM = None
            my_ODRSRL = None  
        else:
            my_AMOUNT = int(new_store["AMOUNT"])
            my_MANHRS = int(new_store["MANHRS"])
            my_SEQNUM = int(new_store["SEQNUM"])
            my_ODRSRL = int(new_store["ODRSRL"])

        store = StoreModel(new_store["HARCOD"], new_store["SOFCOD"],new_store["CODDES"], new_store["CORCOD"],
                            my_AMOUNT, int(new_store["MANHRS"]), new_store["RTDNON"], new_store["OPRSTAMP"], 
                            my_TIMSTAMP, new_store["SECCOD"], new_store["ACTFLG"], int(new_store["SEQNUM"]), 
                            new_store["INTRT_CHGFLG"], new_store["REQUIRE_FLG"], int(new_store["ODRSRL"]), my_EFFDAT)
        print(" ********************* Final Store is: ",store)
        #return {"message":"{} store save to final store.".format(name)}, 400
        try:
            store.save_to_db()
        except Exception as e:
            return {"message":"Unexpected error occured in Stroe insertion. please see the post method of store Resource."}, 500
        return store.json(), 201

    def delete(self): #, name, date

        data = request.get_json()
        print("#########################   ",data)

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

        new_store = { "HARCOD":text_to_dict["HARCOD"], "SOFCOD":text_to_dict["SOFCOD"]}

        name = new_store["HARCOD"]
        date = new_store["SOFCOD"]

        store = StoreModel.find_by_name(name, date)
        if store:
            store.delete_from_db()
            return {"message":"{} store is deleted successfully.".format(name)}
        else:
            return {"message":"{} is not found.".format(name)}


class StoreList(Resource):
    #@jwt_required()
    def get(self):
        return {"stcodmas":[store.json() for store in StoreModel.query.all()]}
