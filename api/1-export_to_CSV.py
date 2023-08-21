#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID.
"""


import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = f"{base_url}/users/{employee_id}"
    todo = f"{base_url}/todos?userId={employee_id}"
    todos_url = f"{base_url}/todos"

    response_user = requests.get(user_id)
    response_todo = requests.get(todo)

    user_data = response_user.json()
    todo_data = response_todo.json()

    name = user_data['name']
    username = user_data['username']

    todo_done = sum(1 for task in todo_data if task['completed'])
    todo_count = len(todo_data)

    task_list = [task['title']
                 for task in todo_data]

    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for task in todo_data:
            csvwriter.writerow([employee_id, username,
                                str(task["completed"]), task["title"]])
