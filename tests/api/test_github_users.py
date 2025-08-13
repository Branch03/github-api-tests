import pytest

USERNAME_LIST = ["octocat", "torvalds", "mojombo"]

@pytest.mark.parametrize('username', USERNAME_LIST)
def test_username(base_url, session, username):
    r = session.get(f"{base_url}/users/{username}")
    assert r.status_code == 200
    data = r.json()
    assert "login" in data 
    assert data["login"] == username

def test_user_not_found(base_url, session,):
    r = session.get(f"{base_url}/users/{"chmo7741941"}")
    assert r.status_code == 404
