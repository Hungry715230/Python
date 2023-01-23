import string

ToDoList = []

print("This is your personal To-Do list.\nYour actions are to add, remove, sort, view list and mark done.\nType 'help' for help\n")
while True:
    action = input("What action would you like to take?")
    if action.lower() == "help":
        print("To add type 'add'")
        print("To remove type 'remove'")
        print("To mark done type 'done'")
        print("To sort list type 'sort'")
        print("To view list type 'view' or type 'list'\n")
    if action.lower() == "add":
        add = input("\nWhat would you like to add?")
        ToDoList.append(add)
        print(f"{add} was added to your list.\n")
    if action.lower() == "list" or action.lower() == "view":
        for element in ToDoList:
            print(f"{element}")
        print(" ")
    if action.lower() == "sort":
        ToDoList.sort()
        print("\nYour list was sorted.\n")
    if action.lower() == "remove":
        removing = input("\nWhat would you like to remove?")
        removing = removing.lower()
        if removing in ToDoList:
            ToDoList.remove(removing)
            print(f"{removing} was removed.\n")
