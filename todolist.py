# todo.py
"""
A simple command-line To-Do List application that allows users to manage tasks.
"""

from typing import List


class Todo:
    """A simple To-Do list application that manages tasks in memory.

    This class provides basic task management functionality including adding,
    deleting, and viewing tasks. Tasks are stored in memory as a list.
    """

    def __init__(self) -> None:
        """Initialize a new Todo instance with an empty task list."""
        self.tasks: List[str] = []
        self.completed: List[str] = []

    def add_task(self, task: str) -> None:
        """Add a new task to the list.

        Args:
            task: The task description to add.

        Note:
            Prints a success message if the task is added,
            or an error message if the task is empty.
        """
        if task:
            self.tasks.append(task)
            print(f"Task '{task}' added successfully.")
        else:
            print("Task cannot be empty.")

    def delete_task(self, task: str) -> None:
        """Delete a task from the list.

        Args:
            task: The task description to delete.

        Note:
            Prints a success message if the task is deleted,
            or an error message if the task is not found.
        """
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' deleted successfully.")
        else:
            print(f"Task '{task}' not found.")

    def complete_task(self, task:str) -> None:
        """Complete a task from the list.

        Args:
            task: The task descripton to mark completed.

        Note:
            Prints a success message if the task is designated
            completed, or an error message if the task is not found.
        """
        if task in self.tasks:
            self.completed.append(task)
            self.tasks.remove(task)
            print(f"Task '{task}' successfully marked completed.")
        else:
            print(f"Task '{task}' not found.")

    def show_tasks(self) -> None:
        """Display all current tasks in a numbered list.

        Note:
            Prints a message if there are no tasks,
            or a numbered list of all tasks if any exist.
        """
        if not self.tasks:
            print("No tasks available.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def show_completed(self) -> None:
        """Display all completed tasks in a numbered list.

        Note:
            Prints a message if there are no tasks,
            or a numbered list of all completed tasks if any
            exist.
        """
        if not self.completed:
            print("No tasks completed.")
        else:
            print("Completed Tasks:")
            for i, task in enumerate(self.completed, start=1):
                print(f"{i}. {task}")

    def num_tasks(self) -> None:
        """Display the number of all active tasks.

        Note:
            Prints the number of tasks if there are any,
            or a message if there are none.
        """
        if not self.tasks:
            print("You have zero active tasks.")
        else:
            print(f"You have {len(self.tasks)} tasks.")

def main():
    """Run the interactive To-Do list application.

    This function provides a command-line interface for interacting
    with the Todo class. It continuously prompts the user for actions
    until they choose to quit.
    """
    todo = Todo()

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Mark Task Completed")
        print("3. Delete Task")
        print("4. Show Tasks")
        print("5. Show Completed Tasks")
        print("6. Show Number of Tasks")
        print("7. Quit")
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo.add_task(task)
        elif choice == "2":
            task = input("Enter the task: ")
            todo.complete_task(task)
        elif choice == "3":
            task = input("Enter the task to delete: ")
            todo.delete_task(task)
        elif choice == "4":
            todo.show_tasks()
        elif choice == "5":
            todo.show_completed()
        elif choice == "6":
            todo.num_tasks()
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
