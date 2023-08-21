#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID.
"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = f"{base_url}/users/{employee_id}"
    todo = f"{base_url}/todos?userId={employee_id}"

    response_user = requests.get(user_id)
    response_todo = requests.get(todo)

    user_data = response_user.json()
    todo_data = response_todo.json()

    name = user_data['name']
    username = user_data['username']

    todo_done = sum(1 for task in todo_data if task['completed'])
    todo_count = len(todo_data)

    list_task_complete = [task['title']
                          for task in todo_data if task['completed']]

    completed_tasks = []

    for task in todo_data:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        completed_tasks.append(task_data)

        user_tasks_data = {
            str(employee_id): completed_tasks
        }

    with open(f"{employee_id}.json", "w") as jsonfile:
        json.dump(user_tasks_data, jsonfile)
