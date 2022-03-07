from http import HTTPStatus
from flask import jsonify

from sqlalchemy.exc import DataError

from app.models.library_model import LibraryModel

def create_rental():
    pass

def update_rental(id: str):
    pass

def delete_rental(id: str):
    pass

def get_all_rents():
    pass

def get_rental_by_id(rental_id: str):
    
    try:
        rental: LibraryModel = LibraryModel.query.filter_by(
        library_id=rental_id
    ).first()

        response = {
            "rental": rental,
            "student": rental.student.name,
            "book": rental.book.title,
            "employee": rental.employee.name
        }

        return jsonify(response), HTTPStatus.OK
    
    except DataError:
        return {"msg": "rental_id not found"}, HTTPStatus.NOT_FOUND
