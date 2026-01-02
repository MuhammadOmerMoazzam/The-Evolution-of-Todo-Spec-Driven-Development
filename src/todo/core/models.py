"""
Task model for the Todo application.

This module defines the Task dataclass which represents a single todo item
with attributes: unique ID, title, description, and completion status.
"""

from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single todo item with attributes: unique ID, title, description, and completion status.
    
    Attributes:
        id (int): Unique identifier for the task (auto-incremented)
        title (str): Title or short description of the task
        description (str): Detailed description of the task
        completed (bool): Status indicator (True for complete, False for incomplete)
    """
    id: int
    title: str
    description: str
    completed: bool = False