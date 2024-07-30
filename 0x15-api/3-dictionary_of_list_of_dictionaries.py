#!/usr/bin/python3
""" Script to fetch all user tasks and export them in JSON format."""

import json
import requests


def fetch_employee_data():
    """Fetch user and task data, then save to JSON file."""
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    user_tasks = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks[user_id] = [
            {
                "username": username,
                "task": task['title'],
                "complete": task['completed']
            }
            for task in todos if task['userId'] == user_id
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(user_tasks, json_file)


if __name__ == "__main__":
    fetch_employee_data()
