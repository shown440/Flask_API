#import sqlite3
#import cx_Oracle
from datetime import datetime

from db import db

######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################

class StoreModel(db.Model):
    __tablename__ = "stexhdtl"
    __table_args__ = {'extend_existing': True}

    ROWID = db.Column(db.String, primary_key=True)
    CURCDE = db.Column(db.String(3))
    VALDAT = db.Column(db.DateTime)
    MIDRAT = db.Column(db.Numeric(asdecimal=False))

    #items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, ROWID, CURCDE, VALDAT, MIDRAT):
        self.ROWID = ROWID
        self.CURCDE = CURCDE
        self.VALDAT = VALDAT
        self.MIDRAT = MIDRAT

    def json(self):
        #return {"name":self.name, "items":[item.json() for item in self.items.all()], "opening_date":str(self.opening_date.date())} #, "date":self.date #self.items.all() use that bcz we used lazy="dynamic" in line 13
        return {"currency_code":self.CURCDE, "validation_date":str(self.VALDAT.date()), "mid_rate":self.MIDRAT}

    @classmethod
    def find_by_name(cls, name, date):
        # print("inside find_by_name method...")
        # print(date)
        # print(type(date))
        datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #print("#####################",datetime_object)
        return cls.query.filter_by(CURCDE=name, VALDAT=datetime_object.date()).first() #alter coommand = return cls.query.filter_by(name=name).first()

    def save_to_db(self): #Here self = Object of item
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self): #Here self = Object of item
        db.session.delete(self)
        db.session.commit()


######################################################################################################
########### STLBAS DB | shifullah:shifullah@10.11.201.251:1521/stlbas ################################
######################################################################################################

# class StoreModel(db.Model):
#     __tablename__ = "stores6"
#     __table_args__ = {'extend_existing': True}
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100))
#     opening_date = db.Column(db.DateTime)
#
#     items = db.relationship("ItemModel", lazy="dynamic")
#
#     def __init__(self, id, name, opening_date):
#         self.id = id
#         self.name = name
#         self.opening_date = opening_date
#
#     def json(self):
#         return {"name":self.name, "items":[item.json() for item in self.items.all()], "opening_date":str(self.opening_date.date())} #, "date":self.date #self.items.all() use that bcz we used lazy="dynamic" in line 13
#
#     @classmethod
#     def find_by_name(cls, name, date):
#         # print("inside find_by_name method...")
#         # print(date)
#         # print(type(date))
#         datetime_object = datetime.strptime(date, '%d-%m-%Y')
#         #print("#####################",datetime_object)
#         return cls.query.filter_by(name=name, opening_date=datetime_object.date()).first() #alter coommand = return cls.query.filter_by(name=name).first()
#
#     def save_to_db(self): #Here self = Object of item
#         db.session.add(self)
#         db.session.commit()
#
#     def delete_from_db(self): #Here self = Object of item
#         db.session.delete(self)
#         db.session.commit()
