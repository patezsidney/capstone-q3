from flask import Blueprint

from app.controllers import students_controllers

bp = Blueprint('example', __name__, url_prefix='/api/students')

bp.post('/login')(students_controllers.signin)