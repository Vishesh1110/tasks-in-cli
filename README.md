# tasks-in-cli

A Python CLI app to manage your todos without leaving the terminal. Add, update, delete, and mark tasks as complete — all from the command line.

---

## Prerequisites

- Python 3.x (see `.python-version` for the exact version)
- [`uv`](https://docs.astral.sh/uv/) — the package manager used by this project

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/Vishesh1110/tasks-in-cli.git
cd tasks-in-cli
```

### 2. Install dependencies

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock` to install the exact dependency versions into a virtual environment.

---

## Usage

Run the CLI using `uv run`:

```bash
uv run todocli.py --help
```

### Available Commands

| Command | Description |
|---|---|
| `add "<task>"` | Add a new todo item |
| `list` | List all todos |
| `update <id> "<new text>"` | Update an existing todo by ID |
| `delete <id>` | Delete a todo by ID |
| `complete <id>` | Mark a todo as complete |

### Examples

```bash
# Add a task
uv run todocli.py add "Buy groceries"

# List all tasks
uv run todocli.py list

# Mark task 1 as complete
uv run todocli.py complete 1

# Update task 2
uv run todocli.py update 2 "Buy groceries and cook dinner"

# Delete task 3
uv run todocli.py delete 3
```

---

## Database

Tasks are stored locally in `todos.db`, a SQLite database file. It is created automatically on first run — no setup required.