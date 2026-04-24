from fastapi import FastAPI
from database import connection, cursor


app = FastAPI()


@app.get("/")
def tasks():
    cursor.execute
    return {"message": "Hello World"}

@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks;")
    rows= cursor.fetchall()
    tasks = []
    for row in rows:
        tasks.append({"id": row[0],"title":row[1]})

    return{"tasks": tasks}