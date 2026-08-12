import json
import pytest
from app import create_app

@pytest.fixture()
def client(tmp_path, monkeypatch):
    import app.config as config
    data_file = tmp_path / "tasks.json"
    data_file.write_text("[]", encoding="utf-8")
    monkeypatch.setattr(config, "DATA_FILE", data_file)

    application = create_app()
    application.config["TESTING"] = True
    with application.test_client() as client:
        yield client

def test_health(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["success"] is True

def test_get_tasks(client):
    response = client.get("/api/tasks")
    assert response.status_code == 200
    assert response.get_json()["count"] == 0

def test_create_task(client):
    response = client.post(
        "/api/tasks",
        json={
            "title": "Prepare project submission",
            "description": "Create ZIP and upload to GitHub",
            "status": "pending"
        }
    )
    assert response.status_code == 201
    assert response.get_json()["data"]["id"] == 1

def test_validation(client):
    response = client.post("/api/tasks", json={"title": "Hi"})
    assert response.status_code == 400
    assert response.get_json()["success"] is False

def test_not_found(client):
    response = client.get("/api/tasks/999")
    assert response.status_code == 404
