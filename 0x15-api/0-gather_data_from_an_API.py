#!/usr/bin/python3
""" A py script that retrives a given employee informaton."""

import requests
from sys import argv
""" d request method used to fetch the url response"""


def get_employee_todo_progress(employee_id):
    """ the employee todo progress func."""
    try:
        # Define d base URL for d API
        base_url = "https://jsonplaceholder.typicode.com/"

        # Fetch user data
        user_details = requests.get(f"{base_url}users/{employee_id}")
        user_details.raise_for_status()
        user_data = user_details.json()
        employee_name = user_data.get('name')

        """ Now let fetch TODO list for an employee"""
        todos_reply = requests.get(f"{base_url}todos", params={
            'userId': employee_id
        })
        todos_reply.raise_for_status()
        json_todos_reply = todos_reply.json()

        """ Now let calculate atal and completed task."""
        total_tasks = len(json_todos_reply)
        completed_tasks = [
                task for task in json_todos_reply if task.get('completed')
        ]
        nos_completed_tasks = len(completed_tasks)

        """ we are to display the result now."""
        print(f"Employee {employee_name} is done with tasks("
              f"{nos_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"/t {task.get('title')}")

    except requests.RequestException as e:
        print(f"An error occured while fetching data: {e}")
    except KeyError as e:
        print(f"Missing expected data: {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage:script <employee_id>")
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Invalid employee ID. It must be an integer.")
