import sqlite3
import cx_Oracle

#from db import db

class ItemModel:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {"name":self.name, "price":self.price}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        # int=INTEGER. but if we need auto incremented id then we have to write INTEGER
        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()

        connection.close()
        if row: #this is a cls method. so it can return a object of ItemModel instead of dictionary
            return cls(*row) #, 200 # (*row <- row[0], row[1] <- #{"item":{"name":row[0], "price":row[1]}}, 200)
            #here row[0]=name and  row[1]=price of def __init__(self, name, price): ...
            #we can call (row[0], row[1] = *row) also

    def insert(self): #Here self = Object of item
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query="INSERT INTO items VALUES(?, ?)"
        cursor.execute(query, (self.name, self.price, ))

        connection.commit()
        connection.close()

    def update(self): #Here self = Object of item
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query="UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (self.price, self.name, ))

        connection.commit()
        connection.close()
