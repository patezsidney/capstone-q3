from http import HTTPStatus
from flask import jsonify
from sqlalchemy.orm.session import Session

from app.configs.database import db
from app.models.classroom_model import ClassroomModel

def create_classroom():
    pass

def update_classroom(id: str):
    pass

def delete_classroom(id: str):
    pass

def get_all_classroom():
    session: Session = db.session
    data = session.query(ClassroomModel).all()

    return jsonify(data), HTTPStatus.OK

def get_employee_classroom(id: str):
    pass