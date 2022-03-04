from http import HTTPStatus
from app.models.students_model import StudentsModel
from flask import request, current_app, jsonify
from secrets import token_urlsafe

def sigin():
    data = request.get_json()
    data["api_key"] = token_urlsafe(16)

    student = StudentsModel(**data)

    current_app.db.session.add(student)
    current_app.db.session.commit()

    return jsonify(student),HTTPStatus.CREATED

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