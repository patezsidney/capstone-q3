from flask.testing import FlaskClient


def test_get_all_absences(client: FlaskClient):
    request_response = client.get("/api/absences", headers={"Authorization": "Bearer 1234"})

    assert (request_response.status_code == 200), "Verificar se o status code é ok"