
# reconstructing the todo app from memory
# using the match case
# in my version keeping todo's in memory, not reading and writing every time
# Started at 18:25 and completed, with my own twists (in memory, error checking) at 19:50.

import os

filename = "todos.txt"
todos = []

if os.path.exists(filename):
    with open(filename, "r") as file:
        todos = file.readlines()
else:
    print("didn't find the file.")

while True:
    action = input("Please enter what you would like to do (show, add, edit, delete, complete, quit): ").strip()

    match action:

        case "quit" | "q":
            with open(filename, "w") as file:
                for item in todos:
                    if 0 == len(item) or item == "\n":
                        continue
                    file.write(item.strip() + '\n')
            print("Thanks for using the todo lister.")
            break

        case "add" | 'a':
            todo = input("Please enter your todo: ").strip()
            todos.append(todo)

        case "show" | "s":
            if len(todos) == 0:
                print("No todo's to show. Please add some.")
            for index, item in enumerate(todos):
                print(f"{index+1}: {item.strip()}")

        case "edit" | "e":
            try:
                item_number = int(input("Enter number of item to edit: "))
            except ValueError as e:
                print("That was an invalid index, please try again")
                continue

            if len(todos) >= item_number > 0:  # Ensure the index is in range
                new_todo = input("Enter the new todo: ")
                todos[item_number-1] = new_todo
            else:
                print("That was not a valid item number, please try again.")

        case "delete" | "d":
            try:
                item_number = int(input("Enter number of item to edit: "))
            except Exception as e:
                print(f"That was an invalid index, please try again. The exception was {e}")
                continue
            if len(todos) >= item_number > 0:  # Ensure the index is in range
                todos.pop(item_number-1)
            else:
                print("That was not a valid item number, please try again.")
                continue
        case "complete" | "c":
            try:
                item_number = int(input("Enter number of item to edit: "))
            except Exception as e:
                print(f"That was an invalid index, please try again. The exception was {e}")
                continue
            if len(todos) >= item_number > 0:  # Ensure the index is in range
                ctodo = todos[item_number - 1]
                todos[item_number - 1] = "[COMPLETED] " + ctodo
            else:
                print("That was not a valid item number, please try again.")
                continue

        case _:
            print("That is an invalid selection or the functionality has not been implemented yet.")

print("Bye")
