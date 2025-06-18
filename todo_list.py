import os
tasks = []
file_path = "todo.txt"

def load_data():
    if os.path.exists(file_path):
        with open(file_path,"r") as f:
            for line in f:
                if "|" in line:
                    task_text, status = line.strip().split("|")
                    tasks.append({"task": task_text,"done": status == "done"})
        
def save_data():
    with open(file_path,"w") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['task']} | {status}\n")
def add_tasks():
    n_tasks = int(input("How many tasks you wants to add? "))
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
        open(file_path,"w").close()
        print("All tasks cleared!")