from http import HTTPStatus
from secrets import token_urlsafe

from flask import current_app, jsonify, request
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.absence_model import AbsenceModel
from app.models.exc import IncorrectKeyError
from app.models.students_model import StudentsModel
from app.models.classroom_model import ClassroomModel


@auth_employee.login_required(role=['admin', 'teacher'])
def create_absense():
    
    session: Session = db.session

    data = request.get_json()

    absence = AbsenceModel(**data)

    session.add(absence)
    session.commit()

    classrom: ClassroomModel = ClassroomModel.query.filter_by(
            classroom_id=absence.classroom_id).first()

    student: StudentsModel = StudentsModel.query.filter_by(
            registration_student_id=absence.student_id).first()        

    response = {
            "absence_id": absence.absence_id,
            "date": absence.date.strftime('%d/%m/%Y'),
            "justify": absence.justify,
            "classroom": classrom.name,
            "student": student.name.title(),
            "school_subject": classrom.school_subjects[0].school_subject.title()
        }

    return jsonify(response), HTTPStatus.CREATED
    

@auth_employee.login_required(role=['admin', 'teacher'])
def update_absense(absence_id: str):
    session = current_app.db.session

    try:
        absence: AbsenceModel = AbsenceModel.query.filter_by(
            absence_id=absence_id).first()

        student: StudentsModel = StudentsModel.query.filter_by(
            registration_student_id=absence.student_id
        ).first()

        classrom: ClassroomModel = ClassroomModel.query.filter_by(
            classroom_id=absence.classroom_id).first()

        setattr(absence, "justify", True)
        session.add(absence)
        session.commit()

        response = {
            "absence_id": absence.absence_id,
            "date": absence.date.strftime('%d/%m/%Y'),
            "justify": absence.justify,
            "classroom": classrom.name,
            "student": student.name.title(),
            "school_subject": classrom.school_subjects[0].school_subject.title()
        }

        return jsonify(response), HTTPStatus.OK
    
    except DataError:
        return {"msg": "absence id not found"}, HTTPStatus.NOT_FOUND


@auth_employee.login_required(role=['admin', 'teacher'])
def delete_absense(absence_id: str):
    
    try:
        absence: AbsenceModel = AbsenceModel.query.get(absence_id)
        if absence is None:
            return {'msg': 'absence not found'}, HTTPStatus.NOT_FOUND
            
        db.session.delete(absence)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT

    except DataError:
        return {'msg': 'absence not found'}, HTTPStatus.NOT_FOUND


@auth_employee.login_required(role=['admin', 'teacher'])
def get_all_absense():

    page = request.args.get('page', 1, type=int)
    per_page = 20

    absences = db.session.query(AbsenceModel
    ).paginate(page, per_page=per_page, error_out=False)
    
    output = []

    for absence in absences.items:
        absence: AbsenceModel
        classrom: ClassroomModel = ClassroomModel.query.filter_by(
            classroom_id=absence.classroom_id).first()
        students: StudentsModel = StudentsModel.query.filter_by(
            registration_student_id=absence.student_id).first()

        response = {
            "absence_id": absence.absence_id,
            "date": absence.date.strftime('%d/%m/%Y'),
            "justify": absence.justify,
            "classroom": classrom.name,
            "student": students.name.title(),
            "school_subjec": classrom.school_subjects[0].school_subject.title()
        }

        output.append(response)

    return jsonify(output), HTTPStatus.OK

# @auth_employee.login_required(role=['admin', 'teacher'])
def get_student_absense(student_id: str):
    
    try:
        student: StudentsModel = StudentsModel.query.filter_by(
        registration_student_id = student_id
        ).first()

        output = []

        for absence in student.absences:

            classrom: ClassroomModel = ClassroomModel.query.filter_by(
                classroom_id=absence.classroom_id).first()

            response = {
                "absence_id": absence.absence_id,
                "date": absence.date.strftime('%d/%m/%Y'),
                "justify": absence.justify,
                "classroom": classrom.name,
                "student": student.name.title(),
                "school_subject": classrom.school_subjects[0].school_subject.title()
            }

            output.append(response)

        return jsonify(output), HTTPStatus.OK
    
    except DataError:
        return {"msg": "student not found!"}, HTTPStatus.NOT_FOUND

