tasks = []
# display       -->
def display_tasks(tasks):
    if len(tasks) == 0:
        print("No Tasks !")
    else:
        for i, task in enumerate(tasks):
            print(f"{str(i+1)}. {task}")
                     
# add_tasks     -->
def add_task(tasks):
    task = input("Enter New Task : ")
    tasks.append(task)
    
# edit_task     -->
def edit_task(tasks):
    indx = int(input("Enter Task Number : "))-1
    if indx >= 0 and indx < len(tasks):
        task = input("Enter the edit of task : ")
        tasks[indx] = task
    else:
        print("Invalid number of task")
        
# remove_task   -->
def delete_task(tasks):
    indx = int(input("Enter Task Number : "))-1
    if indx >= 0 and indx < len(tasks):
        tasks.pop(indx)
    else:
        print("Invalid number of task")
        
# control_tasks -->
while True:
    print("""
          TO Do Lists Using Python
          -------------------------
          1. Add Task.
          2. Edit Task.
          3. Delete Task.
          4. Display Task.
          5. Quit.
          """)
    choice = int(input("Enter Yout Choice : "))
    if choice == 1:
        add_task(tasks)
    elif choice == 2:
        edit_task(tasks)
    elif choice == 3:
        delete_task(tasks)
    elif choice == 4:
        display_tasks(tasks)
    elif choice == 5:
        break
    else:
        print("This choice not allowed..\n")