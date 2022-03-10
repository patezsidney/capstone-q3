from http import HTTPStatus

from flask import current_app, request, jsonify
from werkzeug.exceptions import NotFound

from sqlalchemy.exc import DataError

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError, TypeValueError
from app.models.school_subjects_model import SchoolSubjectsModel


@auth_employee.login_required(role='admin')
def register_teacher_in_school_subject():
    try:
        data = request.get_json()
        SchoolSubjectsModel.check_incorrect_keys(data)
        SchoolSubjectsModel.check_keys(data)
        SchoolSubjectsModel.check_type_value(data)

        school_subject = SchoolSubjectsModel(**data)

        current_app.db.session.add(school_subject)
        current_app.db.session.commit()

        return {
                "school_subject_id":school_subject.school_subject_id,
                "school_subject":school_subject.school_subject,
                "classroom":school_subject.classroom.name,
                "teacher":school_subject.teacher.name
                },HTTPStatus.CREATED
    except MissingKeyError:
        return {"msg":"Missing key(s)"},HTTPStatus.BAD_REQUEST
    except IncorrectKeyError:
        return {"msg": "Use of invalid key"},HTTPStatus.BAD_REQUEST
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST


@auth_employee.login_required(role='admin')
def edit_school_subject_by_id(school_subject_id:str):
    try:
        data = request.get_json()
        SchoolSubjectsModel.check_incorrect_keys(data)
        SchoolSubjectsModel.check_type_value(data)

        new_school_subject = SchoolSubjectsModel.query.filter_by(school_subject_id=school_subject_id).first()

        if new_school_subject==None:
            raise NotFound

        for key,value in data.items():
            setattr(new_school_subject,key,value)

        current_app.db.session.add(new_school_subject)
        current_app.db.session.commit()

        return {"school_subject_id":new_school_subject.school_subject_id,
                "school_subject":new_school_subject.school_subject,
                "classroom":new_school_subject.classroom.name,
                "teacher":new_school_subject.teacher.name},HTTPStatus.ACCEPTED
    except IncorrectKeyError:
        return {"msg": "Use of invalid key"},HTTPStatus.BAD_REQUEST
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg":"Student not found"},HTTPStatus.NOT_FOUND


@auth_employee.login_required(role='admin')
def delete_school_subjects(school_subject_id):
    try:
        school_subjects: SchoolSubjectsModel = SchoolSubjectsModel.query.get(school_subject_id)
        if school_subjects is None:
            return {'msg': 'school_subjects not found'}, HTTPStatus.NOT_FOUND
            
        db.session.delete(school_subjects)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT

    except DataError:
        return {'msg': 'school_subjects not found'}, HTTPStatus.NOT_FOUND


@auth_employee.login_required(role='admin')
def get_all_school_subjects():
    page = request.args.get('page', 1, type=int)
    per_page = 20

    school_subjects = db.session.query(SchoolSubjectsModel
    ).paginate(page, per_page=per_page, error_out=False)

    output = []

    for school_subject in school_subjects.items:

        response = {
                    "school_subject_id":school_subject.school_subject_id,
                    "school_subject":school_subject.school_subject.title(),
                    "classroom":school_subject.classroom.name,
                    "teacher":school_subject.teacher.name.title()
                    }
        
        output.append(response)
    
    return jsonify(output), HTTPStatus.OK