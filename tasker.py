import sys
import json
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) +1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }   
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {new_task["id"]})")

def list_tasks(status_filter=None):
    tasks = load_tasks()
    if status_filter:
        tasks = [task for task in tasks if task["status"] == status_filter]

    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        print(f"ID: {task['id']}")
        print(f"Description: {task['description']}")
        print(f"Status: {task['status']}")
        print(f"Created: {task['createdAt']}")
        print(f"Updated: {task['updatedAt']}")
        print("-" * 30)

def main():
    if len(sys.argv) < 2:
        print("Usage: task-cli [command] [arguments]")
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) > 2:
        description = " ".join(sys.argv[2:])
        add_task(description)
    elif command == "list":
        status_filter = sys.argv[2] if len(sys.argv) > 2 else None
        list_tasks(status_filter)
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()