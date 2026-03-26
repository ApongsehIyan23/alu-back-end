#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID from
JSONPlaceholder (https://jsonplaceholder.typicode.com).
"""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base = "https://jsonplaceholder.typicode.com"

    user_resp = requests.get(f"{base}/users/{employee_id}")
    user = user_resp.json()
    employee_name = user.get("name")

    todos_resp = requests.get(
        f"{base}/todos", params={"userId": employee_id})
    todos = todos_resp.json()

    completed = [t for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task.get("title")))
