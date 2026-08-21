from fastapi.testclient import TestClient

from src.api.main import app


client = TestClient(app)


def test_review_page_is_available():
    response = client.get("/items/review")

    assert response.status_code == 200
    assert "Review Jewelry Extraction" in response.text
