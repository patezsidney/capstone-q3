from http import HTTPStatus

from flask import jsonify, request
from sqlalchemy import exc
from sqlalchemy.orm.session import Session

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.classroom_model import ClassroomModel


@auth_employee.login_required(role='admin')
def create_classroom():
    try:
        session: Session = db.session

        data = request.get_json()

        classroom = ClassroomModel(**data)

        session.add(classroom)
        session.commit()

        return jsonify(classroom), HTTPStatus.CREATED

    except TypeError:
        return {'msg': 'could not assign a classroom'}, HTTPStatus.BAD_REQUEST


# @auth_employee.login_required(role=['admin', 'teacher'])
def update_classroom(classroom_id: str):
    try:
        data = request.get_json()

        classroom: ClassroomModel = ClassroomModel.query.get(classroom_id)
        
        if classroom is None: 
            return {'msg': 'Classroom not found'}, HTTPStatus.NOT_FOUND

        setattr(classroom, 'name', data['name'])  
        
        db.session.add(classroom)
        db.session.commit()

        return jsonify(classroom), HTTPStatus.ACCEPTED

    except exc.DataError:
        return {'msg': 'Classroom id is invalid'}, HTTPStatus.NOT_FOUND
    
    except AttributeError:
        return {'msg': 'could not assign a classroom'}, HTTPStatus.BAD_REQUEST

    except KeyError:
        return {'msg': 'could not assign a classroom'}, HTTPStatus.BAD_REQUEST


@auth_employee.login_required(role='admin')
def delete_classroom(classroom_id: str):
    try:
        classroom: ClassroomModel = ClassroomModel.query.get(classroom_id)
        if classroom is None:
            return {'msg': 'Classroom not found'}, HTTPStatus.NOT_FOUND
            
        db.session.delete(classroom)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT

    except exc.DataError:
        return {'msg': 'Classroom id is invalid'}


@auth_employee.login_required(role='admin')
def get_all_classroom():
    session: Session = db.session
    data = session.query(ClassroomModel).all()

    return jsonify(data), HTTPStatus.OK


@auth_employee.login_required(role=['admin', 'teacher'])
def get_employee_classroom(classroom_id: str):
    try:
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

    except exc.NoResultFound:
        return {'msg': 'Classroom not found'}, HTTPStatus.NOT_FOUND