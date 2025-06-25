TASKS_FILE = "tasks.txt"


def load_tasks():
    """Load tasks from file into a list."""
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save all tasks into file."""
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("\nYour to-do list:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    print()  # blank line for readability


def add_task(tasks):
    """Add a new task."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f'Added task: "{task}"\n')
    else:
        print("Task cannot be empty.\n")


def remove_task(tasks):
    """Remove a task by its number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        index = int(input("Enter the task number to remove: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks(tasks)
            print(f'Removed task: "{removed}"\n')
        else:
            print("Invalid task number!\n")
    except ValueError:
        print("Please enter a valid number!\n")


def main():
    """Main loop for the to-do list application."""
    tasks = load_tasks()

    while True:
        print("=== To-Do List Manager ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!\n")


if __name__ == "__main__":
    main()
