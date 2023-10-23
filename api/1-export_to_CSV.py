import csv
import requests
import sys

def get_employee_info(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    user_id = employee_data['id']
    username = employee_data['username']

    # Get employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()

    # Prepare data for CSV
    csv_data = []
    for todo in todos:
        task_completed_status = "True" if todo['completed'] else "False"
        task_title = todo['title']
        csv_data.append([user_id, username, task_completed_status, task_title])

    # Write data to CSV file
    with open(f"{user_id}.csv", "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(csv_data)

    print(f"Data exported to {user_id}.csv")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print("Invalid employee ID. Please enter a valid integer.")
