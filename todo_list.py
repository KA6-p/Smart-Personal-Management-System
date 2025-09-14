import os
tasks = []
TODO_FILE = "todo.txt"

def get_task_count():
    while True:
        try:
            count = int(input("How many tasks do you wants to add? "))
            if count > 0:
                return count
            else:
                print("Please enter a number greater than 0")
        except ValueError:
            print("Please enter a valid number")

def load_data():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE,"r") as f:
            for line in f:
                if "|" in line:
                    task_text, status = line.strip().split("|")
                    tasks.append({"task": task_text,"done": status == "done"})
        
def save_data():
    with open(TODO_FILE,"w") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['task']} | {status}\n")

def add_tasks():
    n_tasks = get_task_count()
    for i in range(n_tasks):
        task = input("Enter the task: ")
        tasks.append({"task": task, "done": False})
        print("Task added!")
        save_data()

def view_tasks():
    load_data()  
    if not tasks:
        print("No tasks available.")
        return
    print("Tasks:\n")
    for index, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{index + 1}. {task['task']} - {status}")

def done_tasks():
    load_data()
    view_tasks()
    task_index = int(input("Enter the task number to mark as done: ")) - 1
    if 0 <= task_index < len(tasks):
        tasks[task_index]["done"] = True
        print("Task marked as done!")
        save_data()
    else:
        print("Invalid task number.")                

def clear_tasks():
    ans = (input("Are you sure you want to clear all your tasks?(Y/N)")).upper()
    if ans == "Y":
        tasks.clear()
        open(TODO_FILE,"w").close()
        print("All tasks cleared!")