import os

import pytest
from flask import Flask

from app import create_app
from app.configs import database
from tests.database_populate import populate_database

#necessario instalar a lib pytest-dotenv

@pytest.fixture(scope="session")
def app():

    app: Flask = create_app()
    app.config.update({
                        "TESTING": True,
                        'SQLALCHEMY_DATABASE_URI': os.getenv('DB_TEST_URI')
                      })
    

    database.db.create_all(app=app)
    yield app
    database.db.drop_all(app=app)

@pytest.fixture(scope="session")
def client(app: Flask):
    populate_database(app)
    return app.test_client()
