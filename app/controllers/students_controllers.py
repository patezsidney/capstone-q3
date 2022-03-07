from http import HTTPStatus
from flask import current_app, jsonify, request
from app.configs.auth import auth_employee

from sqlalchemy.exc import DataError

from app.models.students_model import StudentsModel

def sigin():
    pass

def create_student():
    pass

# @auth_employee.login_required(role='admin')
def update_student(student_id:str):
    data = request.get_json()

    student:StudentsModel = StudentsModel.query.filter_by(registration_student_id=student_id).first()

    for key, value in data.items():
        setattr(student,key,value)

    current_app.db.session.add(student)
    current_app.db.session.commit()

    return jsonify(student),HTTPStatus.OK

def delete_student():
    pass

def get_all_students():
    pass


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

