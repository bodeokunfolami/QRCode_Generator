import PySimpleGUI as sg
import qrcode

sg.theme('BlueMono')
font = ('Monaco', 18)

qr_image = [sg.Image('', key='-QRCODE-')]

layout = [
    [sg.Text('Enter URL:')],
    [sg.Input('', key='-URL-')],
    [sg.Column([qr_image], justification='center')],
    [sg.Button('Generate', key='-submit-', expand_x=True)]
]

window = sg.Window('QR Code Generator', layout, font=font)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-submit-':
        url = values['-URL-']
        if url:
            img = qrcode.make(url)
            img.save('qr.png')
            window['-QRCODE-'].update('qr.png')
window.close()

print(sg.theme_list())