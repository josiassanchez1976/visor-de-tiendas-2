import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient  # noqa: E402
from api_busqueda import app  # noqa: E402

client = TestClient(app)


def test_root_message():
    response = client.get("/")
    assert response.status_code == 200
    assert "API" in response.json().get("mensaje", "")
