from flask_httpauth import HTTPTokenAuth
from sqlalchemy import exc

from app.models.employee_model import EmployeeModel

auth_employee = HTTPTokenAuth()

@auth_employee.verify_token
def verify_token(api_key: str):
    try:
        employee: EmployeeModel = EmployeeModel.query.filter_by(api_key=api_key).one()
        return employee
    except exc.NoResultFound:
        'Not found'

@auth_employee.get_user_roles
def get_user_roles(employee: EmployeeModel):
    if employee == 'Not Found':
        return 'error'
    return employee.access_level