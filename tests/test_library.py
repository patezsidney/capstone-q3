from flask.testing import FlaskClient


def test_get_all_library(client :FlaskClient):

    response = client.get("/api/library",headers={"Authorization": 'Bearer 1236'})

    response_json: list = response.get_json()
    
    assert (type(response_json) is list), "Verificar se está retornando um lista"
    assert (len(response_json) == 10), "Verificar se está retornando 9 registros"
    assert (response.status_code == 200), "Verificar se o status code é OK"