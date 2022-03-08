from flask import Blueprint

from app.controllers import grades_controllers

bp = Blueprint('grades', __name__, url_prefix='/grades')

bp.get("")(grades_controllers.get_all_grades)
bp.post("")(grades_controllers.create_grade)
bp.get("/<student_id>")(grades_controllers.get_student_grades)
bp.delete("/<grade_id>")(grades_controllers.delete_grade)
