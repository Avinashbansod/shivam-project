from crypt import methods
import sys
from unittest import result
from flask import render_template, redirect, url_for, request, abort
from models.models import EmployeePersonalDetail, ServiceLocation
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    return render_template('management-console.html')


def populateallrecords():
    records = db.session.query(EmployeePersonalDetail.firstname, EmployeePersonalDetail.lastname,
                                 EmployeePersonalDetail.personaladdress, EmployeePersonalDetail.contactdetails,
                                 ServiceLocation.city, ServiceLocation.serviceaddress) \
                                .join(ServiceLocation) \
                                .filter(EmployeePersonalDetail.empid == ServiceLocation.person_id).all()
    return records                            

def searchGuards():
    employees = populateallrecords()
    return render_template('search-guards.html', employees=employees)


def renderCreateGuardForm():
    return render_template('guard-registration-form.html')


def createGuard():
    data = request.form
    isdetailsnotok = False
    for key in data:
        if (data.get(key) == None) or (data.get(key) == ''):
            isdetailsnotok = True

    if isdetailsnotok:
        return render_template('guard-registration-form.html', status=f"Required fields are missing!")
    else:
        employee = EmployeePersonalDetail(data.get('firstname'), data.get('lastname'),
                                          data.get('residentialaddress'), data.get('phonenumber'))
        db.session.add(employee)
        db.session.commit()
        person_id = employee.empid
        service_location = ServiceLocation(
            data.get('servingcity'), data.get('servingaddress'), person_id)
        db.session.add(service_location)
        db.session.commit()
        return render_template('guard-registration-form.html', status=f"{data.get('firstname')} {data.get('lastname')} is added to the database")


def updateGuard():
    all_locations = db.session.query(ServiceLocation).with_entities(ServiceLocation.city).distinct().all()
    all_city = []
    for item in all_locations:
       for city in item: 
         all_city.append(city)
    
    records = populateallrecords() 
    if(request.method == 'GET'):
     return render_template('update-guard-details.html',employees = records,cities = all_city)

    else:
      data = request.form
      isdetailsnotok = False
      for key in data:
        if (data.get(key) == None) or (data.get(key) == ''):
            isdetailsnotok = True
      if isdetailsnotok:
        return render_template('update-guard-details.html', cities = all_city, employees = records,status=f"Required fields are missing!")
      else:
        empid = db.session.query(EmployeePersonalDetail).\
                filter(EmployeePersonalDetail.firstname == data.get('firstname'),EmployeePersonalDetail.lastname == data.get('lastname')).\
                with_entities(EmployeePersonalDetail.empid).first()
        if(empid == None):
          return render_template('update-guard-details.html', cities = all_city, employees = records,status=f"No such user exist!")          
        
        db.session.query(ServiceLocation).\
        filter(ServiceLocation.person_id == empid[0]).\
        update({ ServiceLocation.city: data.get('servingcity'), ServiceLocation.serviceaddress: data.get('servingaddress') })
        db.session.commit()
        return redirect('/management/search-guards')

def deleteGuard():
    data = request.form
    records = populateallrecords()
    if(request.method == 'GET'):
     return render_template('delete-guard.html',employees = records)
    else:
      empid = db.session.query(EmployeePersonalDetail).\
                filter(EmployeePersonalDetail.firstname == data.get('firstname'),EmployeePersonalDetail.lastname == data.get('lastname')).\
                with_entities(EmployeePersonalDetail.empid).first()
    
      if(empid == None):
        return render_template('delete-guard.html', employees = records,status=f"No such user exist!")
     
      db.session.query(ServiceLocation).filter(ServiceLocation.person_id == empid[0]).delete()
      db.session.query(EmployeePersonalDetail).filter(EmployeePersonalDetail.empid == empid[0]).delete()
      db.session.commit()
      return redirect('/management/search-guards')
