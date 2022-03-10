from flask.testing import FlaskClient


def test_get_student_by_api_key(client: FlaskClient):
    response = client.get("/api/absences/student", headers={"Authorization": 'Bearer 1233'})
    mock_reponse = [
                    {
                        "absence_class": "2A",
                        "school_subject": "Node",
                        "absence_date": "15/02/2020"
                    }
                    ]
    
    response_json: dict = response.get_json()
    
    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is list), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"