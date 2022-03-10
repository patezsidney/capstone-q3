from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy import null
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError, TypeValueError
from app.models.school_subjects_model import SchoolSubjectsModel

@auth_employee.login_required(role='admin')
def register_teacher_in_school_subject():
    data = request.get_json()

    school_subject = SchoolSubjectsModel(**data)

    current_app.db.session.add(school_subject)
    current_app.db.session.commit()

    return {
            "school_subject_id":school_subject.school_subject_id,
            "school_subject":school_subject.school_subject,
            "classroom":school_subject.classroom.name,
            "teacher":school_subject.teacher.name
            },HTTPStatus.CREATED

@auth_employee.login_required(role='admin')
def edit_school_subject_by_id(school_subject_id:str):
    data = request.get_json()
    new_school_subject = SchoolSubjectsModel.query.filter_by(school_subject_id=school_subject_id).first()

    for key,value in data.items():
        setattr(new_school_subject,key,value)

    current_app.db.session.add(new_school_subject)
    current_app.db.session.commit()

    return {"school_subject_id":new_school_subject.school_subject_id,
            "school_subject":new_school_subject.school_subject,
            "classroom":new_school_subject.classroom.name,
            "teacher":new_school_subject.teacher.name},HTTPStatus.ACCEPTED