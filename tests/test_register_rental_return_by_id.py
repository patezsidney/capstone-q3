from flask.testing import FlaskClient


def test_register_book_rental_return_by_id(client: FlaskClient):
    
    request_response = client.patch("/api/library/return/536801db-e27e-470e-b180-3e9905938808", headers={"Authorization": "Bearer 1234"})
    
    assert (request_response.status_code == 202), "Verificar se o status code é ACCEPTED"

from flask.testing import FlaskClient


def test_register_book_rental_return_by_id_of_rental_returned(client: FlaskClient):
    
    request_response = client.patch("/api/library/return/23c3c4c8-d923-43d3-bc1b-c47d7b741ee1", headers={"Authorization": "Bearer 1234"})
    
    assert (request_response.status_code == 404), "Verificar se o status code é NOT FOUND"