import pytest

USERNAME_LIST = ["octocat", "torvalds", "mojombo"]
INVALID_USERNAMES = ["", "@@@!!!"]
EXPECTED_USER_KEYS = {"login", "id", "node_id", "url", "type"}

@pytest.mark.parametrize('username', USERNAME_LIST)
def test_username(base_url, session, username):
    r = session.get(f"{base_url}/users/{username}")
    
    assert r.status_code == 200

    assert r.headers["Content-Type"].startswith("application/json")
    
    data = r.json()

    assert EXPECTED_USER_KEYS.issubset(data.keys())

    assert isinstance(data["login"], str)
    assert isinstance(data["id"], int)
    assert isinstance(data["node_id"], str)
    assert isinstance(data["url"], str)
    assert isinstance(data["type"], str)
    
    assert data["login"] == username

def test_user_not_found(base_url, session,):
    r = session.get(f"{base_url}/users/chmo7741941")
    assert r.status_code == 404

@pytest.mark.parametrize('username', INVALID_USERNAMES)
def test_invalid_usernames(base_url, session, username):
    r = session.get(f"{base_url}/users/{username}")
    assert r.status_code == 404
