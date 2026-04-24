from fastapi import FastAPI
from database import get_connection


app = FastAPI()


@app.get("/")
def tasks():
    return {"message": "Execution Data Platform running"}

@app.get("/tasks")
def get_tasks():
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

@app.post("/tasks")
def create_task(title: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id;",
        (title,)
    )

    task_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()

    return {"id": task_id, "title": title}

    