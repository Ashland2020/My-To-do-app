#from functions import get_todos,write_todos
import functions  # import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
user_prompt = "Type add, show, edit, complete or exit :"
print(now)


todos = []

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()
    if user_action.startswith("add") :
# List slicing
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith("show"):

        todos = functions.get_todos()

# REMOVE \n from the todos list
        new_todos = [item.strip('\n') for item in todos]

        for index,item in enumerate(new_todos):
            row = f"{index+1} -{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo : ")
            todos[number] = new_todo + '\n'
        except ValueError:
            print("Your command is not valid")
            continue
# Modify doto list:
        functions.write_todos(todos)

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            # Read the list again before remove record from it:

            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

    # After record removed we write the list to the file:
            functions.write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
            continue
    elif user_action.startswith("exit"):
         break
    else:
        print("Command is not valid !")
  #  if _ in user_action:
  #      print("You entered invalid command !!!")


        
print("Bye!")




