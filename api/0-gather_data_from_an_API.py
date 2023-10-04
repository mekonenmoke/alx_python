import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data['name']

    # Get employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Count completed tasks
    completed_tasks = [todo for todo in todos if todo['completed']]
    number_of_completed_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos)

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({number_of_completed_tasks}/{total_number_of_tasks}):")
    for todo in completed_tasks:
        print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print("Invalid employee ID. Please enter a valid integer.")
