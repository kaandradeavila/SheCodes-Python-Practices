""" 
1. Create a new todo.txt file with some tasks you need to do
2. Display each item in a nice readable way using Python
"""

with open("todo_6.txt", "r") as file:
    lines = file.readlines()

    print("My To Do List:")
    for line in lines:
        print(f"- {line.strip()}")

file.close()