from flask import jsonify
from http import HTTPStatus
from app.configs.database import db
from app.models.absence_model import AbsenceModel
from sqlalchemy.exc import DataError
from app.models.students_model import StudentsModel


def create_absense():
    pass

def update_absense(id: str):
    pass

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

