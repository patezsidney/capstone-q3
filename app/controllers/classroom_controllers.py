from http import HTTPStatus
from flask import jsonify, request
from sqlalchemy import exc
from sqlalchemy.orm.session import Session

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.classroom_model import ClassroomModel
from app.models.employee_model import EmployeeModel


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
    page = request.args.get('page', 1, type=int)
    per_page = 20
    session: Session = db.session
    data = session.query(ClassroomModel).paginate(page, per_page=per_page, error_out=False)

    response = []
    
    for classroom in data.items:

        response.append({
            "classroom_id": classroom.classroom_id,
            f"{classroom.name}": [{"materia":materia.school_subject,"teacher":materia.teacher.name} for materia in classroom.school_subjects]
        })


    result = {"result": response}
    result['page'] = data.page
    result['total_number_of_pages'] = data.pages
        

    return jsonify(result), HTTPStatus.OK


@auth_employee.login_required(role=['admin', 'teacher'])
def get_employee_classroom(classroom_id: str):
    try:
        classroom: ClassroomModel = ClassroomModel.query.filter_by(classroom_id=classroom_id).one()
        teacher: EmployeeModel = EmployeeModel.query.filter_by(employee_id=classroom.school_subjects[0].employee_id).one()
        response = []
        students = []
        
        for student in classroom.students:
            students.append({
                "name": student.name.title()
            })

        response.append({
                "classroom_id": classroom.classroom_id,
                "name": classroom.name,
                "teacher": teacher.name.title(),
                "school_subjects": classroom.school_subjects[0].school_subject.title(),
                "students": students
            })

        return jsonify(response), HTTPStatus.OK

    except exc.NoResultFound:
        return {'msg': 'Classroom not found'}, HTTPStatus.NOT_FOUND