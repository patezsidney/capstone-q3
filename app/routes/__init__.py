from flask import Blueprint, Flask
from app.routes.student_routes import bp as bp_student
from app.routes.employees_routes import bp as bp_employees
from app.routes.absences_routes import bp as bp_absences

bp = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):
    bp.register_blueprint(bp_student)
    bp.register_blueprint(bp_employees)
    bp.register_blueprint(bp_absences)
    app.register_blueprint(bp)