import pytest
import os
from flask import Flask

from app import create_app
from app.configs import database

#necessario instalar a lib pytest-dotenv

@pytest.fixture()
def app():

    app: Flask = create_app()
    app.config.update({
                        "TESTING": True,
                        'SQLALCHEMY_DATABASE_URI': os.getenv('DB_TEST_URI')
                      })
    

    database.db.create_all(app=app)
    yield app
    database.db.drop_all(app=app)

@pytest.fixture()
def client(app: Flask):
    return app.test_client()
