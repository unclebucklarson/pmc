
# https://3m.udemy.com/course/the-python-mega-course/learn/lecture/34597766#overview
# replacing match with if/elif/else statements (I prefer the match case...)
# left for lunch at time 505 in video

todo_file = "todos.txt"
todos = []

while True:
    user_action = input("Type add <todo>, delete <index>, show, edit <index> or exit: ").strip()

    # replacing match with if statements
    if "add" in user_action or "new" in user_action:

        with open(todo_file, 'r') as f:
            todos = f.readlines()

        # instructors solution
        todo = user_action[4:] # @9:23
        todos.append(todo + "\n")

        with open(todo_file, 'w') as f:
            f.writelines(todos)

    elif "delete" in user_action:

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

    elif "show" in user_action:
        with open(todo_file, 'r') as f:
            todos = f.readlines()

        for index, item in enumerate(todos):
            print(f"{index + 1}. {item.strip()}")

    elif "edit" in user_action:
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

    elif "exit" in user_action:
        break
    else:
        print("Invalid entry please try again")

print("Bye!")
