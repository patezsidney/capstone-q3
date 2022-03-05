from http import HTTPStatus
from flask import current_app, jsonify, request

from sqlalchemy.exc import DataError

from app.models.students_model import StudentsModel

def sigin():
    pass

def create_student():
    pass

def update_student():
    pass

def delete_student():
    pass

def get_all_students():
    pass

def get_student_by_id():
    pass

# @auth.login_required
def get_student_by_api_key():
    bearer_token = request.headers.get('Authorization').split(' ')[1]

    student: StudentsModel = StudentsModel.query.filter_by(api_key=bearer_token).first()

    if not student:
        return {"msg": "unauthorized token!"}, HTTPStatus.BAD_REQUEST

    return jsonify(student), HTTPStatus.OK
