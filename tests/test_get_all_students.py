def test_login_students(client):
    response = client.get("/students")
    assert response.get_json()[''] == ''


def test_status_rota_get_all_stundets(client):
    response = client.get("/students")

    assert response.status_code == 200, "Status Incorreto"