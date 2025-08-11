import requests

def test_get_repo():
    url = "https://api.github.com/repos/python/cpython"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "cpython"
