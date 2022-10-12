import PySimpleGUI as sg
from pathlib import Path
from parse_input import runModel
import datetime
import costants
import os
import calendar

import output

from pythonProject.costants import MODEL, MODEL_MAPPING, ADVANCED_SETTINGS


def make_window(theme):
    sg.theme("DarkBlue3")
    sg.set_options(font=("Microsoft JhengHei", 13))
    font_title = ("Microsoft JhengHei", 15, 'bold')
    right_click_menu_def = [[], ['Edit Me', 'Versions', 'Nothing', 'More Nothing', 'Exit']]

    # Table Data
    data = [["John", 10], ["Jen", 5]]
    headings = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    cal = calendar.monthcalendar(2022, 10)

    MAX_ROWS = len(cal)
    MAX_COL = len(cal[0])

    MAX_ROWS_NUM = [3, 2, 5, 1, 1, 1, 1, 1]

    columm_layout = [[
        sg.Frame((str(cal[i][k]) if str(cal[i][k]) != '0' else ' '), [[sg.Button('', pad=((1,1) if str(cal[i][k]) != '0' else (2,2)), button_color= (costants.ANNI_SEMESTRI_COLORI[i] if str(cal[i][k]) != '0' else '#64778d'),
                                                                                  font=("Microsoft JhengHei", 9),size=(20, 1), disabled=(True if str(cal[i][k]) == '0' else False), border_width=(1 if str(cal[i][k]) != '0' else 0), key=(i, j), )] for j in
                                  range(MAX_ROWS_NUM[i])], pad=(0, 0), border_width=1, key=(i, k), ) for k in
        range(MAX_COL)] for i in range(MAX_ROWS)]

    input_layout = [

        # [sg.Menu(menu_def, key='-MENU-')],
        [sg.Text('Anything that requires user-input is in this tab!')],
        [sg.Input(key='-INPUT-')],
        [sg.Slider(orientation='h', key='-SKIDER-'),
         sg.Image(data=sg.DEFAULT_BASE64_LOADING_GIF, enable_events=True, key='-GIF-IMAGE-'), ],
        [sg.Checkbox('Checkbox', default=True, k='-CB-')],
        [sg.Radio('Radio1', "RadioDemo", default=True, size=(10, 1), k='-R1-'),
         sg.Radio('Radio2', "RadioDemo", default=True, size=(10, 1), k='-R2-')],
        [sg.Combo(values=('Combo 1', 'Combo 2', 'Combo 3'), default_value='Combo 1', readonly=False, k='-COMBO-'),
         sg.OptionMenu(values=('Option 1', 'Option 2', 'Option 3'), k='-OPTION MENU-'), ],
        [sg.Spin([i for i in range(1, 11)], initial_value=10, k='-SPIN-'), sg.Text('Spin')],
        [sg.Multiline(
            'Demo of a Multi-Line Text Element!\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nYou get the point.',
            size=(45, 5), expand_x=True, expand_y=True, k='-MLINE-')],
        [sg.Button('Button'), sg.Button('Popup'), sg.Button(image_data=sg.DEFAULT_BASE64_ICON, key='-LOGO-')]]

    asthetic_layout = [[sg.T('Anything that you would use for asthetics is in this tab!')],
                       [sg.Image(data=sg.DEFAULT_BASE64_ICON, k='-IMAGE-')],
                       [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS BAR-'),
                        sg.Button('Test Progress bar')]]

    logging_layout = [[sg.Text("Anything printed will display here!")],
                      [sg.Multiline(size=(60, 15), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True,
                                    auto_refresh=True)]
                      # [sg.Output(size=(60,15), font='Courier 8', expand_x=True, expand_y=True)]
                      ]

    graphing_layout = columm_layout

    popup_layout = [[sg.Text("Popup Testing")],
                    [sg.Button("Open Folder")],
                    [sg.Button("Open File")]]

    theme_layout = [[sg.Text("See how elements look under different themes by choosing a different theme here!")],
                    [sg.Listbox(values=sg.theme_list(),
                                size=(20, 12),
                                key='-THEME LISTBOX-',
                                enable_events=True)],
                    [sg.Button("Set Theme")]]

    layout = [[sg.TabGroup([[sg.Tab('Input Elements', input_layout),
                             sg.Tab('Asthetic Elements', asthetic_layout),
                             sg.Tab('Graphing', graphing_layout),
                             sg.Tab('Popups', popup_layout),
                             sg.Tab('Theming', theme_layout),
                             sg.Tab('Output', logging_layout)]], key='-TAB GROUP-'),

               ]]

    col2 = sg.Column(layout)

    col1 = sg.Column([
        # Categories sg.Frame
        [sg.Frame('Input:', [[sg.Text(), sg.Column([[sg.Text('Model Input:')],
                                                    [sg.Input(key='-INPUT-', size=(19, 1)), sg.FileBrowse(
                                                        file_types=(("Excel", "*.xlsx"), ("ALL Files", "*.*")))],
                                                    [sg.Text('Output folder:')],
                                                    [sg.Input(key='-OUTPUT-', size=(19, 1)), sg.FolderBrowse()],
                                                    [sg.Text('Choose Model:')],
                                                    [sg.Combo(MODEL, size=(19, 1), default_value='Default Model',
                                                              readonly=True, key='_MODEL_')],
                                                    ], size=(300, 250), pad=(0, 0))], ], pad=(5, 0))],
        # Information sg.Frame
        [sg.Frame('Advanced Settings:', [[sg.Text(), sg.Column([[sg.Text('Time limit (M):')],
                                                                [sg.Input(key='time_limit_input',
                                                                          default_text=ADVANCED_SETTINGS['time_limit'],
                                                                          size=(19, 1))]
                                                                ], size=(300, 100), pad=(0, 0))]])],
        [sg.Frame('Actions:',
                  [[sg.Column([[sg.Button("Run Model"),
                                sg.ProgressBar(1000, orientation='h', size=(17, 35), key='progressbar', visible=True)]],
                              size=(312, 60), pad=(0, 0))]])],
        [sg.T('', text_color='#aa080b', visible=False, key='ErrGUI'),
         sg.T('', text_color='#caf17c', visible=False, key='SuccGUI')]], pad=(5, 0))

    col3 = sg.Column([
        # Categories sg.Frame
        [sg.Frame('Sessione:', [[sg.Text('Inizio:', key='data_start_sessione', size=(20, 1))],
                                 [sg.Text('Fine:', key='data_end_sessione', size=(20, 1))]], size=(317, 100))],
        # Information sg.Frame
        [sg.Frame('Dettagli:', [[sg.Text(), sg.Column([[sg.Text('Account:')],
                                                          [sg.Input(key='-ACCOUNT-IN-', size=(19, 1))],
                                                          [sg.Text('User Id:')],
                                                          [sg.Input(key='-USERID-IN-', size=(19, 1)),
                                                           sg.Button('Copy', key='-USERID-')],
                                                          [sg.Text('Password:')],
                                                          [sg.Input(key='-PW-IN-', size=(19, 1)),
                                                           sg.Button('Copy', key='-PASS-')],
                                                          [sg.Text('Location:')],
                                                          [sg.Input(key='-LOC-IN-', size=(19, 1)),
                                                           sg.Button('Copy', key='-LOC-')],
                                                          [sg.Text('Notes:')],
                                                          [sg.Multiline(key='-NOTES-', size=(25, 5))],
                                                          ], size=(300, 350), pad=(0, 0))]])], ], pad=(0, 0))

    # The final layout is a simple one
    layout = [[col1, col2, col3]]
    window = sg.Window('Ottimizzazione Calendario Esami', layout, right_click_menu=right_click_menu_def,
                       right_click_menu_tearoff=True, grab_anywhere=True, resizable=True, margins=(0, 0),
                       use_custom_titlebar=True, finalize=True, keep_on_top=True)
    window.set_min_size(window.size)
    return window


def main():
    advanced_settings = ADVANCED_SETTINGS
    window = make_window(sg.theme())
    progress_bar = window['progressbar']
    error_message_gui = window['ErrGUI']
    succ_message_gui = window['SuccGUI']

    #Inforamtion Exam
    data_start_sessione = window['data_start_sessione']
    data_end_sessione = window['data_end_sessione']

    # This is an Event Loop
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Run Model':
            succ_message_gui.update(visible=False)
            filenameInput = values['-INPUT-']
            filenameOutput = values['-OUTPUT-']

            model = MODEL_MAPPING[values['_MODEL_']]

            advanced_settings['time_limit'] = values['time_limit_input']

            print(values['time_limit_input'])

            if os.path.isfile(filenameInput) and os.path.isdir(filenameOutput):
                error_message_gui.update(visible=False)
                try:
                    progress_bar.update(visible=True)
                    model_output = runModel(Path(filenameInput), filenameOutput, progress_bar, error_message_gui, model,
                                advanced_settings)
                    if model_output:
                        progress_bar.UpdateBar(1000)
                        succ_message_gui.update(visible=True)
                        succ_message_gui.update(value='Esecuzione Completata')

                        #Update information output
                        data_start_sessione.update(value= 'Inizio: ' + datetime.date.strftime(model_output.sessione[0][0],'%d/%m/%Y')) #TODO: sarebbe bello accedere a questa info con sessione.dataInizio
                        data_end_sessione.update(value= 'Fine: ' + datetime.date.strftime(model_output.sessione[0][1],'%d/%m/%Y'))
                    else:
                        progress_bar.update(visible=False)
                except Exception as e:
                    sg.Print("Error: ", e)
            else:
                error_message_gui.update(visible=True)
                error_message_gui.update(value='Input non valido')

    window.close()


if __name__ == '__main__':
    sg.theme('black')
    # sg.theme('DefaultNoMoreNagging')
    main()
