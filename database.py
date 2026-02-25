import sqlite3
from typing import List
import datetime
from model import Todo

conn = sqlite3.connect('todos.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS todos
                 (task TEXT NOT NULL,
                  category TEXT NOT NULL,
                  date_added TEXT NOT NULL,
                  date_completed TEXT,
                  status INTEGER NOT NULL,
                  position INTEGER)''')

create_table()

def insert_todo(todo: Todo):
    c.execute('select count(*) FROM todos')
    count = c.fetchone()[0]
    todo.position = count if count else 0
    with conn:
        c.execute("INSERT INTO todos VALUES (:task, :category, :date_added, :date_completed, :status, :position)",
                  {'task': todo.task, 'category': todo.category, 'date_added': todo.date_added,
                   'date_completed': todo.date_completed, 'status': todo.status, 'position': todo.position})

def get_all_todos() -> List[Todo]:
    c.execute("SELECT * FROM todos")
    rows = c.fetchall()
    todos = []
    for row in rows:
        todos.append(Todo(*row))
    return todos

def delete_todo(position):
    c.execute("SELECT count(*) FROM todos")
    count = c.fetchone()[0]

    with conn:
        c.execute("DELETE FROM todos WHERE position=:position", {'position': position})
        for pos in range(position + 1, count):
            change_position(pos, pos - 1, False)

def change_position(old_position: int, new_position: int, commit=True):
    c.execute("UPDATE todos SET position=:new_position WHERE position=:old_position",
              {'new_position': new_position, 'old_position': old_position})
    if commit:
        conn.commit()

def update_todo(position: int, task: str = None, category: str = None):
    with conn:
        if task is not None and category is not None:
            c.execute("UPDATE todos SET task = :task, category=:category WHERE position=:position", {'task': task, 'category': category, 'position': position})
        elif task is not None:
            c.execute("UPDATE todos SET task = :task WHERE position=:position", {'task': task, 'position': position})
        elif category is not None:
            c.execute("UPDATE todos SET category=:category WHERE position=:position", {'category': category, 'position': position})
        conn.commit()

def complete_todo(position: int):
    with conn:
        c.execute("UPDATE todos SET status=2, date_completed=:date_completed WHERE position=:position",
                  {'date_completed': datetime.datetime.now().isoformat(), 'position': position})
        conn.commit()