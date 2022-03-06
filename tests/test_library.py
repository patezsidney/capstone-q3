def test_get_all_library(client):
    request_response = client.get("/api/library")

    assert (request_response.status_code == 200), "Verificar se o status code é ok"