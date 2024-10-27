import functions

import FreeSimpleGUI as sg

#from command_line_interface import todos

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")

# Each row in the GUI has to be a list in "layout" parameter

window = sg.Window('My To-Do Application',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))

while True:

    event, values = window.read()  # READ method associated with instance "window"
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)

        case sg.WINDOW_CLOSED:
            break


window.close()