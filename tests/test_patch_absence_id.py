from flask.testing import FlaskClient

def test_get_student_by_id(client: FlaskClient):
    response = client.patch("/api/absences/494925c7-7399-44e2-a00e-653581145979")
    mock_reponse = {
                    "name": "felipe",
                    "absence": {
                        "absence_id": "494925c7-7399-44e2-a00e-653581145979",
                        "date": "Sat, 15 Feb 2020 00:00:00 GMT",
                        "justify": True,
                        "classroom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20",
                        "student_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20"
                    }
                    }
    
    response_json: dict = response.get_json()
    
    print(response.get_json())
    
    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"