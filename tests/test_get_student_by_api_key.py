from flask.testing import FlaskClient


def test_get_student_by_api_key(client: FlaskClient):
    response = client.get("/api/students/profile", headers={"Authorization": 'Bearer 1230'})
    mock_reponse = {
                    "name": "felipe",
                    "contact_name": "Rosita",
                    "contact_email": "rosita@email.com",
                    "cpf": "11111111111",
                    "birth_date": "Sun, 20 Feb 2000 00:00:00 GMT",
                    "gender":"Feminino"
                    }
    
    response_json: dict = response.get_json()
    
    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"