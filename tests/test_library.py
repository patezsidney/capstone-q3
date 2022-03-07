def test_get_all_library(client):
    request_response = client.get("/api/library")
    print(request_response)
    assert (request_response.status_code == 200), "Verificar se o status code é ok"