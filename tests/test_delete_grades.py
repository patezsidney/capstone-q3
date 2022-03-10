from flask.testing import FlaskClient


def test_delete_grades_success(client :FlaskClient):

    request_delete = client.delete("/api/grades/14cff389-868d-4858-8e3b-466ab29c8137", headers={"Authorization": "Bearer 1234"})

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"