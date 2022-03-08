from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy import exc, inspect
from sqlalchemy.engine.row import RowMapping
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

def update_classroom(classroom_id: str):
    try:
        data = request.get_json()
        classroom: ClassroomModel = ClassroomModel.query.get(classroom_id)
        if classroom is None: 
            return {'msg': 'Classroom not found'}, HTTPStatus.NOT_FOUND

        for key, value in data.items():    
            setattr(classroom, key, value)    
        
        db.session.add(classroom)
        db.session.commit()

        return jsonify(classroom), HTTPStatus.OK
    except exc.IdentifierError:
        return {'msg': 'Classrom id already exists'}, HTTPStatus.CONFLICT

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

def get_employee_classroom(classroom_id: str):
    classroom: ClassroomModel = ClassroomModel.query.filter_by(classroom_id=classroom_id).one()
    subjects = []

    for subject in classroom.school_subjects:
        subjects.append({
            "school_subject_id": subject.school_subject_id,
			"school_subject": subject.school_subject,
			"employee_id": subject.employee_id,
			"classroom_id": subject.teacher
        })

    return {
            "classroom_id": classroom.classroom_id,
            "name": classroom.name,
            "absences": classroom.absences,
            "school_subjects": subjects,
            "grades": classroom.grades,
            "students": classroom.students

        }, HTTPStatus.OK
