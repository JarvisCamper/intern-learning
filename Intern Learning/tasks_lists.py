tasks = []
while True:
    choice =  input('\nmenu : 1. Add tasks, 2. View Tasks, 3.Exit')
    if choice == "1":
        tasks.append(input("Enter task: "))
        print("Task added!")
    elif choice =='2':
        print("\nYour Tasks" if tasks else "no tasks listed yet")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
