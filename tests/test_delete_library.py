from flask.testing import FlaskClient

def test_delete_library(client: FlaskClient):
    request_delete = client.delete("/api/library/3554e9f0-8208-4e99-81c1-d79f3caf891c")

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"