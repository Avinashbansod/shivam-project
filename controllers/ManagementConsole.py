import sys
from flask import render_template, redirect, url_for, request, abort
from models.models import EmployeePersonalDetail , ServiceLocation
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def index():
    return render_template('management-console.html')

def search_Guards():
    employees = db.session.query(EmployeePersonalDetail.firstname, EmployeePersonalDetail.lastname,
                   EmployeePersonalDetail.personaladdress, EmployeePersonalDetail.contactdetails, 
                   ServiceLocation.city, ServiceLocation.serviceaddress) \
                   .join(ServiceLocation) \
                   .filter(EmployeePersonalDetail.empid == ServiceLocation.person_id).all()
    
    return render_template('search-guards.html',employees=employees)