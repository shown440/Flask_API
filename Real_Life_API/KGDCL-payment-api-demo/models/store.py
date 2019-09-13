#import sqlite3
#import cx_Oracle
from datetime import datetime

from db import db

######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################

class StoreModel(db.Model):
    __tablename__ = "KGDCL_API"
    __table_args__ = {'extend_existing': True}

    # ROWID = db.Column(db.String, primary_key=True)
    CUSCODE = db.Column(db.String(), primary_key=True)  # , primary_key=True
    NAME = db.Column(db.String())
    MOBILE = db.Column(db.String())
    BILL_MONTH = db.Column(db.String())
    BILL_YEAR = db.Column(db.String())
    
    GASS_BILL = db.Column(db.Numeric())
    SURCHARGE = db.Column(db.Numeric())
    METER_CHARGE = db.Column(db.Numeric())
    TOTAL_BILL = db.Column(db.Numeric())

    LAST_PAYMENT_DATE = db.Column(db.DateTime)

    #items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, CUSCODE, NAME, MOBILE, BILL_MONTH, BILL_YEAR, GASS_BILL, SURCHARGE, METER_CHARGE, TOTAL_BILL, LAST_PAYMENT_DATE):
        # self.ROWID = ROWID
        self.CUSCODE = CUSCODE
        self.NAME = NAME
        self.MOBILE = MOBILE
        self.BILL_MONTH = BILL_MONTH
        self.BILL_YEAR = BILL_YEAR

        self.GASS_BILL = GASS_BILL
        self.SURCHARGE = SURCHARGE
        self.METER_CHARGE = METER_CHARGE
        self.TOTAL_BILL = TOTAL_BILL

        self.LAST_PAYMENT_DATE = LAST_PAYMENT_DATE


    def json(self):
        #return {"name":self.name, "items":[item.json() for item in self.items.all()], "opening_date":str(self.opening_date.date())} #, "date":self.date #self.items.all() use that bcz we used lazy="dynamic" in line 13
        return {"Customer Name":self.NAME,
                "Bill Month":self.BILL_MONTH,
                "Bill Year":self.BILL_YEAR,
                "Gas Bill":int(self.GASS_BILL),
                "Surcharge":int(self.SURCHARGE),
                "Meter Charge":int(self.METER_CHARGE),
                "Total Bill Amount":int(self.TOTAL_BILL),
                "Last Payment Date":str(self.LAST_PAYMENT_DATE.date())
                }

    @classmethod
    def find_by_name(cls, name, date):
        # print("inside find_by_name method...")
        # print(date)
        # print(type(date))
        # datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #print("#####################",datetime_object)
        return cls.query.filter_by(CUSCODE=name, MOBILE=date).first() #alter coommand = return cls.query.filter_by(name=name).first()

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
