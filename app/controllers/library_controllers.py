from datetime import datetime
from http import HTTPStatus

from flask import current_app, jsonify, request
from sqlalchemy import null
from sqlalchemy.exc import DataError
from sqlalchemy.orm.session import Session
from werkzeug.exceptions import NotFound

from app.configs.auth import auth_employee
from app.configs.database import db
from app.models.exc import IncorrectKeyError, MissingKeyError, TypeValueError
from app.models.library_model import LibraryModel
from app.models.students_model import StudentsModel


# @auth_employee.login_required(role=['admin','librarian'])
def library_register():
    try:
        data = request.get_json()

        LibraryModel.check_incorrect_keys(data)
        LibraryModel.missing_key(data)

        rent = LibraryModel(**data)

        current_app.db.session.add(rent)
        current_app.db.session.commit()
        
        return jsonify(rent),HTTPStatus.CREATED
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except MissingKeyError:
        return {"msg":"Missing key"},HTTPStatus.BAD_REQUEST

def edit_book_or_student_in_book_rental_by_id(id: str):
    try:
        data = request.get_json()
        LibraryModel.check_key_in_edit_book_or_student_in_rental(data)
        LibraryModel.check_type_value(data)

        rental = LibraryModel.query.filter_by(library_id=id).first()

        if rental == None:
            raise NotFound

        for key,value in data.items():
            setattr(rental,key,value)

        current_app.db.session.add(rental)
        current_app.db.session.commit()

        return jsonify(data),HTTPStatus.ACCEPTED
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg":"rental not found"},HTTPStatus.NOT_FOUND

# @auth_employee.login_required(["admin","librarian"])
def register_book_rental_return_by_id(id:str):
    try:
        data = request.get_json()
        LibraryModel.check_incorrect_keys(data)
        LibraryModel.check_type_value(data)

        data["date_return"]=datetime.now()

        rental = LibraryModel.query.filter_by(library_id=id).first()

        if rental == None:
            raise NotFound

        for key,value in data.items():
            setattr(rental,key,value)

        current_app.db.session.add(rental)
        current_app.db.session.commit()

        return jsonify(data),HTTPStatus.ACCEPTED
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except TypeValueError:
        return {"msg":"request with incorrect value type!"},HTTPStatus.BAD_REQUEST
    except NotFound:
        return {"msg":"rental not found"},HTTPStatus.NOT_FOUND

def delete_library(library_id: str):
    
    try:
        library: LibraryModel = LibraryModel.query.get(library_id)
    
        db.session.delete(library)
        db.session.commit()

        return {}, HTTPStatus.NO_CONTENT
    
    except DataError:
        return {"mgs": "library_id not found"}, HTTPStatus.NOT_FOUND

def get_library_list():
    session: Session = db.session
    data = session.query(LibraryModel).paginate(page=None,per_page=20)

    return jsonify(data.items), HTTPStatus.OK

def get_library(library_id: str):

    try:
        library: LibraryModel = LibraryModel.query.filter_by(
        library_id=library_id
    ).first()

        response = {
            "library": library,
            "student": library.student.name,
            "book": library.book.title,
            "employee": library.employee.name
        }

        return jsonify(response), HTTPStatus.OK
    
    except DataError:
        return {"msg": "library_id not found"}, HTTPStatus.NOT_FOUND

#lista de livros de o aluno alugou e ainda não devolveu
def get_books_of_student(student_id):

    rented_books = LibraryModel.query.filter_by(student_id=student_id,date_return=None).paginate(page=None,per_page=20)

    return jsonify([{"student":rented.student.name,
             "book":rented.book.title,
             "date_accurancy":rented.date_accurancy} 
             for rented in rented_books.items ]),HTTPStatus.OK

#lista de livros alugados pelo aluno, tanto devolvidos como não devolvidos
def get_books_rented(student_id):

    rented_books = LibraryModel.query.filter_by(student_id=student_id).paginate(page=None,per_page=20)

    return jsonify([{"student":rented.student.name,
                    "book":rented.book.title,
                    "date_accurancy":rented.date_accurancy} 
                    for rented in rented_books.items ]),HTTPStatus.OK
