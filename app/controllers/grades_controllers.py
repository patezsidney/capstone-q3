from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.exc import DataError, StatementError
from app.configs.auth import auth_employee
from werkzeug.exceptions import NotFound
from app.configs.database import db
from app.models import GradesModel, StudentsModel
from app.services.decorators import verify_some_keys


@auth_employee.login_required(role=['admin','teacher'])
@verify_some_keys(["ativity", "grade", "student_id", "classrom_id"])
def create_grade(*_):
    data = request.get_json()
    new_grade = GradesModel(**data)
    db.session.add(new_grade)
    db.session.commit()
    return jsonify(new_grade), HTTPStatus.CREATED


@auth_employee.login_required(role=['admin','teacher'])
def update_grade(id: str):
    try:
        data = request.get_json()
        grade: GradesModel = GradesModel.query.get(id)
        if grade is None:
            return {"msg": "id not found"}, HTTPStatus.NOT_FOUND
        for key, value in data.items():    
            setattr(grade, key, value)    
        db.session.add(grade)
        db.session.commit()
        return jsonify(grade), HTTPStatus.ACCEPTED
    except DataError:
        return {"msg": "grade id invalid"}, HTTPStatus.BAD_REQUEST

@auth_employee.login_required(role=['admin','teacher'])
def delete_grade(grade_id: str):
    try:
        grade: GradesModel = GradesModel.query.filter_by(grade_id=grade_id).one()
        if grade is None:
            return {"msg": "id not found"}, HTTPStatus.NOT_FOUND
        return jsonify(grade), HTTPStatus.NO_CONTENT
    except DataError:
        return {"msg": "grade id invalid"}, HTTPStatus.BAD_REQUEST


@auth_employee.login_required(role=['admin','teacher'])
def get_all_grades():
    try:
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 20, type=int)
        classroom = request.args.get("classroom", type=str)
        if classroom is None:
            grades: GradesModel = GradesModel.query.paginate(page,per_page)
            return jsonify(grades.items), HTTPStatus.OK
        grades: GradesModel = GradesModel.query.filter_by(classrom_id=classroom).paginate(page,per_page)
        if grades.items == []:
            return {"msg": "classroom id not found"}, HTTPStatus.NOT_FOUND
        return jsonify(grades.items), HTTPStatus.OK
    except StatementError:
        return {"msg": "classroom id is invalid"}, HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg": "page not found"}, HTTPStatus.NOT_FOUND
    

@auth_employee.login_required(role=['admin','teacher'])
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
        return {"msg": "student id invalid"}, HTTPStatus.BAD_REQUEST
    except AttributeError:
        return {"msg": "student not found"}, HTTPStatus.NOT_FOUND
