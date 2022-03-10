from flask.testing import FlaskClient


def test_delete_school_subjects(client: FlaskClient):
    
    request_response = client.delete("/api/school_subjects/62921285-ac00-4f38-ab44-356cdea16631", headers={"Authorization": 'Bearer 1234'})
    
    assert (request_response.status_code == 204), "Verificar se o status code é NO CONTENT"
