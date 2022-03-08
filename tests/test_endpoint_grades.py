from contextlib import redirect_stderr

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

    response_json = response.get_json()

    assert(response_json == mock_response), "Verificar se o retorno está correto"
    assert(type(response_json) is dict), "Verificar se está retornando um dict"
    assert(response.status_code == 200), "Verificar se o status code é OK"


def test_get_all_grades(client:FlaskClient):
    response = client.get("/api/grades")
    response_json = response.get_json()
    assert(type(response_json) is list), "Verificar se está retornando um list"
    assert(type(response_json[0]) is dict), "Verificar se está retornando um dict"
    assert(response.status_code == 200), "Verificar se o status code é OK"
    assert(len(response_json) == 4), "O comprimento da resposta esta menor do que o esperado"


def test_post_new_grade(client:FlaskClient):
    data ={
            "ativity": "debug",
            "grade": 10,
            "student_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20',
            "classrom_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20'
            }
    request_response = client.post("/api/grades",json=data, follow_redirects=True)
    assert (request_response.status_code == 201), "Verificar se o status code é OK"


def test_patch_grade(client:FlaskClient):
    data ={
            "ativity": "testando"
            }
    request_response = client.patch("/api/grades/14cff389-868d-4858-8e3b-466ab29c8137",json=data)
    grade = request_response.get_json()
    assert (data["ativity"] == grade["ativity"]), "Verificar se o ativity foi atualizada"
    assert (request_response.status_code == 202), "Verificar se o status code é OK"
