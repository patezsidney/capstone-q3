from http import HTTPStatus
from secrets import token_urlsafe

from flask import jsonify, request
from sqlalchemy import exc
from sqlalchemy.orm.session import Session

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.employee_model import EmployeeModel
from app.services.decorators import verify_some_keys


def sigin():
    data = request.get_json()

    try:
        employee: EmployeeModel = EmployeeModel.query.filter_by(email=data['email']).one()
    
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
        return {"msg": "Invalid employee email"}, HTTPStatus.UNAUTHORIZED
    
    except KeyError:
        return {
                "error": "incorrect key(s)",
                "expected to be": ['email','password'],
                "received": list(data.keys())
                }, HTTPStatus.UNPROCESSABLE_ENTITY

@auth_employee.login_required(role='admin')
def create_employee():
    try:
        session: Session = db.session

        data = request.get_json()
        data["api_key"] = token_urlsafe(16)

        employee = EmployeeModel(**data)

        session.add(employee)
        session.commit()

        return jsonify(employee), HTTPStatus.CREATED

    except exc.IntegrityError:
        return {'msg': 'Email already exists'}, HTTPStatus.CONFLICT

    except TypeError:
        data.pop('api_key')
        return {
                "error": "incorrect key(s)",
                "expected to be": ['name', 'email', 'wage', 'access_level','password'],
                "received": list(data.keys())
                }, HTTPStatus.UNPROCESSABLE_ENTITY


@verify_some_keys(['name', 'email', 'wage', 'access_level','password' ,'school_subjects'])
@auth_employee.login_required(role=['admin', 'teacher'])
def update_employee(employee_id: str):
    try: 
        data = request.get_json()

        employee: EmployeeModel = EmployeeModel.query.get(employee_id)
        if employee is None: 
            return {'msg': 'Employee not found'}, HTTPStatus.NOT_FOUND

        if auth_employee.current_user().access_level == 'teacher' and employee != auth_employee.current_user():
            return {'msg': 'No authtorization for this action'}, HTTPStatus.UNAUTHORIZED
            
        password = data.get('password')

        if password is not None:
            password = data.pop('password')

        for key, value in data.items():    
            setattr(employee, key, value)    
        
        if password is not None:
            employee.password = password

        db.session.add(employee)
        db.session.commit()

        return jsonify(employee), HTTPStatus.ACCEPTED

    except exc.IntegrityError:
        return {'msg': 'Email already exists'}, HTTPStatus.CONFLICT

@auth_employee.login_required(role='admin')
def delete_employee(employee_id: str):
    employee: EmployeeModel = EmployeeModel.query.get(employee_id)
    if employee is None:
        return {'msg': 'Employee not found'}, HTTPStatus.NOT_FOUND
        
    db.session.delete(employee)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT

@auth_employee.login_required(role='admin')
def get_all_employees():
    session: Session = db.session
    data = session.query(EmployeeModel).all()

    return jsonify(data), HTTPStatus.OK

@auth_employee.login_required(role='admin')
def get_employee_by_id(employee_id:str):
    employee: EmployeeModel = EmployeeModel.query.filter_by(employee_id=employee_id).one()
    return jsonify(employee), HTTPStatus.OK