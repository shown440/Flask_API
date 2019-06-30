import sqlite3
import cx_Oracle

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

#################################################################################
#################################################################################
##### ORACLE DB Item(Resource) ##################################################
#################################################################################
################################################################################

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price",
        type=float,
        required=True,
        help="Price Field can't be empty..."
    )
    # parser.add_argument("date",
    #     type=str,
    #     required=True,
    #     help="Date Field can't be empty..."
    # )

    #@jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item
        return {"message":"{} is not found".format(name)}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {"Message":"{} is exist. No need to create it again.".format(name)}, 400

        data = Item.parser.parse_args()
        print("#####", data)
        item = {"name":name, "price":data["price"]} #, "date":data["date"]
        print("*****", item)
        ItemModel.insert(item)
        # try:
        #     ItemModel.insert(item)
        # except:
        #     return {"message":"{} insertion failed.".format(name)}, 500
        return item, 201


    def delete(self, name):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query="DELETE FROM REST_ITEMS WHERE name=:name"
        cursor.execute(query, (name, ))

        connection.commit()
        connection.close()
        return {"message" : "Item {} deleted successfully".format(name)}

    def put(self, name):
        data = Item.parser.parse_args()

        item_exist = ItemModel.find_by_name(name)
        update_item = {"name":name, "price":data["price"]}
        if item_exist is None: # is None
            try:
                ItemModel.insert(update_item)
            except:
                return {"message":"Updating error. Please see the update and put method."}, 500
        else:
            try:
                ItemModel.update(update_item)
            except:
                return {"message":"Updating error. Please see the update and put method."}, 500
        return update_item

class ItemList(Resource):
    #@jwt_required()
    def get(self):
        items = []

        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()
        query="SELECT * FROM REST_ITEMS"
        result = cursor.execute(query)

        for row in result:
            items.append({"name":row[0], "price":row[1]})   #, "date":str(row[2])

        connection.close()
        return {"items" : items}


###############################################################################
###############################################################################
##### SQLite3 DB Item(Resource) ###############################################
###############################################################################
###############################################################################

# class Item(Resource):
#     parser = reqparse.RequestParser()
#     parser.add_argument("price",
#         type=float,
#         required=True,
#         help="Field can't be empty..."
#     )
#
#     @jwt_required()
#     def get(self, name):
#         item = ItemModel.find_by_name(name) # here we pass the name into ItemModel calss of item.py in models packageand it return value as object
#         if item:
#             return item.json()
#         return {"message":"{} is not found".format(name)}, 404
#
#     @jwt_required()
#     def post(self, name):
#         if ItemModel.find_by_name(name): # here we pass the name into ItemModel calss of item.py in models package and it return value as object
#             return {"Message":"{} is exist. No need to create it again.".format(name)}, 400
#
#         data = Item.parser.parse_args()
#         #print("####################", data)
#         item = ItemModel(name, data["price"]) #ItemModel(name, data["price"]) <- {"name":name, "price":data["price"]}
#         #because this is not a dictionary. Its a ItemModel object now.
#
#         try:
#             item.insert() #now we directly insert item because item is now ItemModel class object. #ItemModel.insert(item)
#         except:
#             return {"message":"{} insertion failed.".format(name)}, 500
#         return item.json(), 201
#
#     @jwt_required()
#     def delete(self, name):
#         connection = sqlite3.connect("data.db")
#         cursor = connection.cursor()
#
#         query="DELETE FROM items WHERE name=?"
#         cursor.execute(query, (name, ))
#
#         connection.commit()
#         connection.close()
#
#         return {"message" : "Item {} deleted successfully".format(name)}
#
#     def put(self, name):
#
#         data = Item.parser.parse_args()
#
#         item_exist = ItemModel.find_by_name(name) # here we pass the name into ItemModel calss of item.py in models package and it return value as object
#
#         update_item = ItemModel(name, data["price"]) #ItemModel(name, data["price"]) <- {"name":name, "price":data["price"]}
#         #because this is not a dictionary. Its a ItemModel object now.
#         if item_exist is None: # is None
#             try:
#                 update_item.insert() #ItemModel.insert(update_item)
#             except:
#                 return {"message":"Updating error. Please see the update and put method."}, 500
#         else:
#             try:
#                 update_item.update() #ItemModel.update(update_item)
#                 # because update_item=new item, its not in db, and item_exist is in db, so for update we have to use update_item.update()
#                 # if we use item_exist.update() then it will return update item, but it will unable to update in DB.
#                 # so be careful about this. This is coding concept not logical concept.
#             except:
#                 return {"message":"Updating error. Please see the update and put method."}, 500
#         return update_item.json()
#
#
# class ItemList(Resource):
#     #@jwt_required()
#     def get(self):
#         items = []
#
#         connection = sqlite3.connect("data.db")
#         cursor = connection.cursor()
#         query="SELECT * FROM items"
#         result = cursor.execute(query)
#
#         for row in result:
#             items.append({"name":row[0], "price":row[1]})
#
#         connection.close()
#         return {"items" : items}
