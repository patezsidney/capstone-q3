from flask import jsonify, request
from http import HTTPStatus
from sqlalchemy.exc import DataError
from app.models import StudentsModel, GradesModel
from app.configs.database import db


def create_grade():
    data = request.get_json()
    new_grade = GradesModel(**data)
    db.session.add(new_grade)
    db.session.commit()
    return jsonify(new_grade), HTTPStatus.CREATED

def update_grade(id: str):
    pass

def delete_grade(grade_id: str):
    grade: GradesModel = GradesModel.query.filter_by(grade_id=grade_id).one()
    return jsonify(grade), HTTPStatus.NO_CONTENT

def get_all_grades():
    grades: GradesModel = db.session.query(GradesModel).all()
    return jsonify(grades), HTTPStatus.OK

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

