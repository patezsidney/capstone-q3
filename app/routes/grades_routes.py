from flask import Blueprint

from app.controllers import grades_controllers

bp = Blueprint('grades', __name__, url_prefix='/grades')

bp.get("/<student_id>")(grades_controllers.get_student_grades)