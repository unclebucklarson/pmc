
#https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34597748#overview
# recreated from memory 20221209

todo_file = "todos.txt"
todos = []

while True:
    user_action = input("Type add, delete, show, edit or exit: ").strip()

    match user_action:
        case "add" | "a":

            with open(todo_file, 'r') as f:
                todos = f.readlines()

            todos.append(input("Enter a todo: ") + '\n')

            with open(todo_file, 'w') as f:
                f.writelines(todos)

        case "delete" | "d":
            with open(todo_file, 'r') as f:
                todos = f.readlines()

            number = int(input("Number of todo to delete: "))
            number -= 1
            todos.pop(number)

            with open(todo_file, 'w') as f:
                f.writelines(todos)

        case "show" | "s":
            with open(todo_file, 'r') as f:
                todos = f.readlines()

            # list comprehension, strips new line from each item in todo list
            # new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")

        case "edit" | "ed":
            number = int(input("Number of todo to edit: "))
            number -= 1

            with open(todo_file, 'r') as f:
                todos = f.readlines()

            todos[number] = input("Enter the new todo: ") + '\n'

            with open(todo_file, 'w') as f:
                f.writelines(todos)

        case "exit" | "e":
            break
        case _:
            print("Invalid entry please try again")

print("Bye!")