def add_task(tasks):
    #Adds a task to the to-do list.
    task = input("Enter task to add: ")#lets user add a task with input()function
    tasks.append(task)#adds a task to the list tasks with append() function
    print("Task added successfully!")


def display_tasks(tasks):
        #Displays all tasks in the to-do list.
    if not tasks:
        print("Your to-do list is empty.")#CHECKS IF LIST IS EMPTY AND 
        #displays a meesage if mit is
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")#displays list starting with number 1


def remove_task(tasks):
    #Removes a task from the to-do list.
    display_tasks(tasks)
    if not tasks:#checks is list is empty
        return

    while True:#HANDLES ERRORS with try and except blocks
        try:
            task_index = int(
                input("Enter the number of the task to remove: ")) - 1
            if 0 <= task_index < len(tasks):#removes task from list 
                #using list indices and del() function
                del tasks[task_index]
                print("Task removed successfully!")
                break
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    #main function that runs application
    tasks = []#creats empty list to store tasks.
#menu runs infinite loop untill user chooses option 4 to exit
    while True:
        print("welcome to shaneys simple to do list application")
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice: ")
#asks user to choose option with input() functiion
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break#ends the loop
        else:
            print("Invalid choice. Please try again.")


main()
