from flask.testing import FlaskClient

def test_get_all_classrooms(client):
    request_response = client.get("/api/classrooms")

    assert (request_response.status_code == 200), "Verificar se o status code é ok"