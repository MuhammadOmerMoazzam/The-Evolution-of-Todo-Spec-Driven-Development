# Data Model: Evolution of Todo – Phase I: In-Memory Python Console App

## Task Entity

**Definition**: Represents a single todo item in the application

**Fields**:
- `id: int` - Unique identifier for the task (auto-incremented)
- `title: str` - Title or short description of the task
- `description: str` - Detailed description of the task
- `completed: bool` - Status indicator (True for complete, False for incomplete)

**Validation Rules**:
- `id` must be a positive integer
- `title` must not be empty
- `completed` defaults to False when creating a new task

## Task Repository Interface

**Definition**: Interface for managing Task entities in memory

**Methods**:
- `add_task(title: str, description: str) -> Task` - Creates a new task with auto-incremented ID
- `get_all_tasks() -> List[Task]` - Returns all tasks in the repository
- `get_task_by_id(task_id: int) -> Optional[Task]` - Returns a specific task or None if not found
- `update_task(task_id: int, title: str = None, description: str = None) -> bool` - Updates task details, returns True if successful
- `delete_task(task_id: int) -> bool` - Deletes a task, returns True if successful
- `toggle_task_completion(task_id: int) -> bool` - Toggles the completion status, returns True if successful

## State Transitions

**Task Completion**:
- Initial state: `completed = False`
- Transition: User toggles completion status
- Final state: `completed = True` (or back to False)

## Relationships

- The TaskList is a simple collection of Task entities with no complex relationships between them
- Each Task has a unique ID that serves as its identifier within the system