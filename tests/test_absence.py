from flask.testing import FlaskClient

def test_delete_absence_success(client: FlaskClient):
    request_data = {
        "name": "felipe",
        "absences": [
                        {
                            "date": "Sat, 15 Feb 2020 00:00:00 GMT",
                            "justify": False,
                            "classroom_id": "cf43d8ca-37a8-4140-bc97-32192e151a27"
                        }
                    ]
    }

    request_response = client.post("/api/absence", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    request_delete = client.delete(f"/api/absence/{response_json['absence_id']}")

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"

def test_delete_absence_error(client: FlaskClient):

    request_delete = client.delete(f"/api/absence/b3298cfc-7fb8-47af-91ed-f2d8c4545cdd")

    assert (request_delete.status_code == 404), "Verificar se o status code é Not Found"