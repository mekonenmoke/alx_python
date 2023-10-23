import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = employee_data["id"]
    username = employee_data["username"]

    # Get employee TODO list
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    response = requests.get(todo_url)
    todos = response.json()

    # Export data to CSV
    csv_file_name = "{}.csv".format(user_id)
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for todo in todos:
            task_completed_status = "True" if todo["completed"] else "False"
            task_title = todo["title"]
            writer.writerow([user_id, username, task_completed_status, task_title])

    print("Data exported to: {}".format(csv_file_name))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 1-expoert_to_CSV.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
