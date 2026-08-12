tasks=[]

file=open("tasks.txt","r")
tasks=file.read().splitlines()
file.close()

while True:

    print("=====================================")
    print("       STUDENT TASK MANAGER")

    print("=====================================")
    print()
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice=input("Enter your choice:")

    if choice=="1":
        task=input("Enter your task:")
        tasks.append(task)

        file=open("tasks.txt","w")

        for task in tasks:
            file.write(task+"\n")

        file.close()

        print("Task Added Successfully!")
        
        print("Your Tasks:",tasks)

    elif choice=="2":
        print("Your Tasks:")
        print(tasks)

    elif choice=="3":
        if len(tasks)==0:
            print("no tasks found.")
        else:
            print("Your Tasks:")
            for task in tasks:
                print("-",task)
            complete_task=input("Enter task name to complete:")
            if complete_task in tasks:
                index=tasks.index(complete_task)
                tasks[index]=complete_task+"(Completed)"
                print("Task Completed Successfully!")
            else:
                print("Task Not Found!")

    elif choice=="4":
        print(tasks)
        delete_task=input("Enter task name to delete:")
        if delete_task in tasks:
            tasks.remove(delete_task)
            print("Task Deleted Successfully!")
        else:
            print("Task Not Found!")