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
                }, HTTPStatus.BAD_REQUEST

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
                }, HTTPStatus.BAD_REQUEST


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

    page = request.args.get('page', 1, type=int)
    per_page = 20
    session: Session = db.session
    
    get_args = request.args
    page = get_args.get('page', 1, type=int)
    per_page = 20
    
    args_model = {
            "employee_id": get_args.get('employee_id'),
			"name": get_args.get('name'),
			"email": get_args.get('email'),
			"wage":get_args.get('wage', type=float),
			"access_level": get_args.get('access_level')
            }
    args = {}
    for key, value in args_model.items():
        if value != None:
            args[key] = value

    data = session.query(EmployeeModel).filter_by(**args).paginate(page, per_page, error_out=False)
    
    result = {"result": data.items}
    result['page'] = data.page
    result['total_number_of_pages'] = data.pages

    return jsonify(result), HTTPStatus.OK

@auth_employee.login_required(role='admin')
def get_employee_by_id(employee_id:str):
    employee: EmployeeModel = EmployeeModel.query.get(employee_id)

    if employee == None:
        return {'msg': 'Employee not found'}, HTTPStatus.NOT_FOUND

    return jsonify(employee), HTTPStatus.OK
