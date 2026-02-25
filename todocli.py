import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import insert_todo, get_all_todos, delete_todo, update_todo, complete_todo

console = Console()

app = typer.Typer()

@app.command(short_help="Add a new task to the to-do list")
def add(task: str, category: str):
    typer.echo(f"adding task: {task}, {category}")
    todo = Todo(task, category)
    insert_todo(todo)
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting task at position: {position}")
    delete_todo(position-1)
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"Updating task at position: {position} with task: {task}, category: {category}")
    update_todo(position-1, task, category)
    show()

@app.command()
def complete(position: int):
    typer.echo(f"marking task at position: {position} as complete")
    complete_todo(position-1)
    show()

@app.command()
def show():
    tasks = get_all_todos()
    console.print("[bold-magneta]Todos[/bold-magneta]", "💻")
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Status", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {
            "Study": "cyan",
            "Exercise": "green",
            "Work": "yellow",
            "Other": "magenta"
        }
        if category in COLORS:
            return COLORS[category]
        return "white"

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = "✅" if task.status == 2 else "❌"
        table.add_row(str(idx), task.task, f"[{c}]{task.category}[/{c}]", is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()