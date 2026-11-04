from fastapi.testclient import TestClient
from app.main import app, tasks
import app.main as main
client = TestClient(app)
<<<<<<< HEAD

def setup_function():
   tasks.clear()
   main.text_id = 1

def test_create_task():
   response = client.post("/tasks", json={"title":"Learn FastAPI"})
   assert response.status_code == 201
   assert response.json() == {"id":1, "title": "Learn FastAPI", "completed": False}
def test_reject_empty_title():
   response = client.post("/tasks", json={"title":" "})
   assert response.status_code == 422
=======
def setup_function():
   tasks.clear()
   main.text_id = 1
def test_create_task():
   response = client.post("/tasks", json={"title":"Learn FastAPI"})
   assert response.status_code == 201  
def test_reject_empty_title():
   response = client.post("/tasks", json={"title":" "})
   assert response.status_code == 400
>>>>>>> 9f92691 (test)
   assert response.json()["detail"] == "Task title can not be empty"
def test_list_tasks():
   client.post("/tasks", json={"title": "Write tests"})
   response = client.get("/tasks")
   assert response.status_code == 200
<<<<<<< HEAD
   assert len(response.json())==1
def test_task_not_found():
   response = client.get("/tasks/999")
   assert response.status_code == 404
   assert response.json()["detail"] == "Task not found"
=======
   assert len(response.json())==1   
def test_task_not_found():
   response = client.get("/tasks/999")
   assert response.status_code == 404
   assert response.json()["detail"] == "Task not found"
>>>>>>> 9f92691 (test)
