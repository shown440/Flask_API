import sqlite3
import cx_Oracle

#from db import db

###############################################################################
###############################################################################
##### ORACLE DB Item(Resource) ################################################
###############################################################################
###############################################################################

class ItemModel:

    def __init__(self, name, price):
        self.name = name
        self.price = price
        #self.date = date #datetime.strptime(date, '%d/%b/%Y')

    def json(self):
        return {"name":self.name, "price":self.price} #, "date":self.date

    @classmethod
    def find_by_name(cls, name):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        # int=INTEGER. but if we need auto incremented id then we have to write INTEGER
        query = "SELECT * FROM REST_ITEMS WHERE name=:name"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()
        if row:
            return {"item":{"name":row[0], "price":row[1]}}, 200  #, "date":str(row[2])

    def insert(self):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        print("@@@@@@@@@@@@@@@@")
        query="INSERT INTO REST_ITEMS VALUES(:1, :2)" #, :3,
        cursor.execute(query, (self.name, self.price, )) #self.date,

        connection.commit()
        connection.close()

    def update(self):
        connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
        cursor = connection.cursor()

        query="UPDATE REST_ITEMS SET price=:1 WHERE name=:2"
        cursor.execute(query, (self.price, self.name, ))

        connection.commit()
        connection.close()

###############################################################################
###############################################################################
##### SQLite3 DB Item(Resource) ###############################################
###############################################################################
###############################################################################

# class ItemModel:
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def json(self):
#         return {"name":self.name, "price":self.price}
#
#     @classmethod
#     def find_by_name(cls, name):
#         connection = sqlite3.connect("data.db")
#         cursor = connection.cursor()
#
#         # int=INTEGER. but if we need auto incremented id then we have to write INTEGER
#         query = "SELECT * FROM items WHERE name=?"
#         result = cursor.execute(query, (name,))
#         row = result.fetchone()
#
#         connection.close()
#         if row: #this is a cls method. so it can return a object of ItemModel instead of dictionary
#             return cls(*row) #, 200 # (*row <- row[0], row[1] <- #{"item":{"name":row[0], "price":row[1]}}, 200)
#             #here row[0]=name and  row[1]=price of def __init__(self, name, price): ...
#             #we can call (row[0], row[1] = *row) also
#
#     def insert(self): #Here self = Object of item
#         connection = sqlite3.connect("data.db")
#         cursor = connection.cursor()
#
#         query="INSERT INTO items VALUES(?, ?)"
#         cursor.execute(query, (self.name, self.price, ))
#
#         connection.commit()
#         connection.close()
#
#     def update(self): #Here self = Object of item
#         connection = sqlite3.connect("data.db")
#         cursor = connection.cursor()
#
#         query="UPDATE items SET price=? WHERE name=?"
#         cursor.execute(query, (self.price, self.name, ))
#
#         connection.commit()
#         connection.close()
