from http import HTTPStatus
from secrets import token_urlsafe
from flask import current_app, jsonify, request
from app.configs.auth import auth_employee
from app.models.exc import IncorrectKeyError,MissingKeyError

from sqlalchemy.exc import DataError
from app.models.students_model import StudentsModel
# from flask_httpauth import HTTPTokenAuth


# auth = HTTPTokenAuth(scheme="Bearer")

# @auth_employee.login_required(role='adm')
def register():
    try:
        data = request.get_json()

        # StudentsModel.check_incorrect_keys(data)
        StudentsModel.check_keys(data)

        data["api_key"] = token_urlsafe(16)

        # password_to_hash = data.pop("password")

        student = StudentsModel(**data)

        # student.password = password_to_hash

        current_app.db.session.add(student)
        current_app.db.session.commit()

        return {"id":student.registration_student_id,
                "name":student.name,
                "contact_name":student.contact_name,
                "contact_email":student.contact_email
                },HTTPStatus.CREATED
    except MissingKeyError:
        return {"msg":"Missing key(s)"},HTTPStatus.BAD_REQUEST
    except IncorrectKeyError:
        return {"msg":"incorrect key(s)"},HTTPStatus.BAD_REQUEST

def sigin():
    pass

def create_student():
    pass

# @auth_employee.login_required(role='admin')
def update_student(student_id:str):
    try:
        data = request.get_json()

        StudentsModel.check_incorrect_keys(data)

        student:StudentsModel = StudentsModel.query.filter_by(registration_student_id=student_id).first()

        for key, value in data.items():
            setattr(student,key,value)

        current_app.db.session.add(student)
        current_app.db.session.commit()

        return jsonify(student),HTTPStatus.OK
    except IncorrectKeyError:
        return {"msg":"incorrect key(s)"},HTTPStatus.BAD_REQUEST

def delete_student():
    pass


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

