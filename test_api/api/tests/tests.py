import pytest

@pytest.mark.django_db
def test_get_req(client):
    response = client.get("http://127.0.0.1:8000/api/v1/users/")
    assert response.status_code == 200


