def test_delete_absence_success(client):
    request_data = {
        "date": "07/03/2022",
        "justify": True
    }

    request_response = client.post("/api/absence", json=request_data, follow_redirects=True )
    response_json: dict = request_response.get_json()

    request_delete = client.delete(f"/api/absence/{response_json['absence_id']}")

    assert (request_delete.status_code == 204), "Verificar se o status code é No Content"

def test_delete_absence_error(client):

    request_delete = client.delete(f"/api/absence/b3298cfc-7fb8-47af-91ed-f2d8c4545cdd")

    assert (request_delete.status_code == 404), "Verificar se o status code é Not Found"