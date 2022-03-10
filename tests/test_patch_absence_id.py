from flask.testing import FlaskClient


def test_patch_absense_by_id(client: FlaskClient):
    response = client.patch("/api/absences/b20dfcbb-f121-41ef-bf96-cb988d68a35a", headers={"Authorization": "Bearer 1234"})
    mock_reponse = {
                    "absence_id": "b20dfcbb-f121-41ef-bf96-cb988d68a35a",
                    "date": "15/02/2020",
                    "justify": True,
                    "classroom": "1A",
                    "student": "Matheus",
                    "school_subject": "React"
                    }
    
    response_json: dict = response.get_json()
    
    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"