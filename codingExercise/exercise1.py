import FreeSimpleGUI as sg
from bonus.convertes14 import convert


label1 = sg.Text("Enter feet: ")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches: ")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="white")

window = sg.Window("Convertor", layout=[[label1, input1],
                                        [label2, input2],
                                        [convert_button, output_label]])
while True:
    values = window.read()
    print(values)
    feets = float(values[1].get('feet'))
    inches = float(values[1].get('inches'))
    print("feets: "+ str(feets))
    print("inches: " + str(inches))
    result = convert(feets,inches)
    window["output"].update(value=str(result)+" m")


window.close()