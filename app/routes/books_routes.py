from flask import Blueprint

from app.controllers import books_controllers

bp = Blueprint("books",__name__,url_prefix="/books")
                                                                     
bp.delete("/<book_id>")(books_controllers.delete_book_by_id)
bp.patch("/<book_id>")(books_controllers.patch_book_by_id)
bp.post("/register")(books_controllers.register_books)
bp.get("")(books_controllers.get_all_books)