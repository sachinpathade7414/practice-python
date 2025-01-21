#to-do-list app
task = []
print("Welcome to the To-Do-List App")
def menu():
    print("1. Add task")
    print("2. Delete task")
    print("3. Update task")
    print("4. View tasks")
    print("5. Exit")
menu()
choice = int(input("Enter your choice:"))
while choice != 5:
    if choice == 1:
        print("Enter the task to be added:")
        task.append(input())
    elif choice == 2:
        print("Enter the task number to be deleted:")
        task_number = int(input())
        task.pop(task_number-1)
    elif choice == 3:
        print("Enter the task number to be updated:")
        task_number = int(input())
        print("Enter the updated task:")
        task[task_number-1] = input()
    elif choice == 4:
        print("Your tasks are:")
        for i in range(len(task)):
            print(i+1, task[i])
    else:
        print("Invalid choice")
    menu()
    choice = int(input("Enter your choice:"))















