#import sqlite3
#import cx_Oracle
from datetime import datetime

from db import db

######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################

class StoreModel(db.Model):
    __tablename__ = "BP_INFO"
    __table_args__ = {'extend_existing': True}

    # ROWID = db.Column(db.String, primary_key=True)
    SN = db.Column(db.Numeric(asdecimal=False), primary_key=True)
    CUSID = db.Column(db.String())  # , primary_key=True
    AGE = db.Column(db.Numeric(2))
    HEIGHT = db.Column(db.String())

    SYS = db.Column(db.Numeric(asdecimal=False))
    DYS = db.Column(db.Numeric(asdecimal=False))
    TIMSTAMP = db.Column(db.DateTime)

    #items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, CUSID, AGE, HEIGHT, SYS, DYS, TIMSTAMP, SN):
        # self.ROWID = ROWID
        self.CUSID = CUSID
        self.AGE = AGE
        self.HEIGHT = HEIGHT

        self.SYS = SYS
        self.DYS = DYS
        self.TIMSTAMP = TIMSTAMP
        self.SN = SN


    def json(self):
        #return {"name":self.name, "items":[item.json() for item in self.items.all()], "opening_date":str(self.opening_date.date())} #, "date":self.date #self.items.all() use that bcz we used lazy="dynamic" in line 13
        return {"S/N": self.SN,
                "cuscode":self.CUSID,
                "age":int(self.AGE),
                "height":self.HEIGHT,
                "lower_bp":int(self.SYS),
                "higher_bp":int(self.DYS),
                "measued_date":str(self.TIMSTAMP) # .date()
                }

    @classmethod
    def find_by_name(cls, name, date):
        # print("inside find_by_name method...")
        # print(date)
        # print(type(date))
        datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #print("#####################",datetime_object)
        return cls.query.filter(CUSID=name, TIMSTAMP=datetime_object.date()).all() #.first() #alter coommand = return cls.query.filter_by(name=name).first()

    def save_to_db(self): #Here self = Object of item
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self): #Here self = Object of item
        db.session.delete(self)
        db.session.commit()


