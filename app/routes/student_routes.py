from flask import Blueprint

from app.controllers import example_controllers

bp = Blueprint('example', __name__, url_prefix='/api')

bp.post("/sign/student")(example_controllers.get_example_controller)