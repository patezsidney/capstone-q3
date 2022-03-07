import json

from flask import request, jsonify
from http import HTTPStatus
from secrets import token_urlsafe
from sqlalchemy import exc
from sqlalchemy.orm.session import Session

from app.configs.database import db

from app.models.employee_model import EmployeeModel

def sigin():
    data = request.get_json()

    try:
        employee: EmployeeModel = EmployeeModel.query.filter_by(employee_id=data['employee_id']).one()
    
        if employee.check_password(data['password']):
            return {
                "employee_id": employee.employee_id, 
                "name": employee.name,
                "email": employee.email,
                "wage": employee.wage, 
                "access_level":employee.access_level, 
                "api_key": employee.api_key
            }, HTTPStatus.OK
    
        else:
            return {'msg': 'Wrong password'}, HTTPStatus.UNAUTHORIZED
    
    except exc.NoResultFound:
        return {"msg": "Employee not found"}, HTTPStatus.UNAUTHORIZED

    except exc.DatabaseError:
        return {"msg": "Invalid employee id"}, HTTPStatus.UNAUTHORIZED

def create_employee():
    session: Session = db.session

    data = request.get_json()
    data["api_key"] = token_urlsafe(16)

    employee = EmployeeModel(**data)

    session.add(employee)
    session.commit()

    return jsonify(employee), HTTPStatus.CREATED

def update_employee():
    pass

def delete_employee():
    pass

def get_all_employees():
    session: Session = db.session
    data = session.query(EmployeeModel).all()

    return jsonify(data), HTTPStatus.OK

def get_employee_by_id():
    pass