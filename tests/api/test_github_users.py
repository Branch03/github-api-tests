import pytest

USERNAME_LIST = ["octocat", "torvalds", "mojombo"]
INVALID_USERNAMES = ["", "@@@!!!"]

@pytest.mark.parametrize('username', USERNAME_LIST)
def test_username(base_url, session, username):
    r = session.get(f"{base_url}/users/{username}")
    
    assert r.status_code == 200

    assert r.headers["Content-Type"] == "application/json; charset=utf-8"
    
    data = r.json()

    expected_keys = {"login","id","node_id","url","type"}
    assert expected_keys.issubset(data.keys())

    assert isinstance(data["login"], str)
    assert isinstance(data["id"], int)
    assert isinstance(data["node_id"], str)
    assert isinstance(data["url"], str)
    assert isinstance(data["type"], str)
    
    assert data["login"] == username

def test_user_not_found(base_url, session,):
    r = session.get(f"{base_url}/users/chmo7741941")
    assert r.status_code >= 404

@pytest.mark.parametrize('username', INVALID_USERNAMES)
def test_invalid_usernames(base_url, session, username):
    r = session.get(f"{base_url}/users/{username}")
    assert r.status_code >= 400

def test_rate_limit(base_url, session):
    r = session.get(f"{base_url}/rate_limit")
    assert r.status_code == 200
    data = r.json()
    assert "rate" in data
    assert "resources" in data
    assert "core" in data["resources"]