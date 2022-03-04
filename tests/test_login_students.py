def test_login_students(client):
    response = client.get("/students/login")
    assert response.get_json()[''] == ''


def test_status_rota_login_stundets(client):
    response = client.get("/students/login")

    assert response.status_code == 200, "Status Incorreto"