from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy.exc import DataError, StatementError
from werkzeug.exceptions import NotFound

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models import GradesModel
from app.models import StudentsModel
from app.services.decorators import verify_some_keys


@auth_employee.login_required(role=['admin','teacher'])
@verify_some_keys(["ativity", "grade", "student_id", "classrom_id"])
def create_grade(*_):
    data = request.get_json()
    new_grade = GradesModel(**data)
    db.session.add(new_grade)
    db.session.commit()
    return GradesModel.serialize(new_grade), HTTPStatus.CREATED


@auth_employee.login_required(role=['admin','teacher'])
def update_grade(id: str):
    try:
        data = request.get_json()
        grade: GradesModel = GradesModel.query.get_or_404(id)
        for key, value in data.items():    
            setattr(grade, key, value)    
        db.session.add(grade)
        db.session.commit()
        return GradesModel.serialize(grade), HTTPStatus.ACCEPTED
    except DataError:
        return {"msg": "grade id invalid"}, HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg": "id not found"}, HTTPStatus.NOT_FOUND


@auth_employee.login_required(role=['admin','teacher'])
def delete_grade(grade_id: str):
    try:
        grade: GradesModel = GradesModel.query.filter_by(grade_id=grade_id).one()
        if grade is None:
            return {"msg": "id not found"}, HTTPStatus.NOT_FOUND
        return GradesModel.serialize(grade), HTTPStatus.NO_CONTENT
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
            return jsonify(GradesModel.serialize(grades.items)), HTTPStatus.OK
        grades: GradesModel = GradesModel.query.filter_by(classrom_id=classroom).paginate(page,per_page)
        if grades.items == []:
            return {"msg": "classroom id not found"}, HTTPStatus.NOT_FOUND
        return jsonify(GradesModel.serialize(grades.items)), HTTPStatus.OK
    except StatementError:
        return {"msg": "classroom id is invalid"}, HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg": "page not found"}, HTTPStatus.NOT_FOUND
    

@auth_employee.login_required(role=['admin','teacher'])
def get_student_grades(student_id: str):
    try:
        grades = GradesModel.query.filter_by(student_id = student_id).all()
        if grades == []:
            return {"msg": "student not found"}, HTTPStatus.NOT_FOUND
        return jsonify(GradesModel.serialize(grades)), HTTPStatus.OK
    except DataError:
        return {"msg": "student id invalid"}, HTTPStatus.BAD_REQUEST
    except AttributeError:
        return {"msg": "student not found"}, HTTPStatus.NOT_FOUND


def get_student_grades_by_api_key():
    bearer_token = request.headers.get('Authorization').split(' ')[1]

    student: StudentsModel = StudentsModel.query.filter_by(api_key=bearer_token).first()

    if not student:
        return {"msg": "unauthorized token!"}, HTTPStatus.BAD_REQUEST

    output = []

    for grades in student.grades:
        grades: GradesModel

        response = {
                "grades_class": grades.classroom.name,
                "school_subject": grades.classroom.school_subjects[0].school_subject.title(),
                "grade": grades.grade
        }

        output.append(response)

    return jsonify(output), HTTPStatus.OK