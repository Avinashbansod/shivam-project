import sys
from flask import render_template, redirect, url_for, request, abort
from models.models import EmployeePersonalDetail, ServiceLocation
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def index():
    return render_template('management-console.html')


def searchGuards():
    employees = db.session.query(EmployeePersonalDetail.firstname, EmployeePersonalDetail.lastname,
                                 EmployeePersonalDetail.personaladdress, EmployeePersonalDetail.contactdetails,
                                 ServiceLocation.city, ServiceLocation.serviceaddress) \
                                .join(ServiceLocation) \
                                .filter(EmployeePersonalDetail.empid == ServiceLocation.person_id).all()

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
    pass