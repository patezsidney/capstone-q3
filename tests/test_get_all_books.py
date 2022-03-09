from flask.testing import FlaskClient


def test_get_all_books(client: FlaskClient):
    request_response = client.get("/api/books")

    assert (request_response.status_code == 200), "Verificar se o status code é ok"