from http import HTTPStatus
from flask import request
from app.models.students_model import StudentsModel


def signin():
    user_data = request.get_json()
    found_user: StudentsModel = StudentsModel.query.filter_by(cpf=user_data["cpf"]).first()

    if not found_user:
        return {"message": "User not found"}, HTTPStatus.NOT_FOUND

    if found_user.verify_password(user_data["password"]):
        return {"api_key": found_user.api_key}, HTTPStatus.OK

    else:
        return {"message": "Unauthorized"}, HTTPStatus.UNAUTHORIZED


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