from fastapi.testclient import TestClient
from fastapi import HTTPException
from app.main import app, tasks
import app.main as main
client = TestClient(app)
def setup_function():
   tasks.clear()
   main.text_id = 1
def test_create_task():
   response = client.post("/tasks", json = {"title":"Learn FastAPI"})
   assert response.status_code == 201
   assert response.json() == {"id":1, "title": "Learn FastAPI", "completed": False}
def test_reject_empty_title():
   response = client.post("/tasks", json = {"title":" "})
   assert response.status_code == 400
   assert response.json()["detail"] == "Task title can not be empty"
def test_list_tasks():
   response = client.post("/tasks", json = {"title": "Write tests"})
   response = client.get("/tasks")
   assert response.status_code == 200
   assert len(response.json()) == 1   
def test_task_not_found():
   response = client.get("/tasks/999")
   assert response.status_code == 404
   assert response.json()["detail"] == "Task not found"
   #raise HTTPException(status_code=404,detail="Task not found")
