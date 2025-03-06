import sqlite3


def get_connection_db():
    conn = sqlite3.connect("todo.db")

    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_connection_db()
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            due_date TEXT NOT NULL ,
            status TEXT NOT NULL CHECK(status IN ('未着手', '進行中', '完了')),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )

"""
    )


def get_tasks():
    conn = get_connection_db()
    c = conn.cursor()
    tasks = c.execute("SELECT * FROM tasks").fetchall()
    c.close()
    return tasks


def add_task(title, content, due_date, status):
    conn = get_connection_db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO tasks (title, content, due_date, status) VALUES (?, ?, ?, ?)",
        (
            title,
            content,
            due_date,
            status,
        ),
    )
    conn.commit()
    c.close()


def show_task(id):
    conn = get_connection_db()
    c = conn.cursor()
    task = c.execute("SELECT * FROM tasks WHERE id = ?", (id,)).fetchone()
    c.close()
    return task


def edit_task(id, title, content, due_date, status):
    conn = get_connection_db()
    c = conn.cursor()
    c.execute(
        "UPDATE tasks SET title = ?,content = ?, due_date = ?, status = ?,updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (
            title,
            content,
            due_date,
            status,
            id,
        ),
    )
    conn.commit()
    c.close()


def delete_task(id):
    conn = get_connection_db()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    c.close
