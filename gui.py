import functions

import FreeSimpleGUI as sg

#from command_line_interface import todos

label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = functions.get_todos(), key = 'todos',
                                enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

# Each row in the GUI has to be a list in "layout" parameter

window = sg.Window('My To-Do Application',
                   layout=[[label],                     # First row of the GUI
                           [input_box, add_button],    # Second row of the GUI
                           [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:

    event, values = window.read()  # READ method associated with instance "window"
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value =values['todos'][0])



        case sg.WINDOW_CLOSED:
            break


window.close()