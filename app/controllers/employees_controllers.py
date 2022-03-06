from flask import request, jsonify
from http import HTTPStatus
from secrets import token_urlsafe
from sqlalchemy.orm.session import Session

from app.configs.database import db

from app.models.employee_model import EmployeeModel

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