from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy import exc
from sqlalchemy.exc import DataError
from werkzeug.exceptions import NotFound

from app.configs.auth import auth_employee
from app.models.exc import IncorrectKeyError
from app.models.students_model import StudentsModel

# from flask_httpauth import HTTPTokenAuth


# auth = HTTPTokenAuth(scheme="Bearer")


def signin():
    data = request.get_json()
    
    try:
        student: StudentsModel = StudentsModel.query.filter_by(cpf=data['cpf']).one()
    
        if student.check_password(data['password']):
            return {
                        "registration_student_id": student.registration_student_id,
                        "name": student.name,
                        "contact_name": student.contact_name,
                        "contact_email": student.contact_email,
                        "cpf": student.cpf,
                        "birth_date": student.birth_date,
                        "api_key": student.api_key
                    }, HTTPStatus.OK
    
        else:
            return {'msg': 'Wrong password'}, HTTPStatus.UNAUTHORIZED
    
    except exc.NoResultFound:
        return {"msg": "Employee not found"}, HTTPStatus.UNAUTHORIZED

    except exc.DatabaseError:
        return {"msg": "Invalid employee id"}, HTTPStatus.UNAUTHORIZED


def create_student():
    pass

# @auth_employee.login_required(role='admin')
def update_student(student_id:str):
    try:
        data = request.get_json()

        StudentsModel.check_keys(data)

        student:StudentsModel = StudentsModel.query.filter_by(registration_student_id=student_id).first()

        if student == None:
            raise NotFound

        for key, value in data.items():
            setattr(student,key,value)

        current_app.db.session.add(student)
        current_app.db.session.commit()

        return jsonify(student),HTTPStatus.OK
    except IncorrectKeyError:
        return {"msg": "Use of invalid key"},HTTPStatus.CONFLICT
    except NotFound:
        return {"msg":"Student not found"}

# @auth_employee.login_required(role='admin')
def delete_student(student_id):
    try:
        student:StudentsModel = StudentsModel.query.filter_by(registration_student_id=student_id).first()

        if student == None:
            raise NotFound

        current_app.db.session.delete(student)
        current_app.db.session.commit()

        return "",HTTPStatus.OK
    except NotFound:
        return {"msg":"Student not found"}


# @auth.login_required
def get_all_students():
    data = current_app.db.session.query(StudentsModel).all()

    return jsonify(data), HTTPStatus.OK



# @auth.login_required
def get_student_by_api_key():
    bearer_token = request.headers.get('Authorization').split(' ')[1]

    student: StudentsModel = StudentsModel.query.filter_by(api_key=bearer_token).first()

    if not student:
        return {"msg": "unauthorized token!"}, HTTPStatus.BAD_REQUEST

    return jsonify(student), HTTPStatus.OK

#auth.login_required
def get_student_by_id(student_id: str):

    try:
        student: StudentsModel = StudentsModel.query.filter_by(
        registration_student_id = student_id).first()
    
        return jsonify(student), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Student not found"}, HTTPStatus.NOT_FOUND

