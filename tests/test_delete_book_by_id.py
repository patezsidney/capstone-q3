from flask.testing import FlaskClient


def test_delete_book_by_id(client: FlaskClient):
    
    request_response = client.delete("/api/books/9c638ca2-901c-4028-91d4-c34209eff719", headers={"Authorization": 'Bearer 1234'})
    
    assert (request_response.status_code == 204), "Verificar se o status code é NO CONTENT"

def test_delete_book_with_invalid_key(client: FlaskClient):
    
    request_response = client.delete("/api/books/9c638ca2-901c-4028-91d4-c34209eff700", headers={"Authorization": 'Bearer 1234'})
    
    assert (request_response.status_code == 404), "Verificar se o status code é NOT FOUND"