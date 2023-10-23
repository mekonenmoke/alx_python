#!/usr/bin/python3
"""A script that
using this REST API, for a given employee ID, returns information about his/her TODO list progress.
"""
import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    employee_name = response.json()['name']
    # Get employee's TODO list
    response = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id))
    todos = response.json()
    # Count completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    number_of_completed_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)
    # Print employee TODO list progress
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, number_of_completed_tasks, total_number_of_tasks))
    for todo in completed_tasks:
        print("\t{}".format(todo['title']))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print("Invalid employee ID. Please enter a valid integer.")
