#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """Fetch and display employee TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"

    user_res = requests.get(f"{base_url}/users/{employee_id}")
    todos_res = requests.get(f"{base_url}/todos", params={"userId": employee_id})

    user = user_res.json()
    todos = todos_res.json()

    employee_name = user.get("name")
    total = len(todos)
    done = [t for t in todos if t.get("completed")]
    num_done = len(done)

    print(f"Employee {employee_name} is done with tasks({num_done}/{total}):")
    for task in done:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)