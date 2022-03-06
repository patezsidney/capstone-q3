from flask import Blueprint, Flask
from app.routes.student_routes import bp as bp_example
from app.routes.employees_routes import bp as bp_employees
from app.routes.clasroom_routes import bp as bp_classroom
bp = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):
    bp.register_blueprint(bp_example)
    bp.register_blueprint(bp_employees)
    bp.register_blueprint(bp_classroom)

    app.register_blueprint(bp)