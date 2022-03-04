from http import HTTPStatus
from flask import current_app, jsonify, request
from app.models.students_model import StudentsModel
# from flask_httpauth import HTTPTokenAuth


# auth = HTTPTokenAuth(scheme="Bearer")


def signin():
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


def get_student_by_id():
    pass