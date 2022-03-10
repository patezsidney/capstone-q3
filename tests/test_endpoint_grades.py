from flask.testing import FlaskClient

headers = {"Authorization": "Bearer 1234"}

def test_get_grades_by_student_id(client: FlaskClient):
    response = client.get("/api/grades/1d5225ef-5638-4397-9989-e604a2cceca0",headers=headers)
    mock_response = [
            {
                'ativity': 'codar',
                'classrom': {'classroom_id': '51df51e0-00a7-49e3-9f2e-0405574f5c20','name': '1A'},
                'grade': 3.5,
                'student': {'name': 'matheus','student_id': '1d5225ef-5638-4397-9989-e604a2cceca0'}
                }
        ]

    response_json = response.get_json()

    assert(response_json == mock_response), "Verificar se o retorno está correto"
    assert(type(response_json) is list), "Verificar se está retornando um dict"
    assert(response.status_code == 200), "Verificar se o status code é OK"


def test_get_grades_by_student_id_error(client: FlaskClient):
    response = client.get("/api/grades/1d5225ef-5638-4397-9989-e604a2ccecb8",headers=headers)
    response_json = response.get_json()

    assert(response_json['msg'] == "student not found"), "Verificar se id invalido"
    assert(response.status_code == 404), "Verificar se o status code é NOT FOUND"


def test_get_all_grades(client:FlaskClient):
    response = client.get("/api/grades",headers=headers)
    response_json = response.get_json()
    assert(type(response_json) is list), "Verificar se está retornando um list"
    assert(type(response_json[0]) is dict), "Verificar se a lista contem um dict"
    assert(response.status_code == 200), "Verificar se o status code é OK"
    assert(len(response_json) == 4), "O comprimento da resposta esta menor do que o esperado"


def test_get_grades_classroom(client:FlaskClient):
    response = client.get("/api/grades?classroom=51df51e0-00a7-49e3-9f2e-0405574f5c20",headers=headers)
    response_json = response.get_json()
    assert(type(response_json) is list), "Verificar se está retornando um list"
    assert(type(response_json[0]) is dict), "Verificar se a lista contem um dict"
    assert(response.status_code == 200), "Verificar se o status code é OK"


def test_get_all_grades_error(client:FlaskClient):
    response = client.get("/api/grades?classroom=51df51e0-00a7-49e3-9f2e-0405574f5c56",headers=headers)
    response_json = response.get_json()
    assert(response_json['msg'] == "classroom id not found"), "Verificar se a msg e classroom id not found"
    assert(response.status_code == 404), "Verificar se o status code é NOT FOUND"


def test_post_new_grade(client:FlaskClient):
    mock= {
            'ativity': 'debug',
            'classrom': {'classroom_id': '51df51e0-00a7-49e3-9f2e-0405574f5c20', 'name': '1A'},
            'grade': 10.0, 'student': {'name': 'felipe','student_id': '51df51e0-00a7-49e3-9f2e-0405574f5c20'}
            }
    data ={
            "ativity": "debug",
            "grade": 10,
            "student_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20',
            "classrom_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20'
            }
    response = client.post("/api/grades",json=data, follow_redirects=True,headers=headers)
    response_json = response.get_json()
    assert(response_json == mock), "Verificar se o retorno está correto"
    assert (response.status_code == 201), "Verificar se o status code é CREATED"


def test_post_new_grade_error(client:FlaskClient):
    espected = {
            "error": "incorrect key(s)",
            "expected to be in": [
                "ativity",
                "grade",
                "student_id",
                "classrom_id"
                ],
            "received": [
                "ativit",
                "grade",
                "student_id",
                "classrom_id"
                ]
            }
    data ={
            "ativit": "debug",
            "grade": 10,
            "student_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20',
            "classrom_id": '51df51e0-00a7-49e3-9f2e-0405574f5c20'
            }
    response = client.post("/api/grades",json=data, follow_redirects=True,headers=headers)
    response_json = response.get_json()
    assert(espected == response_json), "Verificar se o retorno está como o esperado"
    assert (response.status_code == 400), "Verificar se o status code é BAD REQUEST"


def test_patch_grade(client:FlaskClient):
    data ={
            "ativity": "testando"
            }
    request_response = client.patch("/api/grades/14cff389-868d-4858-8e3b-466ab29c8137",json=data,headers=headers)
    grade = request_response.get_json()
    assert (data["ativity"] == grade["ativity"]), "Verificar se o ativity foi atualizada"
    assert (request_response.status_code == 202), "Verificar se o status code é OK"


def test_patch_grade_error(client:FlaskClient):
    data ={
            "ativity": "testando"
            }
    response = client.patch("/api/grades/14cff389-868d-4858-8e3b-466ab29c8154",json=data,headers=headers)
    grade = response.get_json()
    assert (grade["msg"] == "id not found"), "Verificar se a msg e id not found"
    assert(response.status_code == 404), "Verificar se o status code é NOT FOUND"