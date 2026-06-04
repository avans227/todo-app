#simply to-do app
tasks = []

with open("tasks.txt", "r") as file:
    for line in file:
        tasks.append(line.strip())

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter choice:")
    if choice == '1':
        task = input("Enter task:")
        tasks.append(task)
        with open ("tasks.txt", "a") as file:
            file.write           
        print(tasks)
    elif choice == '2':
        for task in tasks:
            print(task)
    elif choice == '3':
        break
    else:
        print("Invalid")

    
