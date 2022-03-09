from flask.testing import FlaskClient


def test_delete_library(client: FlaskClient):
    request_delete = client.delete("/api/library/023b926d-8f03-460d-be7b-840d80f91f6e")

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"