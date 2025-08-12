import pytest

@pytest.mark.parametrize('username', ["octocat", "torvalds", "mojombo"])
def test_username(base_url, session, username):
    url = base_url + "/users/" + username
    r = session.get(url)
    assert r.status_code == 200
    data = r.json()
    assert "login" in data 
    assert data["login"] == username

def test_user_not_found(base_url, session,):
    url = base_url + "/users/" + "chmo5839287822"
    r = session.get(url)
    assert r.status_code == 404
    