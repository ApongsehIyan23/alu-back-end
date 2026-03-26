#!/usr/bin/python3
"""
Fetches and displays TODO list progress for a given employee ID from
JSONPlaceholder (https://jsonplaceholder.typicode.com).
"""
import requests
import sys

employee_id = int(sys.argv[1])

base = "https://jsonplaceholder.typicode.com"

user = requests.get(
    "{}/users/{}".format(base, employee_id)).json()
employee_name = user.get("name")

todos = requests.get(
    "{}/todos".format(base),
    params={"userId": employee_id}).json()

completed = [t for t in todos if t.get("completed")]

print("Employee {} is done with tasks({}/{}):".format(
    employee_name, len(completed), len(todos)))

for task in completed:
    print("\t {}".format(task.get("title")))
