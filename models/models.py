from flask_sqlalchemy import SQLAlchemy
from flask import Flask
db = SQLAlchemy()
 
class EmployeePersonalDetail(db.Model):
    __tablename__ = 'employee_details'
    empid = db.Column(db.Integer, db.Sequence(__tablename__ + '_empid_seq') ,primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    personaladdress = db.Column(db.String(200), nullable=False)
    contactdetails = db.Column(db.Integer)
    serviceaddress = db.relationship('ServiceLocation')
    def __init__(self,firstname,lastname,personaladdress,contactdetails):
        self.firstname = firstname
        self.lastname = lastname
        self.personaladdress = personaladdress
        self.contactdetails = contactdetails
        

class ServiceLocation(db.Model):
    __tablename__ = 'service_locations'
    city = db.Column(db.String(120), nullable=False)
    serviceaddress = db.Column(db.String(500))
    person_id = db.Column(db.Integer, db.ForeignKey('employee_details.empid'),primary_key=True)

    def __init__(self,city, serviceaddress,person_id):
        self.person_id = person_id
        self.city = city
        self.serviceaddress = serviceaddress
