from flask import Flask

from app import routes
from app.configs import database, migrations
from tests.database_populate import populate_database


def create_app():
    app = Flask(__name__)
    app.config['JSON_SORT_KEYS'] = False

    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)
#    populate_database(app)

    return app
