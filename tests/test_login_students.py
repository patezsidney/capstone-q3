from flask.testing import FlaskClient

def test_login_students_success(client: FlaskClient):
    request_login_data = {
        "cpf": "11111111111", 
	    "password": "1234"
    }

    request_login_response = client.post("/api/students/login", json=request_login_data, follow_redirects=True )

    assert( request_login_response.get_json().get("api_key")), "Verificar se retornou a api_key"
    assert (request_login_response.status_code == 200), "Verificar se o status code é OK"


def test_login_students_error_password(client: FlaskClient):
    request_login_data = {
        "cpf": "11111111111", 
	    "password": "1235"
    }

    request_login_response = client.post("/api/students/login", json=request_login_data, follow_redirects=True )

    # assert( request_login_response.get_json().get("msg") == "Invalid employee id"), "Verificar se retornou a mensagem correta"
    assert(request_login_response.status_code == 401), "Verificar se o status code é Unauthorized"


def test_login_students_error_cpf(client: FlaskClient):
    request_login_data = {
        "cpf": "11111111122", 
	    "password": "1234"
    }

    request_login_response = client.post("/api/students/login", json=request_login_data, follow_redirects=True )

    # assert(request_login_response.get_json().get("msg") == "Wrong password"), "Verificar se retornou a mensagem correta"
    assert(request_login_response.status_code == 401), "Verificar se o status code é Unauthorized"