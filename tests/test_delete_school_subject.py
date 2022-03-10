from flask.testing import FlaskClient


def test_delete_school_subjects(client: FlaskClient):
    new_subject_request = {
        'school_subject':'Matemática do 1º ano A do ensino médio',
        'employee_id':'6d4b0f4d-a418-432e-a112-b44527ea33d4', 
        'classroom_id':'51df51e0-00a7-49e3-9f2e-0405574f5c20'
    }    
    
    new_subject_response = client.post("/api/school_subjects/register",json=new_subject_request,headers={"Authorization": "Bearer 1234"})
    subject_response_json = new_subject_response.get_json()

    
    request_response = client.delete(f"/api/school_subjects/{subject_response_json['school_subject_id']}", headers={"Authorization": 'Bearer 1234'})
    
    assert (request_response.status_code == 204), "Verificar se o status code é NO CONTENT"
