# Day 10
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34597830#overview
# try/except continue exceptions
import os

todo_file = "todos.txt"
todos = []

# check if file exists, if not 'open' it.
if not os.path.exists(todo_file):
    with open(todo_file, 'w') as f:
        pass

while True:
    user_action = input("Type add <todo>, delete <index>, show, edit <index> or exit: ").strip()

    # replacing match with if statements
    if user_action.startswith("add"):

        with open(todo_file, 'r') as f:
            todos = f.readlines()

        # instructors solution
        todo = user_action[4:] # @9:23
        todos.append(todo + "\n")

        with open(todo_file, 'w') as f:
            f.writelines(todos)

    elif user_action.startswith("delete"):

        with open(todo_file, 'r') as f:
            todos = f.readlines()

        index = user_action[7:]
        try:
            index = int(index)
            todos.pop(index - 1)
        except ValueError as e:
            print("An invalid value was entered. Please try again.")
        except IndexError as e:
            print("That was not a valid item number. Please try again.")

        with open(todo_file, 'w') as f:
            f.writelines(todos)

    elif user_action.startswith("show"):
        with open(todo_file, 'r') as f:
            todos = f.readlines()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("edit"):
        with open(todo_file, 'r') as f:
            todos = f.readlines()

        index = user_action[4:]
        try:
            index = int(index) - 1
            old_todo = todos[index]  # need to access the indes to see if its valid
            todos[index] = input("Enter the new todo: ") + '\n'
        except ValueError as e:
            print("An invalid value was entered. Please try again.")
        except IndexError as e:
            print("That was not a valid item number. Please try again.")

        with open(todo_file, 'w') as f:
            f.writelines(todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid entry please try again")

print("Bye!")