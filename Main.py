import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# Load existing tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    title = input("Task Title: ")
    description = input("Description: ")
    due_date = input("Due Date (YYYY-MM-DD): ")
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "status": "Pending"
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added successfully.")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"\n{i}. {task['title']} [{task['status']}]")
        print(f"   Description: {task['description']}")
        print(f"   Due Date: {task['due_date']}")

# Update a task's status or details
def update_task():
    tasks = load_tasks()
    view_tasks()
    index = int(input("\nEnter task number to update: ")) - 1
    if 0 <= index < len(tasks):
        print("1. Mark as Completed\n2. Edit Task")
        choice = input("Select option: ")
        if choice == "1":
            tasks[index]["status"] = "Completed"
        elif choice == "2":
            tasks[index]["title"] = input("New Title: ")
            tasks[index]["description"] = input("New Description: ")
            tasks[index]["due_date"] = input("New Due Date (YYYY-MM-DD): ")
        save_tasks(tasks)
        print("✅ Task updated.")
    else:
        print("❌ Invalid task number.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    index = int(input("\nEnter task number to delete: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("🗑️ Task deleted.")
    else:
        print("❌ Invalid task number.")

# Main menu
def main():
    while True:
        print("\n📋 TaskMate - Personal Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting TaskMate.")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
