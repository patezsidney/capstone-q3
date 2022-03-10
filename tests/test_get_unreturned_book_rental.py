from flask.testing import FlaskClient


def test_get_unreturned_book_rental(client: FlaskClient):

    response = client.get("/api/library/unreturned_rental",headers={"Authorization": 'Bearer 1236'})

    response_json = response.get_json()
    
    assert (type(response_json) is list), "Verificar se está retornando um lista"
    assert (len(response_json) == 2), "Verificar se está retornando 2 registro"
    assert (response.status_code == 200), "Verificar se o status code é OK"