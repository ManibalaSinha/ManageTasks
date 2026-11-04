from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
<<<<<<< HEAD

=======
>>>>>>> 9f92691 (test)
app = FastAPI(title="Task Management API")
   #in memory storage
tasks = []
task_id = 1
#request data validation
<<<<<<< HEAD
class TaskCreate(BaseModel):
   title: str

@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task:TaskCreate):
   global task_id 
   title = task.title.strip()  
   
   if not title:
      raise HTTPException( status_code=422, detail="Task title can not be empty")  
   new_task= {  
      "id": task_id,
      "title": title, "completed": False,   
   }
   tasks.append(new_task)
   task_id += 1 
   return new_task
 
=======
class TaskCreate(BaseModel): #validation
   title: str
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task:TaskCreate):
   global task_id
   title = task.title.strip()     
   if not title:
      raise HTTPException( status_code=400, detail="Task title can not be empty")  
   new_task= {"id": task_id, "title": title, "completed": False}
   tasks.append(new_task)
   task_id += 1
   return new_task 
>>>>>>> 9f92691 (test)
   #List all tasks
@app.get("/tasks")    
def get_tasks():
   return tasks
<<<<<<< HEAD

=======
>>>>>>> 9f92691 (test)
@app.get("/tasks/{task_id}")
def get_task(task_id:int):
   for task in tasks:
      if task["id"] == task_id:
         return task
   raise HTTPException(status_code=404, detail="Task not found")
<<<<<<< HEAD
     
=======
>>>>>>> 9f92691 (test)
