from http import HTTPStatus
from app.configs.database import db
from app.models.absence_model import AbsenceModel

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

def get_student_absense(id: str):
    pass

