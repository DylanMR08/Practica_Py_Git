import requests
import pytest
import json

url: str = "http://localhost:8000/"

@pytest.mark.skip(reason="Not necessary")
def test_read_root():
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == "HOLA"


def test_insert_person():
    data = json.dumps({"id":0,"name":"dsylan","lastname":"Mejia","email":"dyllan@gmail.com"})
    response = requests.post(f"{url}api/person/", data=data)
    assert response.status_code == 200