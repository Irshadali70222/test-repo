# Beginner Task Tracker

## Project name
Beginner Task Tracker

## Project description
Beginner Task Tracker is a lightweight, easy-to-understand command-line interface (CLI) application built in Python. It is designed specifically for beginners in programming to learn how tasks, data persistence (JSON), modular code structure, and command-line interactions work.

## Features
- **View Tasks**: Display all current tasks with clear completion status indicators (`[ ]` for pending, `[X]` for completed).
- **Add Tasks**: Easily create new task items.
- **Mark Complete**: Mark pending tasks as finished by selecting their task number.
- **Delete Tasks**: Remove unwanted tasks from the list.
- **Data Persistence**: Tasks are automatically saved to `tasks.json` so your data is saved even when you exit the app.

## Technologies used
- **Python 3**: Core programming language.
- **JSON**: Simple text-based data format for storing tasks locally.
- **unittest**: Built-in Python library for running automated unit tests.

## How to install/run the project
1. Ensure you have Python 3 installed on your computer. You can check by running:
   ```bash
   python3 --version
   ```
2. Download or clone this repository to your local machine.
3. Open a terminal or command prompt in the project root directory.
4. Run the application with the following command:
   ```bash
   python3 main.py
   ```

## How to use the project
When you run `python3 main.py`, an interactive menu will appear:

```text
=========================
  BEGINNER TASK TRACKER
=========================
1. View all tasks
2. Add a new task
3. Mark task as completed
4. Delete a task
5. Exit
```

- Type `1` and press Enter to view all tasks.
- Type `2` and press Enter, then type the title of your task to add it.
- Type `3` and press Enter, then enter the task number to mark it complete.
- Type `4` and press Enter, then enter the task number to delete it.
- Type `5` and press Enter to exit the application.

### Running Tests
To verify that everything works correctly, you can run the unit tests:
```bash
python3 -m unittest test_task_manager.py
```

## Future improvements
- Add task due dates and priorities (High, Medium, Low).
- Implement task search and filtering (e.g., view only completed tasks).
- Create a graphical user interface (GUI) using `tkinter`.
