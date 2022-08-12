import PySimpleGUI as sg
from pathlib import Path
from parse_input import runModel
import os
print = sg.Print

def main():


    sg.theme("DarkBlue3")
    sg.set_options(font=("Microsoft JhengHei", 16))
    font_title = ("Microsoft JhengHei", 25, 'bold')
    layout = [
        [
            [sg.Text('Modello di ottimizzazione calendario Esami',font=font_title)],
            [sg.T('Model Input     '),sg.Input(key='-INPUT-'),
            sg.FileBrowse(file_types=(("Excel", "*.xlsx"), ("ALL Files", "*.*")))],
            [sg.T('Output folder  '),sg.Input(key='-OUTPUT-'),
            sg.FolderBrowse()],
            [sg.T('Choose Model'),sg.Combo(['Default Model', 'Variation Model 1', 'Variation Model 2', 'Variation Model 3'],default_value='Default Model', readonly=True,key='_MODEL_')],
            [sg.Button("Run Model"), sg.Button('Exit'),sg.T('', text_color='#de335e' , visible=False, key='ErrGUI')],
            [sg.T('Progress...   ', visible=False, key='progresstext'),sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar', visible=False)]
        ]
    ]

    window = sg.Window('Main', layout)
    progress_bar = window['progressbar']
    progress_text = window['progresstext']
    error_message_gui = window['ErrGUI']
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Run Model':
            filenameInput = values['-INPUT-']
            filenameOutput = values['-OUTPUT-']

            model = values['_MODEL_']

            if os.path.isfile(filenameInput) and os.path.isdir(filenameOutput):
                error_message_gui.update(visible=False)
                try:
                    sg.Print('This is a normal print that has been re-routed.')
                    progress_text.update(visible=True)
                    progress_bar.update(visible=True)
                    runModel(Path(filenameInput),filenameOutput,progress_bar)
                    progress_bar.UpdateBar(1000)
                except Exception as e:
                    print("Error: ", e)
            else:
                error_message_gui.update(visible=True)
                error_message_gui.update(value='Input non valido')


    window.close()

if __name__ == '__main__':
    main()