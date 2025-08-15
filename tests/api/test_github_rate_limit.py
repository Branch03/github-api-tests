def test_rate_limit(base_url, session):
    r = session.get(f"{base_url}/rate_limit")
    assert r.status_code == 200

    data = r.json()
    assert "rate" in data
    assert "resources" in data
    assert "core" in data["resources"]