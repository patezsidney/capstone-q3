from http import HTTPStatus
from secrets import token_urlsafe
from flask import current_app, jsonify, request
from sqlalchemy import exc
from sqlalchemy.exc import DataError
from werkzeug.exceptions import NotFound
from app.configs.auth import auth_employee
from app.models.exc import IncorrectKeyError, MissingKeyError, TypeValueError
from app.models.students_model import StudentsModel

@auth_employee.login_required(role=['admin'])
def register():
    try:
        data = request.get_json()

        StudentsModel.check_incorrect_keys(data)
        StudentsModel.check_keys(data)
        StudentsModel.check_type_value(data)

        data["api_key"] = token_urlsafe(16)

        student = StudentsModel(**data)

        current_app.db.session.add(student)
        current_app.db.session.commit()

        return StudentsModel.serialize(student),HTTPStatus.CREATED
    except MissingKeyError:
        return {"msg":"Missing key(s)"},HTTPStatus.BAD_REQUEST
    except IncorrectKeyError:
        return {"msg": "Use of invalid key"},HTTPStatus.BAD_REQUEST
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST
        
def signin():
    data = request.get_json()
    
    try:
        student: StudentsModel = StudentsModel.query.filter_by(cpf=data['cpf']).one()
    
        if student.check_password(data['password']):
            data = StudentsModel.serialize(student)
            data['api_key'] = student.api_key
            return data, HTTPStatus.OK
    
        else:
            return {'msg': 'Wrong password'}, HTTPStatus.UNAUTHORIZED
    
    except exc.NoResultFound:
        return {"msg": "Employee not found"}, HTTPStatus.UNAUTHORIZED

    except exc.DatabaseError:
        return {"msg": "Invalid employee id"}, HTTPStatus.UNAUTHORIZED


@auth_employee.login_required(role=['admin'])
def update_student(student_id:str):
    try:
        data = request.get_json()

        StudentsModel.check_incorrect_keys(data)
        StudentsModel.check_type_value(data)

        student:StudentsModel = StudentsModel.query.filter_by(registration_student_id=student_id).first()

        if student == None:
            raise NotFound

        for key, value in data.items():
            setattr(student,key,value)

        current_app.db.session.add(student)
        current_app.db.session.commit()

        return jsonify(StudentsModel.serialize(student)),HTTPStatus.ACCEPTED
    except IncorrectKeyError:
        return {"msg": "Use of invalid key"},HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg":"Student not found"},HTTPStatus.NOT_FOUND
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST

@auth_employee.login_required(role=['admin'])
def delete_student(student_id):
    try:
        student:StudentsModel = StudentsModel.query.filter_by(registration_student_id=student_id).first()

        if student == None:
            raise NotFound

        current_app.db.session.delete(student)
        current_app.db.session.commit()

        return "",HTTPStatus.NO_CONTENT
    except NotFound:
        return {"msg":"Student not found"},HTTPStatus.NOT_FOUND


@auth_employee.login_required(role="admin")
def get_all_students():
    data = current_app.db.session.query(StudentsModel).paginate(page=None,per_page=20)

    return jsonify(StudentsModel.serialize(data.items)), HTTPStatus.OK



#@auth_employee.login_required(role=['admin'])
def get_student_by_api_key():
    bearer_token = request.headers.get('Authorization').split(' ')[1]

    student: StudentsModel = StudentsModel.query.filter_by(api_key=bearer_token).first()

    if not student:
        return {"msg": "unauthorized token!"}, HTTPStatus.BAD_REQUEST

    return jsonify(StudentsModel.serialize(student)), HTTPStatus.OK

@auth_employee.login_required(role=['admin'])
def get_student_by_id(student_id: str):
    try:
        student: StudentsModel = StudentsModel.query.filter_by(
        registration_student_id = student_id).first()
    
        return jsonify(StudentsModel.serialize(student)), HTTPStatus.OK
    
    except DataError:
        return {"msg": "Student not found"}, HTTPStatus.NOT_FOUND

