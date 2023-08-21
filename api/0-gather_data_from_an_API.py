#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID.
"""


import requests
import sys


def employee_todo(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = f"{base_url}/users/{employee_id}"
    todo = f"{base_url}/todos?userId={employee_id}"

    response_user = requests.get(user_id)
    response_todo = requests.get(todo)

    user_data = response_user.json()
    todo_data = response_todo.json()

    name_employee = user_data['name']

    todo_task = sum(1 for task in todo_data if task['completed'])
    total_task = len(todo_data)

    list_task_complete = [task['title']
                          for task in todo_data if task['completed']]

    print(f"Employee {name_employee} "
          f"is done with tasks ({todo_task}/{total_task}):")

    for title in list_task_complete:
        print(f"\t {title}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    employee_todo(employee_id)
