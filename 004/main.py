
#
todoFile = "todos.txt" # file format is one todo per line
todos = []
with open (todoFile, 'a+') as file:
    todos = file.readlines()

while True:
    user_action = input("Type add, delete, show, edit or exit: ").strip()

    match user_action:
        case "add" | "a":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "delete" | "d":
            number = int(input("Number of todo to delete: "))
            number -= 1
            todos.pop(number)
        case "show" | "s":
            for index, item in enumerate(todos):
                print(f"[{index+1}]: {item}")
        case "edit" | "ed":
            number = int(input("Number of todo to edit: "))
            number -= 1
            todos[number] = input("Enter the new todo: ")
        case "exit" | "e":
            break
        case _:
            print("Invalid entry please try again")

print("Bye!")

