from http import HTTPStatus
from app.models import BooksModel
from flask import request, jsonify, current_app
from app.configs.auth import auth_employee
from app.models.exc import IncorrectKeyError,MissingKeyError

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