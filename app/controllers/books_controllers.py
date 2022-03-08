from http import HTTPStatus
from flask import request,jsonify,current_app
from app.models.books_model import BooksModel
from app.configs.auth import auth_employee
from werkzeug.exceptions import NotFound
from app.models.exc import IncorrectKeyError,MissingKeyError

# @auth_employee.login_required(role=["librarian","admin"])
def patch_book_by_id(book_id):
    try:
        data = request.get_json()

        book = BooksModel.query.filter_by(book_id=book_id).first()

        if book == None:
            raise NotFound

        for key, value in data.items():
            setattr(book,key,value)
            
        return data, HTTPStatus.OK
    except NotFound:
        return {"msg":"book not found"},HTTPStatus.NOT_FOUND

        

# @auth_employee.login_required(role=['librarian','admin'])
def register_books():
    try:
        data = request.get_json()

        BooksModel.check_incorrect_keys(data)
        BooksModel.missing_key(data)

        book = BooksModel(**data)

        current_app.db.session.add(book)
        current_app.db.session.commit()

        return jsonify(book),HTTPStatus.CREATED
    except IncorrectKeyError:
        return {"msg":"Incorrect key use"},HTTPStatus.BAD_REQUEST
    except MissingKeyError:
        return {"msg":"Missing key in request"},HTTPStatus.BAD_REQUEST
