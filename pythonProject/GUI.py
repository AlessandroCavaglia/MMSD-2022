import PySimpleGUI as sg
from pathlib import Path
from parse_input import runModel
import os

import output

from pythonProject.costants import MODEL, MODEL_MAPPING, ADVANCED_SETTINGS

print = sg.Print


def main():
    advanced_settings = ADVANCED_SETTINGS
    sg.theme("DarkBlue3")
    sg.set_options(font=("Microsoft JhengHei", 16))
    font_title = ("Microsoft JhengHei", 25, 'bold')
    layout = [
        [
            [sg.Text('Modello di ottimizzazione calendario Esami', font=font_title)],
            [sg.T('Model Input     '), sg.Input(key='-INPUT-'),
             sg.FileBrowse(file_types=(("Excel", "*.xlsx"), ("ALL Files", "*.*")))],
            [sg.T('Output folder  '), sg.Input(key='-OUTPUT-'),
             sg.FolderBrowse()],
            [sg.T('Choose Model'), sg.Combo(MODEL, size=20, default_value='Default Model', readonly=True, key='_MODEL_'),
             sg.Button("Advanced settings",key='advanced_settings'),sg.Button("Close Advanced settings", key='close_advanced_settings', visible=False)],
            [sg.T('Time limit (M)    ', key='time_limit_text', visible=False),
             sg.Input(key='time_limit_input', size=20, default_text=ADVANCED_SETTINGS['time_limit'], visible=False)],
            [sg.T('Tolleranza Gap [0,1]    ', key='gap_tollerance_text', visible=False),
             sg.Input(key='gap_tollerance', size=20, default_text=ADVANCED_SETTINGS['gap_tollerance'], visible=False)],
            [sg.T('Output folder  ', visible=False), sg.Input(key='-OUTPUT-', visible=False)],
            [sg.Text(' ')],
            [sg.Button("Run Model"), sg.Button('Exit'), sg.T('', text_color='#de335e', visible=False, key='ErrGUI'),
             sg.T('', text_color='#caf17c', visible=False, key='SuccGUI')],
            [sg.T('Progress...   ', visible=False, key='progresstext'),
             sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar', visible=False)]
        ]
    ]

    window = sg.Window('Main', layout)
    progress_bar = window['progressbar']
    progress_text = window['progresstext']
    error_message_gui = window['ErrGUI']
    succ_message_gui = window['SuccGUI']
    time_limit_text = window['time_limit_text']
    time_limit_input = window['time_limit_input']
    gap_tollerance_text = window['gap_tollerance_text']
    gap_tollerance_input = window['gap_tollerance']
    advanced_settings_btn = window['advanced_settings']
    close_advanced_settings = window['close_advanced_settings']
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Run Model':
            filenameInput = values['-INPUT-']
            filenameOutput = values['-OUTPUT-']

            model = MODEL_MAPPING[values['_MODEL_']]

            advanced_settings['time_limit'] = values['time_limit_input']
            advanced_settings['gap_tollerance'] = values['gap_tollerance']

            print(values['time_limit_input'])

            if os.path.isfile(filenameInput) and os.path.isdir(filenameOutput):
                error_message_gui.update(visible=False)
                try:
                    progress_text.update(visible=True)
                    progress_bar.update(visible=True)
                    if runModel(Path(filenameInput), filenameOutput, progress_bar,error_message_gui, model,advanced_settings) :
                        progress_bar.UpdateBar(1000)
                        succ_message_gui.update(visible=True)
                        succ_message_gui.update(value='Esecuzione Completata')
                    else:
                        progress_text.update(visible=False)
                        progress_bar.update(visible=False)
                except Exception as e:
                    sg.Print("Error: ", e)
            else:
                error_message_gui.update(visible=True)
                error_message_gui.update(value='Input non valido')
        elif event == 'advanced_settings':
            time_limit_text.update(visible=True)
            time_limit_input.update(visible=True)
            gap_tollerance_text.update(visible=True)
            gap_tollerance_input.update(visible=True)
            advanced_settings_btn.update(visible=False)
            close_advanced_settings.update(visible=True)

        elif event == 'close_advanced_settings':

            gap_tollerance_text.update(visible=False)
            gap_tollerance_input.update(visible=False)
            time_limit_text.update(visible=False)
            time_limit_input.update(visible=False)
            advanced_settings_btn.update(visible=True)
            close_advanced_settings.update(visible=False)

    window.close()


if __name__ == '__main__':
    main()
