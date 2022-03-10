from flask.testing import FlaskClient


def test_get_absences_by_student_id(client: FlaskClient):
    response = client.get("/api/absences/2a465bd0-22cd-45e7-9fd1-142dee2cca78", headers={"Authorization": "Bearer 1234"})
    mock_response = [
                        {
                        "absence_id": "d98c6e17-d6ce-4432-bc31-b10418a7cf44",
                        "date": "15/02/2020",
                        "justify": False,
                        "classroom": "2A",
                        "student": "Renato",
                        "school_subject": "Node"
                        }
                    ]
    
    response_json = response.get_json()

    assert(response_json == mock_response), "Verificar se o retorno está correto"


def test_status_code_get_absences_by_student_id(client: FlaskClient):
    response = client.get("/api/absences/2a465bd0-22cd-45e7-9fd1-142dee2cca78", headers={"Authorization": "Bearer 1234"})

    assert(response.status_code == 200), "Verificar se o status code é OK"


def test_type_get_absences_by_student_id(client: FlaskClient):
    response = client.get("/api/absences/2a465bd0-22cd-45e7-9fd1-142dee2cca78", headers={"Authorization": "Bearer 1234"})

    assert(type(response.get_json()) == list), "Verificar se está retornando um dict"