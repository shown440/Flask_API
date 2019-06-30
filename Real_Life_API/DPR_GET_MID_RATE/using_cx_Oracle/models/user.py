import sqlite3
import cx_Oracle

#from db import db

#####################################################
##### Finding User Class ############################
#####################################################
class UserModel:

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    # ##############################################################
    # ########### SQLite3 DB part ####################################
    # ##############################################################
    @classmethod
    def find_by_username(cls, username):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2]) #user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row is not None:
            user = cls(row[0], row[1], row[2])
        else:
            user = None

        connection.close()
        return user

    ##############################################################
    ########### Orace DB part ####################################
    ##############################################################
    # @classmethod
    # def find_by_username(cls, username):
    #
    #     connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
    #     cursor = connection.cursor()
    #
    #     query = "SELECT * FROM users WHERE username=:username"
    #     result = cursor.execute(query, (username,)) #, (username,)
    #     row = result.fetchone()
    #     if row is not None:
    #         user = cls(row[0], row[1], row[2])
    #     else:
    #         user = None
    #
    #     connection.close()
    #     return user
    #
    # @classmethod
    # def find_by_id(cls, _id):
    #
    #     connection = cx_Oracle.connect("shifullah/shifullah@10.11.201.251:1521/stlbas")
    #     cursor = connection.cursor()
    #
    #     query = "SELECT * FROM users WHERE id=:id"
    #     result = cursor.execute(query, (_id,)) #, (_id,)
    #     row = result.fetchone()
    #     if row is not None:
    #         user = cls(row[0], row[1], row[2])
    #     else:
    #         user = None
    #
    #     connection.close()
    #     return user
