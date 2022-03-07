from http import HTTPStatus
from flask import current_app, jsonify, request
from sqlalchemy.exc import DataError
from app.models.students_model import StudentsModel
# from flask_httpauth import HTTPTokenAuth


# auth = HTTPTokenAuth(scheme="Bearer")


def signin():
  pass

def sigin():
    pass

def create_student():
    pass

def update_student():
    pass

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

