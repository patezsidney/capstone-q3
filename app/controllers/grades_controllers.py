from flask import jsonify
from http import HTTPStatus

from sqlalchemy.exc import DataError

from app.models.students_model import StudentsModel


def create_grade():
    pass

def update_grade(id: str):
    pass

def delete_grade(id: str):
    pass

def get_all_grades():
    pass

# @auth.login_required
def get_student_grades(student_id: str):
    
    try:
        student: StudentsModel = StudentsModel.query.filter_by(
        registration_student_id = student_id
    ).first()

        response = {
            "name": student.name,
            "grades": student.grades
        }

        return jsonify(response), HTTPStatus.OK
    
    except DataError:
        
        return {"msg": "student not found!"}, HTTPStatus.NOT_FOUND

