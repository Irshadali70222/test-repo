"""
main.py
-------
This is the main entry point for the Beginner Task Tracker CLI app.
It presents a menu to the user and handles user choices.
"""

from task_manager import (
    load_tasks,
    save_tasks,
    add_task,
    mark_task_completed,
    delete_task,
)


def display_tasks(tasks):
    """
    Displays the list of tasks with their index number and completion status.
    """
    if not tasks:
        print("\nYour task list is empty!")
        return

    print("\n--- YOUR TASKS ---")
    for i, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{i}. {status} {task['title']}")


def display_menu():
    """
    Displays the main menu options.
    """
    print("\n=========================")
    print("  BEGINNER TASK TRACKER  ")
    print("=========================")
    print("1. View all tasks")
    print("2. Add a new task")
    print("3. Mark task as completed")
    print("4. Delete a task")
    print("5. Exit")


def main():
    """
    Main loop for running the application.
    """
    tasks = load_tasks()
    print("Welcome to Beginner Task Tracker!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            display_tasks(tasks)

        elif choice == "2":
            title = input("Enter task title: ")
            if add_task(tasks, title):
                save_tasks(tasks)
                print(f"Task '{title.strip()}' added successfully!")
            else:
                print("Error: Task title cannot be empty.")

        elif choice == "3":
            display_tasks(tasks)
            if tasks:
                task_num_input = input("Enter task number to mark complete: ").strip()
                if task_num_input.isdigit():
                    task_num = int(task_num_input)
                    if mark_task_completed(tasks, task_num):
                        save_tasks(tasks)
                        print(f"Task {task_num} marked as completed!")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")

        elif choice == "4":
            display_tasks(tasks)
            if tasks:
                task_num_input = input("Enter task number to delete: ").strip()
                if task_num_input.isdigit():
                    task_num = int(task_num_input)
                    deleted_task = delete_task(tasks, task_num)
                    if deleted_task:
                        save_tasks(tasks)
                        print(f"Deleted task: '{deleted_task['title']}'")
                    else:
                        print("Invalid task number.")
                else:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("Thank you for using Beginner Task Tracker. Goodbye!")
            break

        else:
            print("Invalid option! Please choose a number between 1 and 5.")


if __name__ == "__main__":
    main()
