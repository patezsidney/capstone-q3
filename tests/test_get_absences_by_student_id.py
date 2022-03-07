from flask.testing import FlaskClient

def test_get_absences_by_student_id(client: FlaskClient):
    response = client.get("/api/absences/2a465bd0-22cd-45e7-9fd1-142dee2cca78")
    mock_response = {
                    "name": "renato",
                    "absences": [
                                {
                                "date": "Sat, 15 Feb 2020 00:00:00 GMT",
                                "justify": False,
                                "classroom_id": "cf43d8ca-37a8-4140-bc97-32192e151a27"
                                }
                                ]
                    }
    
    response_json = response.get_json()

    assert(response_json == mock_response), "Verificar se o retorno está correto"


def test_status_code_get_absences_by_student_id(client: FlaskClient):
    response = client.get("/api/absences/2a465bd0-22cd-45e7-9fd1-142dee2cca78")

    assert(response.status_code == 200), "Verificar se o status code é OK"


def test_type_get_absences_by_student_id(client: FlaskClient):
    response = client.get("/api/absences/2a465bd0-22cd-45e7-9fd1-142dee2cca78")

    assert(type(response.get_json()) == dict), "Verificar se está retornando um dict"