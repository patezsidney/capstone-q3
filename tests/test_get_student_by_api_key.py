from flask.testing import FlaskClient

def test_get_student_by_id(client: FlaskClient):
    response = client.get("/api/students/profile", headers={"Authorization": 'Bearer 1234'})
    mock_reponse = {
                    "registration_student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
                    "name": "felipe",
                    "contact_name": "Rosita",
                    "contact_email": "rosita@email.com",
                    "cpf": "11111111111",
                    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
                    "absences": [
                        {
                        "absence_id": "494925c7-7399-44e2-a00e-653581145979",
                        "date": "Sat, 15 Feb 2020 00:00:00 GMT",
                        "justify": False,
                        "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
                        "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20"
                        }
                    ]
                    }
    
    response_json: dict = response.get_json()
    
    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"