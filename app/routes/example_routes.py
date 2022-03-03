from flask import Blueprint

from app.controllers import example_controllers

bp = Blueprint('example', __name__, url_prefix='/example')

bp.get('')(example_controllers.get_example_controller)