import pytest
from fastapi.testclient import TestClient
from app.main import app 
from app.test_db import init_db, drop_db, TestingSessionLocal
from app import models


@pytest.fixture(scope="function")
def test_client():
    init_db()
    db = TestingSessionLocal()
    # Add seed data (same as repository.py)
    db.add(models.FlightEvent(flight_number="A1", from_city="NYC", to_city="CHI", departure_time="2025-07-19T08:00:00", arrival_time="2025-07-19T10:00:00"))
    db.add(models.FlightEvent(flight_number="B2", from_city="CHI", to_city="LAX", departure_time="2025-07-19T11:30:00", arrival_time="2025-07-19T13:30:00"))
    db.add(models.FlightEvent(flight_number="C3", from_city="NYC", to_city="LAX", departure_time="2025-07-19T09:00:00", arrival_time="2025-07-19T12:00:00"))
    db.commit()
    db.close()
    yield TestClient(app)
    drop_db()


def test_journey_search_direct(test_client):
    response = test_client.get("/journeys/search", params={
        "from_city": "NYC",
        "to_city": "CHI",
        "date": "2025-07-19"
    })
    assert response.status_code == 200
    journeys = response.json()
    assert isinstance(journeys, list)
    assert journeys[0]["connections"] == 0
    assert journeys[0]["path"][0]["from"] == "NYC"
    assert journeys[0]["path"][0]["to"] == "CHI"

def test_journey_search_connection(test_client):
    response = test_client.get("/journeys/search", params={
        "from_city": "NYC",
        "to_city": "LAX",
        "date": "2025-07-19"
    })
    assert response.status_code == 200
    journeys = response.json()
    assert any(j["connections"] == 1 for j in journeys)
    assert all(j["path"][0]["from"] == "NYC" for j in journeys)
    assert all(j["path"][-1]["to"] == "LAX" for j in journeys)

def test_journey_search_no_results(test_client):
    response = test_client.get("/journeys/search", params={
        "from_city": "NYC",
        "to_city": "MEX",  # No such journey in seeds
        "date": "2025-07-19"
    })
    assert response.status_code == 200
    journeys = response.json()
    assert journeys == []

def test_journey_search_missing_params(test_client):
    # Omit one required param (e.g., to_city)
    response = test_client.get("/journeys/search", params={
        "from_city": "NYC",
        "date": "2025-07-19"
    })
    assert response.status_code == 400

    # Omit all params
    response = test_client.get("/journeys/search")
    assert response.status_code == 400