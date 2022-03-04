from flask import Blueprint

from app.controllers import example_controllers


bp = Blueprint('student_api', __name__, url_prefix='/api')

bp.get("/sign")(example_controllers.get_example_controller)