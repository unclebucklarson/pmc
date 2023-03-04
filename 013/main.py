# Day 13
# video URL https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598154#overview
#           https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598158#overview # Docstring code experiments
# Doc strings

import os


def get_todos(filepath="todos.txt"):
    """ Read a text file and return a list of todo items"""
    with open(filepath, 'r') as f:
        todos_list = f.readlines()
    return todos_list


def write_todos(todo_list, filepath="todos.txt"):
    """Write the todos items list to a text file"""
    with open(filepath, 'w') as f:
        f.writelines(todo_list)


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
        todo = user_action[4:]
        todos = get_todos()

        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos(todo_file)

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("delete"):

        todos = get_todos()

        index = user_action[7:]
        try:
            index = int(index)
            todos.pop(index - 1)
        except ValueError as e:
            print("An invalid value was entered. Please try again.")
        except IndexError as e:
            print("That was not a valid item number. Please try again.")

        write_todos(todos)

    elif user_action.startswith("edit"):
        todos = get_todos()

        index = user_action[4:]
        try:
            index = int(index) - 1
            old_todo = todos[index]  # need to access the indes to see if its valid
            todos[index] = input("Enter the new todo: ") + '\n'
        except ValueError as e:
            print("An invalid value was entered. Please try again.")
        except IndexError as e:
            print("That was not a valid item number. Please try again.")

        write_todos(todos)

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid entry please try again")

print("Bye!")
