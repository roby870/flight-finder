import pytest
from fastapi.testclient import TestClient
from app.main import app 
from app.test_db import init_db, drop_db, TestingSessionLocal
from app import models


@pytest.fixture(scope="function")
def test_client():
    init_db()
    db = TestingSessionLocal()
    #Add data
    #
    db.close()
    yield TestClient(app)
    drop_db()
