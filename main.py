import threading

import PySimpleGUI as sg
import Server as se
import Client as cl


def open_sender():

    send_layout = [[sg.Text("IP ADDRESS of the target")], [sg.Input()], [sg.Text("DESTINATION PORT")],
                   [sg.Input(default_text="5001")], [sg.Input(key='path'), sg.FileBrowse(key='filebrowser')],
                   [sg.Button("send file", key='send')],
                   [sg.ProgressBar(max_value=100, size=(60, 20), key='progressbar')]]
    send_window = sg.Window("Sending File through network", send_layout, modal=True)
    progressbar = send_window['progressbar']

    while True:
        send_event, send_values = send_window.read()
        if send_event == sg.WIN_CLOSED:
            break
        if send_event == 'send':
            print(send_values)
            cl.run_client(int(send_values[1]), str(send_values[0]), send_values['path'], progressbar)


def open_receiver():
    receiver_layout = [
        [sg.Text("Checking Connections :")], [sg.Text('Port number :'), sg.Input(key='port', default_text="5001"), sg.Button(button_text='Allow connections', key='connect')],
        [sg.Multiline(key='cmd', size=(30, 10))],
        [sg.ProgressBar(max_value=100, size=(60, 20), key='progressbar')]]
    receiver_window = sg.Window("Receiving File through network", receiver_layout, modal=True)
    progressbar = receiver_window['progressbar']

    while True:
        receiver_event, receiver_values = receiver_window.read()
        if receiver_event == sg.WIN_CLOSED:
            break
        if receiver_event == "connect":
            print(receiver_values)
            receiver_window.Element('cmd').print('Connections allowed')
            se.run_server(int(receiver_values['port']), progressbar)


layout = [[sg.Text("Home")], [sg.Button("Send")], [sg.Button("Receive")], [sg.Button("Parameters")]]
window = sg.Window(title="File Sender", layout=layout)

while True:
    event, values = window.read()
    if event == "Send":
        threading.Thread(target=open_sender()).start()
    if event == "Receive":
        threading.Thread(target=open_receiver()).start()
    if event == sg.WIN_CLOSED:
        break

window.close()
