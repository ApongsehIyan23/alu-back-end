#!/usr/bin/python3
"""
gathing data from an api
"""
import requests
import sys

if __name__ == "__main__":
    user_id = int(sys.argv[1])

    r1 = requests.get("https://jsonplaceholder.typicode.com/users")

    users = r1.json()

    r2 = requests.get("https://jsonplaceholder.typicode.com/todos")

    todos = r2.json()

    for user in users:
        if user.get("id") == user_id:
            name = user.get("name")

    total = 0
    done = 0
    task_done = []
    for todo in todos:
        if todo.get("userId") == user_id:
            total += 1
            if todo.get("completed"):
                task_done.append(todo.get("title"))
                done += 1

    print(f"Employee {name} is done with tasks({done}/{total}):")
    for task in task_done:
        print(f"\t {task}")