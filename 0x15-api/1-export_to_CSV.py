#!/usr/bin/python3
"""Exports TODO list data for a given employee ID to a CSV file."""

import csv
import requests
from sys import argv


def export_todo_to_csv(employee_id):
    """Fetches TODO list data and exports it to a CSV file."""
    try:
        # Define the base URL for the API
        base_url = "https://jsonplaceholder.typicode.com/"

        # Fetch user data
        user_response = requests.get(f"{base_url}users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        username = user_data.get('username')

        # Fetch TODO list data
        todos_response = requests.get(f"{base_url}todos", params={
            'userId': employee_id
        })
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Prepare CSV file name
        csv_filename = f"{employee_id}.csv"

        # Write data to CSV file
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL)
            for task in todos_data:
                writer.writerow([
                    employee_id,
                    username,
                    str(task.get('completed')),
                    task.get('title')
            ])

        print(f"Data exported successfully to {csv_filename}")

    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
    except KeyError as e:
        print(f"Missing expected data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee_id>")
    else:
        try:
            employee_id = int(argv[1])
            export_todo_to_csv(employee_id)
        except ValueError:
            print("Invalid employee ID. It must be an integer.")
