import pytest
import requests
import time
from fastapi.testclient import TestClient
from apiserver import app  # Import your FastAPI app directly

# Option 1: Test against live server (requires server running)
testcases_live = [
    ("http://localhost:8000/add/2/2", 4, "Test addition of 2 and 2"),
    # ... other test cases ...
]

# Option 2: Test directly using FastAPI's TestClient (no server needed)
@pytest.fixture
def client():
    return TestClient(app)

testcases_direct = [
    ("/add/2/2", 4, "Test addition of 2 and 2"),
    # ... other test cases ...
]

# Test against live server
@pytest.mark.live
@pytest.mark.parametrize("url, expected, description", testcases_live)
def test_api_live(url, expected, description):
    try:
        response = requests.get(url)
        response.raise_for_status()
        result = response.json()["result"]
        assert result == expected, f"{description}. Expected {expected}, got {result}"
    except requests.exceptions.RequestException as e:
        pytest.fail(f"Connection error testing {url}: {str(e)}")

# Test directly using TestClient (recommended)
@pytest.mark.parametrize("endpoint, expected, description", testcases_direct)
def test_api_direct(client, endpoint, expected, description):
    response = client.get(endpoint)
    assert response.status_code == 200
    assert response.json()["result"] == expected, f"{description}. Expected {expected}, got {response.json()['result']}"