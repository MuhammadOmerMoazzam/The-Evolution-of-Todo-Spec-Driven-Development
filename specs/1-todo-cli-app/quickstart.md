# Quickstart Guide: Evolution of Todo – Phase I: In-Memory Python Console App

## Prerequisites
- Python 3.11 or higher
- UV package manager

## Setup
1. Clone or download the repository
2. Navigate to the project directory
3. Install dependencies using UV:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -e .
   ```

## Running the Application
To start the todo application:
```bash
python -m src.todo
```

## Using the Application
Once the application starts, you'll see a menu with the following options:
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

### Adding a Task
1. Select option 1 from the menu
2. Enter the task title when prompted
3. Optionally enter a task description
4. The task will be added with a unique ID

### Viewing Tasks
1. Select option 2 from the menu
2. All tasks will be displayed with their ID, title, description, and completion status ([ ] for incomplete, [x] for complete)

### Updating a Task
1. Select option 3 from the menu
2. Enter the task ID you want to update
3. Enter the new title (or press Enter to keep the current title)
4. Enter the new description (or press Enter to keep the current description)

### Deleting a Task
1. Select option 4 from the menu
2. Enter the task ID you want to delete
3. Confirm the deletion when prompted

### Marking Task Complete/Incomplete
1. Select option 5 from the menu
2. Enter the task ID you want to toggle
3. The completion status will be toggled (incomplete to complete or vice versa)

## Example Workflow
1. Add a task: "Buy groceries" with description "Milk, bread, eggs"
2. View tasks to see your new task with ID 1
3. Mark task 1 as complete
4. Update task 1 to change the description
5. Add another task: "Walk the dog"
6. View tasks to see both tasks
7. Delete task 2 when completed

## Troubleshooting
- If you get a "command not found" error, ensure you're running Python from the correct virtual environment
- If the application crashes, check that you're entering valid inputs (e.g., numeric IDs when required)
- For type checking errors, run `mypy src/` to identify and fix issues