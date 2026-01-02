"""
Task operations for the Todo application.

This module defines the InMemoryTodoRepository which manages Task entities in memory.
"""

import logging
from typing import List, Optional
from .models import Task


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class InMemoryTodoRepository:
    """
    Repository for managing Task entities in memory.

    This class provides methods to add, view, update, delete, and mark tasks as complete.
    All data is stored in memory and will be lost when the application exits.
    """

    def __init__(self) -> None:
        """Initialize the repository with an empty list of tasks and an ID counter."""
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        """
        Creates a new task with auto-incremented ID.

        Args:
            title (str): The title of the task
            description (str): The description of the task

        Returns:
            Task: The newly created task with assigned ID

        Raises:
            ValueError: If title is empty
        """
        if not title.strip():
            logger.error("Attempted to add task with empty title")
            raise ValueError("Task title cannot be empty")

        task = Task(
            id=self._next_id,
            title=title.strip(),
            description=description.strip() if description else "",
            completed=False
        )
        self._tasks.append(task)
        self._next_id += 1
        logger.info(f"Task added: ID {task.id}, Title: '{task.title}'")
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the repository.

        Returns:
            List[Task]: A list of all tasks
        """
        logger.info(f"Retrieved {len(self._tasks)} tasks")
        return self._tasks.copy()

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Returns a specific task or None if not found.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The task with the given ID or None if not found
        """
        for task in self._tasks:
            if task.id == task_id:
                logger.info(f"Task found: ID {task.id}")
                return task
        logger.warning(f"Task with ID {task_id} not found")
        return None

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Updates task details, returns True if successful.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str], optional): The new title for the task
            description (Optional[str], optional): The new description for the task

        Returns:
            bool: True if the task was updated, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            logger.error(f"Failed to update task: ID {task_id} not found")
            return False

        original_title = task.title
        original_description = task.description

        if title is not None:
            task.title = title.strip() if title.strip() else task.title
        if description is not None:
            task.description = description.strip() if description else task.description

        logger.info(f"Task updated: ID {task.id}, Title '{original_title}' -> '{task.title}'")
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task, returns True if successful.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was deleted, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            logger.error(f"Failed to delete task: ID {task_id} not found")
            return False

        self._tasks.remove(task)
        logger.info(f"Task deleted: ID {task.id}, Title: '{task.title}'")
        return True

    def toggle_task_completion(self, task_id: int) -> bool:
        """
        Toggles the completion status, returns True if successful.

        Args:
            task_id (int): The ID of the task to toggle

        Returns:
            bool: True if the task status was toggled, False if the task was not found
        """
        task = self.get_task_by_id(task_id)
        if task is None:
            logger.error(f"Failed to toggle task completion: ID {task_id} not found")
            return False

        new_status = not task.completed
        logger.info(f"Task completion toggled: ID {task.id}, Status: {not new_status} -> {new_status}")
        task.completed = new_status
        return True