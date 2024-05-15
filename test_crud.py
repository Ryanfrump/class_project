from fastapi.testclient import TestClient
from unittest.mock import patch
import pytest
from CRUD import app

client = TestClient(app)


class MockSession:
    def __init__(self):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

   
def mock_get_db():
    return MockSession()


@pytest.fixture
def patched_get_db():
    with patch("database.get_db", return_value=mock_get_db()) as mock:
        yield mock



def test_get_user(patched_get_db):
    response = client.get("/user")
    assert response.status_code == 200
    

def test_get_reward(patched_get_db):
    response = client.get("/reward")
    assert response.status_code == 200
   

def test_get_punishment(patched_get_db):
    response = client.get("/punishment")
    assert response.status_code == 200
    

def test_get_workout(patched_get_db):
    response = client.get("/workout")
    assert response.status_code == 200
    

def test_get_schedual(patched_get_db):
    response = client.get("/schedual")
    assert response.status_code == 200
    

def test_get_muscle_group(patched_get_db):
    response = client.get("/muscle_group")
    assert response.status_code == 200
    

def test_get_schedual_for_user(patched_get_db):
    response = client.get("/user/1/schedual")
    assert response.status_code == 404 or response.status_code == 200 

def test_get_workouts_for_muscle_group(patched_get_db):
    response = client.get("/workouts/1")
    assert response.status_code == 200  

def test_create_user(patched_get_db):
    
    user_data = {"first_name": "John", "last_name": "Doe", "age": 35}  

    
    response = client.post("/user", json=user_data)

    
    assert response.status_code == 200

    

def test_update_user(patched_get_db):
    
    user_id = 1  
    updated_data = {"name": "Updated Test User"}

    
    response = client.put(f"/user/{user_id}", json=updated_data)

    
    assert response.status_code == 404 or response.status_code == 200

    

def test_remove_user(patched_get_db):
    
    user_id = 1  

    
    response = client.delete(f"/user/{user_id}")

    
    assert response.status_code == 404 or response.status_code == 200
