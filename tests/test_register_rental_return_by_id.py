from flask.testing import FlaskClient


def test_register_book_rental_return_by_id(client: FlaskClient):
    
    request_response = client.patch("/api/library/return/536801db-e27e-470e-b180-3e9905938808", headers={"Authorization": "Bearer 1234"})
    
    assert (request_response.status_code == 202), "Verificar se o status code é ACCEPTED"
