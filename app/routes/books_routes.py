from flask import Blueprint
from app.controllers import books_controllers

bp = Blueprint("books",__name__,url_prefix="/books")
                                                                     
bp.post("/register")(books_controllers.register_books)