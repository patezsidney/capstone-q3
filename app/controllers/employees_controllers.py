from flask import request, jsonify
from http import HTTPStatus
from secrets import token_urlsafe
from sqlalchemy import exc
from sqlalchemy.orm.session import Session

from app.configs.database import db

from app.models.employee_model import EmployeeModel
from app.services.decorators import verify_some_keys

def sigin():
    pass

def create_employee():
    session: Session = db.session

    data = request.get_json()
    data["api_key"] = token_urlsafe(16)

    employee = EmployeeModel(**data)

    session.add(employee)
    session.commit()

    return jsonify(employee), HTTPStatus.CREATED

@verify_some_keys(['name', 'email', 'wage', 'access_level','password' ,'school_subjects'])
def update_employee(employee_id: str):
    try: 
        data = request.get_json()

        employee: EmployeeModel = EmployeeModel.query.get(employee_id)
        if employee is None: 
            return {'msg': 'Employee not found'}, HTTPStatus.NOT_FOUND

        password = data.get('password')

        if password is not None:
            password = data.pop('password')

        for key, value in data.items():    
            setattr(employee, key, value)    
        
        if password is not None:
            employee.password = password

        db.session.add(employee)
        db.session.commit()

        return jsonify(employee), HTTPStatus.OK
    except exc.IntegrityError:
        return {'msg': 'Email already exists'}, HTTPStatus.CONFLICT

def delete_employee():
    pass

def get_all_employees():
    session: Session = db.session
    data = session.query(EmployeeModel).all()

    return jsonify(data), HTTPStatus.OK

def get_employee_by_id():
    pass