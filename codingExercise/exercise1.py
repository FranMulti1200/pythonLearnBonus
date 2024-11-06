import PySimpleGUI as sg
from bonus.convertes14 import convert

sg.theme("Black")


label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")
exit_button = sg.Button("Exit")

window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button, exit_button, output_label]],
                                        font=('Helvetica', 16))
while True:
    event, values = window.read()
    match event:
        case "Convert":
            try:
                print(values)
                feets = float(values['feet'])
                inches = float(values['inches'])
                print("feets: "+ str(feets))
                print("inches: " + str(inches))
                result = convert(feets,inches)
                window["output"].update(value=str(result)+" m")
            except ValueError:
                sg.popup("Please provide two numbers", font=('Helvetica', 16))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()