from flask import Blueprint

from app.controllers import library_controllers

bp = Blueprint('library', __name__, url_prefix='/library')

bp.get("")(library_controllers.get_library_list)

bp.get('/<book_id>')(library_controllers.get_library)
bp.post("/rental")(library_controllers.library_register)
bp.delete('/<library_id>')(library_controllers.delete_library)
bp.patch("/<id>")(library_controllers.edit_book_or_student_in_book_rental_by_id)
bp.patch("/return/<id>")(library_controllers.register_book_rental_return_by_id)
