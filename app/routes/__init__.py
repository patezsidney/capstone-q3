from flask import Blueprint, Flask
from app.routes.absences_routes import bp as bp_absences
from app.routes.students_routes import bp as bp_students
from app.routes.employees_routes import bp as bp_employees
from app.routes.grades_routes import bp as bp_grades


bp = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):
    bp.register_blueprint(bp_absences)
    bp.register_blueprint(bp_students)
    bp.register_blueprint(bp_employees)
    bp.register_blueprint(bp_grades)
    app.register_blueprint(bp)