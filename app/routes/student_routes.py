from flask import Blueprint

from app.controllers import students_controllers

bp = Blueprint('students', __name__, url_prefix='/students')

bp.get('/<student_id>')(students_controllers.get_student_by_id)