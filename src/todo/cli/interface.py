"""
Console interface for the Todo application.

This module defines the CLI interface that allows users to interact with the todo list
through a text-based console interface.
"""

import logging
import sys
from typing import Optional
from ..core.services import InMemoryTodoRepository


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TodoCLIInterface:
    """
    CLI interface for the Todo application.

    This class provides methods to interact with the todo list through a text-based console.
    """

    def __init__(self) -> None:
        """Initialize the CLI interface with a repository instance."""
        self.repository = InMemoryTodoRepository()

    def display_menu(self) -> None:
        """Display the main menu options to the user."""
        print("\n--- Todo Application ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete/Incomplete")
        print("6. Exit")
        print("------------------------")

    def get_user_choice(self) -> str:
        """
        Get the user's menu choice.

        Returns:
            str: The user's menu choice
        """
        try:
            choice = input("Enter your choice (1-6): ").strip()
            return choice
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return "6"  # Exit option
        except EOFError:
            print("\nEnd of input detected. Exiting.")
            return "6"  # Exit option

    def add_task(self) -> None:
        """Add a new task to the todo list."""
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Error: Task title cannot be empty.")
                return

            description = input("Enter task description (optional): ").strip()
            task = self.repository.add_task(title, description)
            print(f"Task added successfully with ID: {task.id}")
            logger.info(f"Task added via CLI: ID {task.id}, Title: '{task.title}'")
        except ValueError as e:
            print(f"Error: {e}")
            logger.error(f"Error adding task: {e}")
        except Exception as e:
            print(f"Unexpected error occurred while adding task: {e}")
            logger.error(f"Unexpected error adding task: {e}")

    def view_tasks(self) -> None:
        """Display all tasks in the todo list."""
        try:
            tasks = self.repository.get_all_tasks()
            if not tasks:
                print("No tasks in the list.")
                return

            print("\n--- Tasks ---")
            for task in tasks:
                status = "[x]" if task.completed else "[ ]"
                print(f"{status} ID: {task.id} | Title: {task.title} | Description: {task.description}")
            print("-------------")
            logger.info(f"Displayed {len(tasks)} tasks to user")
        except Exception as e:
            print(f"Unexpected error occurred while viewing tasks: {e}")
            logger.error(f"Unexpected error viewing tasks: {e}")

    def update_task(self) -> None:
        """Update an existing task."""
        try:
            task_id_input = input("Enter task ID to update: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            logger.warning("Invalid task ID entered for update")
            return
        except Exception as e:
            print(f"Unexpected error occurred while getting task ID: {e}")
            logger.error(f"Unexpected error getting task ID for update: {e}")
            return

        # Check if task exists
        task = self.repository.get_task_by_id(task_id)
        if task is None:
            print(f"Error: Task with ID {task_id} not found.")
            logger.warning(f"Attempted to update non-existent task ID: {task_id}")
            return

        try:
            title_input = input(f"Enter new title (current: '{task.title}', press Enter to keep current): ").strip()
            description_input = input(f"Enter new description (current: '{task.description}', press Enter to keep current): ").strip()

            # Prepare update parameters
            title = title_input if title_input else None
            description = description_input if description_input else None

            # Update the task
            success = self.repository.update_task(task_id, title, description)
            if success:
                print("Task updated successfully.")
                logger.info(f"Task updated via CLI: ID {task_id}")
            else:
                print("Error: Failed to update task.")
                logger.error(f"Failed to update task via CLI: ID {task_id}")
        except Exception as e:
            print(f"Unexpected error occurred while updating task: {e}")
            logger.error(f"Unexpected error updating task ID {task_id}: {e}")

    def delete_task(self) -> None:
        """Delete a task from the todo list."""
        try:
            task_id_input = input("Enter task ID to delete: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            logger.warning("Invalid task ID entered for deletion")
            return
        except Exception as e:
            print(f"Unexpected error occurred while getting task ID: {e}")
            logger.error(f"Unexpected error getting task ID for deletion: {e}")
            return

        # Confirm deletion
        task = self.repository.get_task_by_id(task_id)
        if task is None:
            print(f"Error: Task with ID {task_id} not found.")
            logger.warning(f"Attempted to delete non-existent task ID: {task_id}")
            return

        try:
            confirm = input(f"Are you sure you want to delete task '{task.title}'? (y/N): ").strip().lower()
            if confirm != 'y':
                print("Task deletion cancelled.")
                logger.info(f"Task deletion cancelled for ID: {task_id}")
                return

            success = self.repository.delete_task(task_id)
            if success:
                print("Task deleted successfully.")
                logger.info(f"Task deleted via CLI: ID {task_id}, Title: '{task.title}'")
            else:
                print("Error: Failed to delete task.")
                logger.error(f"Failed to delete task via CLI: ID {task_id}")
        except Exception as e:
            print(f"Unexpected error occurred while deleting task: {e}")
            logger.error(f"Unexpected error deleting task ID {task_id}: {e}")

    def toggle_task_completion(self) -> None:
        """Toggle the completion status of a task."""
        try:
            task_id_input = input("Enter task ID to toggle: ").strip()
            if not task_id_input:
                print("Error: Task ID cannot be empty.")
                return

            task_id = int(task_id_input)
        except ValueError:
            print("Error: Invalid task ID. Please enter a number.")
            logger.warning("Invalid task ID entered for toggle completion")
            return
        except Exception as e:
            print(f"Unexpected error occurred while getting task ID: {e}")
            logger.error(f"Unexpected error getting task ID for toggle completion: {e}")
            return

        # Check if task exists
        task = self.repository.get_task_by_id(task_id)
        if task is None:
            print(f"Error: Task with ID {task_id} not found.")
            logger.warning(f"Attempted to toggle completion of non-existent task ID: {task_id}")
            return

        try:
            success = self.repository.toggle_task_completion(task_id)
            if success:
                new_status = "complete" if task.completed else "incomplete"
                print(f"Task marked as {new_status}.")
                logger.info(f"Task completion status toggled via CLI: ID {task_id}, Status: {task.completed}")
            else:
                print("Error: Failed to toggle task completion status.")
                logger.error(f"Failed to toggle task completion via CLI: ID {task_id}")
        except Exception as e:
            print(f"Unexpected error occurred while toggling task completion: {e}")
            logger.error(f"Unexpected error toggling task completion ID {task_id}: {e}")

    def run(self) -> None:
        """Run the main application loop."""
        print("Welcome to the Todo Application!")
        logger.info("Todo application started")
        try:
            while True:
                self.display_menu()
                choice = self.get_user_choice()

                if choice == "1":
                    self.add_task()
                elif choice == "2":
                    self.view_tasks()
                elif choice == "3":
                    self.update_task()
                elif choice == "4":
                    self.delete_task()
                elif choice == "5":
                    self.toggle_task_completion()
                elif choice == "6":
                    print("Thank you for using the Todo Application. Goodbye!")
                    logger.info("Todo application exited by user")
                    sys.exit(0)
                else:
                    print("Invalid choice. Please enter a number between 1 and 6.")
                    logger.warning(f"Invalid menu choice entered: {choice}")
        except KeyboardInterrupt:
            print("\n\nOperation cancelled by user. Goodbye!")
            logger.info("Todo application interrupted by user")
            sys.exit(0)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            logger.error(f"Unexpected error in main application loop: {e}")
            sys.exit(1)