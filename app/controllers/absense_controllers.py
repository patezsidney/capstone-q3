from flask import jsonify, current_app
from http import HTTPStatus
from app.configs.database import db
from app.models.absence_model import AbsenceModel
from sqlalchemy.exc import DataError
from app.models.students_model import StudentsModel
from app.models.absence_model import AbsenceModel


def create_absense():
    pass

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

def delete_absense(absence_id: str):
    absence: AbsenceModel = AbsenceModel.query.get(absence_id)
    if absence is None:
        return {'msg': 'Absence not found'}, HTTPStatus.NOT_FOUND
        
    db.session.delete(absence)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT

def get_all_absense():
    pass

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

