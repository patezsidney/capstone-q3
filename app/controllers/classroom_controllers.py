from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.classroom_model import ClassroomModel

def create_classroom():
    session: Session = db.session

    data = request.get_json()

    classroom = ClassroomModel(**data)

    session.add(classroom)
    session.commit()

    return jsonify(classroom), HTTPStatus.CREATED

def update_classroom(id: str):
    pass

def delete_classroom(classroom_id: str):
    classroom: ClassroomModel = ClassroomModel.query.get(classroom_id)
    if classroom is None:
        return {'msg': 'Classroom not found'}, HTTPStatus.NOT_FOUND
        
    db.session.delete(classroom)
    db.session.commit()

    return {}, HTTPStatus.NO_CONTENT

def get_all_classroom():
    session: Session = db.session
    data = session.query(ClassroomModel).all()

    return jsonify(data), HTTPStatus.OK

def get_employee_classroom(id: str):
    pass