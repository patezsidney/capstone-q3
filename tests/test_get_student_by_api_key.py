from flask.testing import FlaskClient


def test_get_student_by_api_key(client: FlaskClient):
    response = client.get("/api/students/profile", headers={"Authorization": 'Bearer 1231'})
    mock_reponse = {
            'birth_date': 'Sun, 20 Feb 2000 00:00:00 GMT',
            'contact_email': 'sirlei@email.com',
            'contact_name': 'Sirlei',
            'cpf': '11111111112',
            'gender': 'Feminino',
            'id': '1d5225ef-5638-4397-9989-e604a2cceca0',
            'name': 'matheus'
        }
    
    response_json: dict = response.get_json()
    
    assert(response_json == mock_reponse), "Verificar se o retorno está correto"
    assert (type(response_json) is dict), "Verificar se está retornando um dict"
    assert (response.status_code == 200), "Verificar se o status code é OK"
