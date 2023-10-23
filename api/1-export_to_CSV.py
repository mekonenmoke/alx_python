import requests
import csv
import sys

def get_employee_todo_progress(employee_id):
    # Get employee details
    employee_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = str(employee_data["id"])  # Convert USER_ID to string
    username = employee_data["username"]

    # Get employee TODO list
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)
    response = requests.get(todo_url)
    todos = response.json()

    # Export data to CSV
    csv_file_name = "{}.csv".format(user_id)
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        for todo in todos:
            task_completed_status = todo["completed"]  # TASK_COMPLETED_STATUS as boolean
            task_title = todo["title"]
            writer.writerow([user_id, username, task_completed_status, task_title])

    print("Data exported to: {}".format(csv_file_name))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
