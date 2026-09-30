"""
task_manager.py
----------------
This module contains helper functions to manage a simple list of tasks.
Each task is represented as a dictionary:
    {"title": "Task title", "completed": False}
"""

import json
import os


def load_tasks(filename="tasks.json"):
    """
    Loads tasks from a JSON file.
    If the file does not exist, returns an empty list.
    """
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            tasks = json.load(file)
            return tasks
    except json.JSONDecodeError:
        # If the file is empty or corrupted, return an empty list
        return []


def save_tasks(tasks, filename="tasks.json"):
    """
    Saves the list of tasks to a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks, title):
    """
    Adds a new task to the task list.
    Returns True if added successfully, False if title is empty.
    """
    cleaned_title = title.strip()
    if not cleaned_title:
        return False

    new_task = {
        "title": cleaned_title,
        "completed": False
    }
    tasks.append(new_task)
    return True


def mark_task_completed(tasks, index):
    """
    Marks the task at the given 1-based index as completed.
    Returns True if successful, False if index is invalid.
    """
    if index < 1 or index > len(tasks):
        return False

    tasks[index - 1]["completed"] = True
    return True


def delete_task(tasks, index):
    """
    Deletes the task at the given 1-based index.
    Returns the deleted task dictionary if successful, or None if index is invalid.
    """
    if index < 1 or index > len(tasks):
        return None

    return tasks.pop(index - 1)
