from app.configs.database import db
from app.models.classroom_model import ClassroomModel
from flask import current_app, request , jsonify

def create_classroom():
    data = request.get_json()

    classroom = ClassroomModel(**data)

    current_app.db.session.add(classroom)
    current_app.db.session.commit()

    return ""

def update_classroom(id: str):
    pass

def delete_classroom(id: str):
    pass

def get_all_classroom():
    pass

def get_employee_classroom(id: str):
    pass