from http import HTTPStatus

from flask import current_app, request
from werkzeug.exceptions import NotFound

from app.configs.auth import auth_employee
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