#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID from
JSONPlaceholder (https://jsonplaceholder.typicode.com).
"""
import json
import sys
import urllib.request


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    base = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(base, employee_id)
    with urllib.request.urlopen(user_url) as response:
        user = json.loads(response.read().decode())
    employee_name = user.get("name")

    todos_url = "{}/todos?userId={}".format(base, employee_id)
    with urllib.request.urlopen(todos_url) as response:
        todos = json.loads(response.read().decode())

    completed = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task.get("title")))
