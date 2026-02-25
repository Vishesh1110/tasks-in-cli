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
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting task at position: {position}")
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"Updating task at position: {position} with task: {task}, category: {category}")
    show()

@app.command()
def complete(position: int):
    typer.echo(f"marking task at position: {position} as complete")
    show()

@app.command()
def show():
    tasks = [("Todo1", "Study"), ("Todo2", "Exercise")]
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
        c = get_category_color(task[1])
        is_done_str = "✅" if True == 2 else "❌"
        table.add_row(str(idx), task[0], f"[{c}]{task[1]}[/{c}]", is_done_str)
    console.print(table)


if __name__ == "__main__":
    app()