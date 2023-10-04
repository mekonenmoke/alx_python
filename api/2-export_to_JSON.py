import requests
import json
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

    # Prepare data for JSON
    json_data = {
        "USER_ID": [{"task": todo['title'], "completed": todo['completed'], "username": username} for todo in todos]
    }

    # Write data to JSON file
    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)

    print(f"Data exported to {user_id}.json")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_info(employee_id)
        except ValueError:
            print("Invalid employee ID. Please enter a valid integer.")
