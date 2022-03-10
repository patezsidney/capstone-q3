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

def register_teacher_in_school_subject():
    data = request.get_json()

    school_subject = SchoolSubjectsModel(**data)

    current_app.db.session.add(school_subject)
    current_app.db.session.commit()

    return {
            "school_subject_id":school_subject.school_subject_id,
            "school_subject":school_subject.school_subject,
            "classroom":school_subject.classroom.name,
            "teacher":school_subject.employee.name
            },HTTPStatus.CREATED