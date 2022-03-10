from flask.testing import FlaskClient


def test_register_teacher_in_school_subject(client: FlaskClient):

    request_data = {
        'school_subject':'Matemática do 1º ano A do ensino médio',
        'employee_id':'6d4b0f4d-a418-432e-a112-b44527ea33d4', 
        'classroom_id':'51df51e0-00a7-49e3-9f2e-0405574f5c20'
    }    
    
    request_response = client.post("/api/school_subjects/register",json=request_data,headers={"Authorization": "Bearer 1234"})

    response = request_response.get_json()
    
    assert (type(response) is dict)
    assert (request_response.status_code == 201), "Verificar se o status code é CREATED"