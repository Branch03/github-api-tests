import pytest
import requests

@pytest.fixture 
def base_url():
    return "https://api.github.com"

@pytest.fixture
def session():
    session = requests.Session()
    yield session
    session.close()
