#import sqlite3
#import cx_Oracle
from datetime import datetime

from db import db

######################################################################################################
########### STLBAS DB | stlbas:stlbas@10.11.201.251:1521/stlbas ######################################
######################################################################################################

class StoreModel(db.Model):
    __tablename__ = "EMP"
    __table_args__ = {'extend_existing': True}

    #ROWID = db.Column(db.String, primary_key=True)
    EMPNO = db.Column(db.Numeric(asdecimal=False), primary_key=True)
    ENAME = db.Column(db.String(10))
    JOB = db.Column(db.String(9))
    MGR = db.Column(db.Numeric(asdecimal=False))

    DATE_OF_BIRTH = db.Column(db.DateTime)
    SAL = db.Column(db.Numeric(asdecimal=False))
    COMM = db.Column(db.Numeric(asdecimal=False))
    DEPTNO = db.Column(db.Numeric(asdecimal=False))

    #items = db.relationship("ItemModel", lazy="dynamic")

    def __init__(self, EMPNO, ENAME, JOB, MGR, DATE_OF_BIRTH, SAL, COMM, DEPTNO):
        #self.ROWID = ROWID
        self.EMPNO = EMPNO
        self.ENAME = ENAME
        self.JOB = JOB
        self.MGR = MGR
        self.DATE_OF_BIRTH = DATE_OF_BIRTH
        self.SAL = SAL
        self.COMM = COMM
        self.DEPTNO = DEPTNO

    def json(self):
        #return {"name":self.name, "items":[item.json() for item in self.items.all()], "opening_date":str(self.opening_date.date())} #, "date":self.date #self.items.all() use that bcz we used lazy="dynamic" in line 13
        return {"id":self.EMPNO,
                "name":self.ENAME,
                "designation":self.JOB,
                "manager_id":self.MGR,
                "date_of_birth":str(self.DATE_OF_BIRTH.date()),
                "salary":self.SAL,
                "commission":self.COMM,
                "department_no":self.DEPTNO}

    @classmethod
    def find_by_name(cls, name, date):
        # print("inside find_by_name method...")
        # print(date)
        # print(type(date))
        datetime_object = datetime.strptime(date, '%d-%m-%Y')
        #print("#####################",datetime_object)
        return cls.query.filter_by(ENAME=name, DATE_OF_BIRTH=datetime_object.date()).first() #alter coommand = return cls.query.filter_by(name=name).first()

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
