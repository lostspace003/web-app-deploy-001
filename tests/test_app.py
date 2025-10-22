from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "hello, jalal." in r.text.lower()

def test_health():
    r = client.get("/health")
    assert r.json() == {"status": "ok"}
