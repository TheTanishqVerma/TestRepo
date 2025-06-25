# Python To-Do List Manager

A simple **command-line to-do list manager** built in Python.

## Featues
- 📂 **Persistent Storage** — Tasks are saved into `tasks.txt` so they remain even after you close the app.
- 📜 **List-based management** — Uses Python lists to store and manage tasks.
- 🧹 **Input validation** — Handles invalid inputs gracefully (e.g. empty tasks, invalid task numbers).
- 🧠 **Error handling** — Catches errors like file-not-found automatically.

## File Structure
├── todo.py # Main Python program
├── tasks.txt # Generated file to save your tasks
├── README.md # Project documentation

## Requirements
- ✅ Python 3.x installed
- ✅ Visual Studio Code or any code editor
- ✅ Terminal or VS Code's built-in terminal

## How to Run
1. Clone or download this project into a folder.
2. Open the folder in **Visual Studio Code**.
3. Open the file `todo.py`.
4. Open the **Terminal** inside VS Code:
   - `Terminal` → `New Terminal` or press ``Ctrl + ` `` (backtick key)
5. Run the application:
   ```bash
   python todo.py

## Sample Output
=== To-Do List ===
1. View
2. Add
3. Remove
4. Exit
Choice: 2
Enter the task: Buy groceries
Added: "Buy groceries"

=== To-Do List ===
1. View
2. Add
3. Remove
4. Exit
Choice: 1

Your to-do list:
1. Buy groceries

##  Input Validation
1. ❌ Empty tasks cannot be added:

    Enter the task: 
    Task cannot be empty.

2. ❌ Invalid task numbers:

    Enter the task number to remove: 5
    Invalid task number!

3. ❌ Invalid menu choices:

   Choice: 9
   Invalid choice, please try again!