import pytest

USERNAME_LIST = ["octocat", "torvalds", "mojombo"]
INVALID_USERNAMES = ["", "@@@!!!"]
EXPECTED_REPO_KEYS = {"id", "name", "full_name", "private", "html_url"}

@pytest.mark.parametrize('username',USERNAME_LIST)
def test_user_repos(base_url,session,username):
    response = session.get(f"{base_url}/users/{username}/repos")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data,list)

    if data:
        assert EXPECTED_REPO_KEYS.issubset(data[0].keys())

def test_user_not_found(base_url,session):
    response = session.get(f"{base_url}/users/hiyRlknbvj6754/repos")
    assert response.status_code == 404

@pytest.mark.parametrize('username', INVALID_USERNAMES)
def test_invalid_usernames(base_url, session, username):
    r = session.get(f"{base_url}/users/{username}/repos")
    assert r.status_code == 404
