from flask.testing import FlaskClient


def test_get_grades_by_student_id(client: FlaskClient):
    response = client.get("/api/grades/1d5225ef-5638-4397-9989-e604a2cceca0")
    mock_response = {
                    "name": "matheus",
                    "grades": [
                        {
                        "ativity": "codar",
                        "grade": 3.5,
                        "student_id": "1d5225ef-5638-4397-9989-e604a2cceca0",
                        "classrom_id": "51df51e0-00a7-49e3-9f2e-0405574f5c20"
                        }
                    ]
                    }
    
    response_json: dict = response.get_json()

    assert(response_json == mock_response), "Verificar se o retorno está correto"
    assert(type(response_json) is dict), "Verificar se está retornando um dict"
    assert(response.status_code == 200), "Verificar se o status code é OK"


def test_get_all_grades(client:FlaskClient):
    response = client.get("/api/grades")
    response_json: dict = response.get_json()
    assert(type(response_json) is list), "Verificar se está retornando um list"
    assert(type(response_json[0]) is dict), "Verificar se está retornando um dict"
    assert(response.status_code == 200), "Verificar se o status code é OK"
    assert(len(response_json) == 4), "O comprimento da resposta esta menor do que o esperado"

