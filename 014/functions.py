
def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as f:
        todos_list = f.readlines()
    return todos_list


def write_todos(todo_list, filepath="todos.txt"):
    with open(filepath, 'w') as f:
        f.writelines(todo_list)

if __name__ == "__main__":
    print("Hello")
    print(get_todos())