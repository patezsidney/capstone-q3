from flask import Blueprint, Flask

from app.routes.student_routes import bp as bp_example

bp = Blueprint('api', __name__, url_prefix='/api')

def init_app(app: Flask):
    bp.register_blueprint(bp_example)
    app.register_blueprint(bp)