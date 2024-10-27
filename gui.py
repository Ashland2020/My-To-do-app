import functions

import FreeSimpleGUI as sg


label = sg.Text("Type in a To-Do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window('My To-Do Application', layout=[[label], [input_box, add_button]])
window.read()  # READ method associated with instance "window"
window.close()