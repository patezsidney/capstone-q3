from flask import Blueprint

from app.controllers import students_controllers
from app.controllers import classroom_controllers

bp = Blueprint('student_api', __name__, url_prefix='/student')

bp.post("/sign")(students_controllers.sigin)
bp.post("/classroom")(classroom_controllers.create_classroom)