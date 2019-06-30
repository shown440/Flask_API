#import sqlite3
#import cx_Oracle
from datetime import datetime

from db import db

######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################

class StoreModel(db.Model):

    # __tablename__ = "STCODMAS3"
    __tablename__ = "STCODMAS"
    __table_args__ = {'extend_existing': True}

    #ROWID = db.Column(db.String, primary_key=True)
    #EMPNO = db.Column(db.Numeric(asdecimal=False), primary_key=True)
    HARCOD = db.Column(db.String(3), primary_key=True)
    SOFCOD = db.Column(db.String(6), primary_key=True)
    CODDES = db.Column(db.String(200))
    CORCOD = db.Column(db.String(20))

    AMOUNT = db.Column(db.Numeric(asdecimal=False))
    MANHRS = db.Column(db.Numeric(asdecimal=False))
    RTDNON = db.Column(db.String(1))
    OPRSTAMP = db.Column(db.String(6))

    TIMSTAMP = db.Column(db.DateTime) #Date object
    SECCOD = db.Column(db.String(8))
    ACTFLG = db.Column(db.String(1))
    SEQNUM = db.Column(db.Numeric(asdecimal=False))

    INTRT_CHGFLG = db.Column(db.String(1))
    REQUIRE_FLG = db.Column(db.String(1))
    ODRSRL = db.Column(db.Numeric(asdecimal=False))
    EFFDAT = db.Column(db.DateTime) #Date object



    #items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, HARCOD, SOFCOD, CODDES, CORCOD, AMOUNT, MANHRS, RTDNON, OPRSTAMP, TIMSTAMP, SECCOD, ACTFLG, SEQNUM, INTRT_CHGFLG, REQUIRE_FLG, ODRSRL, EFFDAT): 
        #self.ROWID = ROWID
        self.HARCOD = HARCOD
        self.SOFCOD = SOFCOD
        self.CODDES = CODDES
        self.CORCOD = CORCOD

        self.AMOUNT = AMOUNT
        self.MANHRS = MANHRS
        self.RTDNON = RTDNON
        self.OPRSTAMP = OPRSTAMP

        self.TIMSTAMP = TIMSTAMP
        self.SECCOD = SECCOD
        self.ACTFLG = ACTFLG
        self.SEQNUM = SEQNUM

        self.INTRT_CHGFLG = INTRT_CHGFLG
        self.REQUIRE_FLG = REQUIRE_FLG
        self.ODRSRL = ODRSRL
        self.EFFDAT = EFFDAT

    def json(self):
        #return {"name":self.name, "items":[item.json() for item in self.items.all()], "opening_date":str(self.opening_date.date())} #, "date":self.date #self.items.all() use that bcz we used lazy="dynamic" in line 13
        
        # Date Value Handle For GET Method
        if (self.EFFDAT == None) or (self.TIMSTAMP == None):
            my_EFFDAT = str(self.EFFDAT)
            my_TIMSTAMP = str(self.TIMSTAMP)
        else:
            my_EFFDAT = str(self.EFFDAT.date())
            my_TIMSTAMP = str(self.TIMSTAMP)
        
        return {"HARCOD":self.HARCOD,
                "SOFCOD":self.SOFCOD,
                "CODDES":self.CODDES,
                "CORCOD":self.CORCOD,

                "AMOUNT":self.AMOUNT,
                "MANHRS":self.MANHRS,
                "RTDNON":self.RTDNON,
                "OPRSTAMP":self.OPRSTAMP,

                "TIMSTAMP":my_TIMSTAMP,
                "SECCOD":self.SECCOD,
                "ACTFLG":self.ACTFLG,
                "SEQNUM":self.SEQNUM,

                "INTRT_CHGFLG":self.INTRT_CHGFLG, #,
                "REQUIRE_FLG":self.REQUIRE_FLG,
                "ODRSRL":self.ODRSRL,
                "EFFDAT":my_EFFDAT}  #.date()

    @classmethod
    def find_by_name(cls, name, date):
        # print("inside find_by_name method...")
        # print(date)
        # print(type(date))
        #datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #print("#####################",datetime_object)
        return cls.query.filter_by(HARCOD=name, SOFCOD=date).first() #alter coommand = return cls.query.filter_by(name=name).first()

    def save_to_db(self): #Here self = Object of item
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self): #Here self = Object of item
        db.session.delete(self)
        db.session.commit()


