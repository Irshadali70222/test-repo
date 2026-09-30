"""
test_task_manager.py
---------------------
Unit tests for task_manager functions.
"""

import os
import unittest
from task_manager import (
    load_tasks,
    save_tasks,
    add_task,
    mark_task_completed,
    delete_task,
)


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        """Runs before each test method."""
        self.test_filename = "test_tasks.json"
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def tearDown(self):
        """Runs after each test method."""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_add_task_success(self):
        tasks = []
        result = add_task(tasks, "Learn Python")
        self.assertTrue(result)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Learn Python")
        self.assertFalse(tasks[0]["completed"])

    def test_add_task_empty_title(self):
        tasks = []
        result = add_task(tasks, "   ")
        self.assertFalse(result)
        self.assertEqual(len(tasks), 0)

    def test_mark_task_completed(self):
        tasks = [{"title": "Buy groceries", "completed": False}]
        result = mark_task_completed(tasks, 1)
        self.assertTrue(result)
        self.assertTrue(tasks[0]["completed"])

    def test_mark_task_completed_invalid_index(self):
        tasks = [{"title": "Buy groceries", "completed": False}]
        result = mark_task_completed(tasks, 99)
        self.assertFalse(result)

    def test_delete_task(self):
        tasks = [
            {"title": "Task 1", "completed": False},
            {"title": "Task 2", "completed": False},
        ]
        deleted = delete_task(tasks, 1)
        self.assertEqual(deleted["title"], "Task 1")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Task 2")

    def test_delete_task_invalid_index(self):
        tasks = [{"title": "Task 1", "completed": False}]
        deleted = delete_task(tasks, 0)
        self.assertIsNone(deleted)

    def test_save_and_load_tasks(self):
        tasks = [{"title": "Save me", "completed": True}]
        save_tasks(tasks, self.test_filename)

        loaded_tasks = load_tasks(self.test_filename)
        self.assertEqual(loaded_tasks, tasks)


if __name__ == "__main__":
    unittest.main()
