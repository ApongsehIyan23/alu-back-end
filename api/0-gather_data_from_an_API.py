#!/usr/bin/python3
"""Gather data from an API and display employee TODO list progress."""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(
        base_url, employee_id)).json()
    name = user.get("name")
    total = len(todos)
    done = [t for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        name, len(done), total))
    for task in done:
        print("\t {}".format(task.get("title")))