from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.exc import DataError, StatementError
from werkzeug.exceptions import NotFound
from app.configs.database import db
from app.models import GradesModel, StudentsModel


def create_grade():
    data = request.get_json()
    new_grade = GradesModel(**data)
    db.session.add(new_grade)
    db.session.commit()
    return jsonify(new_grade), HTTPStatus.CREATED

def update_grade(id: str):
    data = request.get_json()
    grade: GradesModel = GradesModel.query.get(id)
    for key, value in data.items():    
        setattr(grade, key, value)    
    db.session.add(grade)
    db.session.commit()
    return jsonify(grade), HTTPStatus.ACCEPTED

def delete_grade(grade_id: str):
    grade: GradesModel = GradesModel.query.filter_by(grade_id=grade_id).one()
    return jsonify(grade), HTTPStatus.NO_CONTENT


def get_all_grades():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)
    classroom = request.args.get("classroom", type=str)
    try:
        if classroom is None:
            grades: GradesModel = GradesModel.query.paginate(page,per_page)
            return jsonify(grades.items), HTTPStatus.OK
        grades: GradesModel = GradesModel.query.filter_by(classrom_id=classroom).paginate(page,per_page)
        return jsonify(grades.items), HTTPStatus.OK
    except StatementError:
        return {"error": "classroom id is invalid"}, HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"error": "page not found"}, HTTPStatus.NOT_FOUND

    

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

