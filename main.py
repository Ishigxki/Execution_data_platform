from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_connection
from pydantic import BaseModel

class Task(BaseModel):
    title: str

class TaskResponse(BaseModel):
    id: int
    title: str   


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)




@app.get("/")
def tasks():
    return {"message": "Execution Data Platform running"}

@app.get("/tasks")
def get_tasks() -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT id, title FROM tasks;")
        rows = cursor.fetchall()

        tasks = [{"id": row[0], "title": row[1]} for row in rows]
        return {"tasks": tasks}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()

@app.post("/tasks", response_model=TaskResponse)
def create_task(task: Task) -> dict:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id;",
        (task.title,)
    )

    task_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()

    return {"id": task_id, "title": task.title}

@app.delete("/tasks/{task_id}")
def remove(task_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tasks WHERE id = %s;", (task_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"id": task_id, "action": "removed"}
    