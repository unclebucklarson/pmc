# Day 14: Organizing the code into modules
# Improving Code
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598196#overview
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598116#overview
# The next video 'is the most important of the course' watch it fresh
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598210#overview # Anatomy of python
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598220#overview # Code Experiments
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34598242#overview  # Intro to Git
#
# Modules Moving code to a different file
# Modules moving code to a sub folder
# Anatomy of Python: class's in python


import os
# Moved the functions to a separate file
# import just a specific function from a module
from functions import write_todos
# import the module and all of its functions, have to use dot notation to access functions
# this way its clear where the functions come from
import functions
import my_utils.utils

todo_file = "todos.txt"
todos = []

# check if file exists, if not 'open' it.
if not os.path.exists(todo_file):
    with open(todo_file, 'w') as f:
        pass

while True:
    # user_action = input("Type add <todo>, delete <index>, show, edit <index> or exit: ").strip()
    user_action = my_utils.utils.get_input()  # using a module in a sub folder

    # replacing match with if statements
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_todos()

        todos.append(todo + "\n")
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif user_action.startswith("delete"):

        todos = functions.get_todos()

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
        todos = functions.get_todos()

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
