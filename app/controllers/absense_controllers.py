from http import HTTPStatus
from secrets import token_urlsafe

from flask import current_app, jsonify, request
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.absence_model import AbsenceModel
from app.models.exc import IncorrectKeyError
from app.models.students_model import StudentsModel


@auth_employee.login_required(role=['admin', 'teacher'])
def create_absense():
    try:
        session: Session = db.session

        data = request.get_json()

        absence = AbsenceModel(**data)

        session.add(absence)
        session.commit()

        return jsonify(absence), HTTPStatus.CREATED
    
    except IncorrectKeyError:
        return {"msg": "incorret type value passed"}, HTTPStatus.BAD_REQUEST
    

@auth_employee.login_required(role=['admin', 'teacher'])
def update_absense(absence_id: str):
    session = current_app.db.session

    try:
        absence: AbsenceModel = AbsenceModel.query.filter_by(absence_id=absence_id).first()
        student: StudentsModel = StudentsModel.query.filter_by(
            registration_student_id=absence.student_id
        ).first()

        setattr(absence, "justify", True)
        session.add(absence)
        session.commit()

        response = {
            "name": student.name,
            "absence": absence
        }

        return jsonify(response), HTTPStatus.OK
    
    except DataError:
        return {"msg": "absence id not found"}, HTTPStatus.NOT_FOUND


@auth_employee.login_required(role=['admin', 'teacher'])
def delete_absense(absence_id: str):
    
    try:
        absence: AbsenceModel = AbsenceModel.query.get(absence_id)
        if absence is None:
            return {'msg': 'absence not found'}, HTTPStatus.NOT_FOUND
            
        db.session.delete(absence)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT

    except DataError:
        return {'msg': 'absence not found'}, HTTPStatus.NOT_FOUND


@auth_employee.login_required(role=['admin', 'teacher'])
def get_all_absense():
    absences: AbsenceModel = db.session.query(AbsenceModel).all()

    return jsonify(absences), HTTPStatus.OK

# @auth_employee.login_required(role=['admin', 'teacher'])
def get_student_absense(student_id: str):
    
    try:
        student: StudentsModel = StudentsModel.query.filter_by(
        registration_student_id = student_id
    ).first()

        response = {
            "name": student.name,
            "absences": student.absences
        }

        return jsonify(response), HTTPStatus.OK
    
    except DataError:
        return {"msg": "student not found!"}, HTTPStatus.NOT_FOUND

