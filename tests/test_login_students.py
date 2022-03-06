def test_login_students_success(client):
    request_register_data = {
        "cpf": "12312312355",
        "password": "1234",
    }

    request_register_response = client.post("/api/students", json=request_register_data, follow_redirects=True )
    response_register_json: dict = request_register_response.get_json()
    request_login_data = {
        "cpf": response_register_json["cpf"], 
	    "password": request_register_data["password"]
    }

    request_login_response = client.post("/api/students/login", json=request_login_data, follow_redirects=True )

    assert( request_login_response.get_json().get("api_key")), "Verificar se retornou a api_key"
    assert (request_login_response.status_code == 200), "Verificar se o status code é OK"


def test_login_students_error_password(client):
    request_register_data = {
        "cpf": "12312312355",
        "password": "1235",
    }

    request_register_response = client.post("/api/students", json=request_register_data, follow_redirects=True )
    response_register_json: dict = request_register_response.get_json()
    request_login_data = {
        "cpf": "12312312355", 
	    "password": request_register_data["password"]
    }

    request_login_response = client.post("/api/students/login", json=request_login_data, follow_redirects=True )

    assert( request_login_response.get_json().get("msg") == "Invalid students id"), "Verificar se retornou a mensagem correta"
    assert(request_login_response.status_code == 401), "Verificar se o status code é Unauthorized"


def test_login_students_error_id(client):
    request_register_data = {
        "cpf": "12312312356",
        "password": "1235",
    }

    request_register_response = client.post("/api/students", json=request_register_data, follow_redirects=True )
    response_register_json: dict = request_register_response.get_json()
    request_login_data = {
        "cpf": response_register_json["cpf"], 
	    "password": "123"
    }

    request_login_response = client.post("/api/students/login", json=request_login_data, follow_redirects=True )

    assert(request_login_response.get_json().get("msg") == "Wrong password"), "Verificar se retornou a mensagem correta"
    assert(request_login_response.status_code == 401), "Verificar se o status code é Unauthorized"