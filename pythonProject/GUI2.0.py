import PySimpleGUI as sg
from pathlib import Path
from parse_input import runModel
import datetime
import costants
import os
import calendar
import create_output
import create_calendar
import statistics_model
import output
import random

from pythonProject.costants import MODEL, MODEL_MAPPING, ADVANCED_SETTINGS

def pick_color_for_exam(exam):
    if exam.anno == 1 and exam.lista_semestri[0] == '1':
        return costants.ANNI_SEMESTRI_COLORI[0]
    if exam.anno == 1 and exam.lista_semestri[0] == '2':
        return costants.ANNI_SEMESTRI_COLORI[1]
    if exam.anno == 2 and exam.lista_semestri[0] == '1':
        return costants.ANNI_SEMESTRI_COLORI[2]
    if exam.anno == 2 and exam.lista_semestri[0] == '2':
        return costants.ANNI_SEMESTRI_COLORI[3]
    if exam.anno == 3 and exam.lista_semestri[0] == '1':
        return costants.ANNI_SEMESTRI_COLORI[4]
    if exam.anno == 3 and exam.lista_semestri[0] == '2':
        return costants.ANNI_SEMESTRI_COLORI[5]

def make_window(theme):
    sg.theme("DarkBlue3")
    sg.set_options(font=("Microsoft JhengHei", 13))
    font_title = ("Microsoft JhengHei", 15, 'bold')
    right_click_menu_def = [[], ['Edit Me', 'Versions', 'Nothing', 'More Nothing', 'Exit']]

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

    layout = [[sg.TabGroup([[]], key='experiments'),

               ]]

    col2 = sg.Column(layout)

    col1 = sg.Column([
        # Categories sg.Frame
        [sg.Frame('Input:', [[sg.Text(), sg.Column([[sg.Text('Model Input:')],
                                                    [sg.Input(key='-INPUT-', size=(19, 1)), sg.FileBrowse(
                                                        file_types=(("Excel", "*.xlsx"), ("ALL Files", "*.*")))],
                                                    [sg.Text('Output folder:')],
                                                    [sg.Text('Choose Model:')],
                                                    [sg.Combo(MODEL, size=(19, 1), default_value='Default Model',
                                                              readonly=True, key='_MODEL_')],
                                                    ], pad=(0, 10))], ], pad=(10, 5))],
        [sg.Frame('Output:', [[sg.Text(), sg.Column([
                                                    [sg.Text('Output folder:')],
                                                    [sg.Input(key='-OUTPUT-', size=(19, 1)), sg.FolderBrowse()]], pad=(0, 10))]])],
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

    '''col3 = sg.Column([
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
                                                       ], size=(300, 350), pad=(0, 0))]])], ], pad=(0, 0))'''

    # The final layout is a simple one
    layout = [[col1, col2]]
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
    tab_layout = window['experiments']
    experiments=[]

    # Inforamtion Exam
    #data_start_sessione = window['data_start_sessione']
    #data_end_sessione = window['data_end_sessione']
    experiment_count = 1
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

            #and os.path.isdir(filenameOutput)

            if os.path.isfile(filenameInput):
                error_message_gui.update(visible=False)
                try:
                    progress_bar.update(visible=True)
                    model_output = runModel(Path(filenameInput), filenameOutput, progress_bar, error_message_gui, model,
                                            advanced_settings)
                    if model_output:
                        model_output.selected_model=model
                        experiments.append(model_output)
                        progress_bar.UpdateBar(1000)
                        succ_message_gui.update(visible=True)
                        succ_message_gui.update(value='Esecuzione Completata')

                        # Update information output
                        '''data_start_sessione.update(
                            value='Inizio: ' + datetime.date.strftime(model_output.sessione[0][0],
                                                                      '%d/%m/%Y'))  # TODO: sarebbe bello accedere a questa info con sessione.dataInizio
                        data_end_sessione.update(
                            value='Fine: ' + datetime.date.strftime(model_output.sessione[0][1], '%d/%m/%Y'))'''
                        tab_layout.add_tab(sg.Tab('Esperimento: ' + str(experiment_count), buildTwoMonthTab(model_output,experiment_count)))
                        experiment_count += 1
                    else:
                        progress_bar.update(visible=False)
                except Exception as e:
                    sg.Print("Error: ", e)
            else:
                error_message_gui.update(visible=True)
                error_message_gui.update(value='File di Input non valido')
        elif event[0:17]== 'Esporta risultato':
            filenameOutput = values['-OUTPUT-']
            if(os.path.isdir(filenameOutput)):
                error_message_gui.update(visible=False)
                succ_message_gui.update(visible=False)
                export_id=int(event.split('#')[1])-1
                progress_bar.UpdateBar(0)
                create_output.build_output(experiments[export_id].input, experiments[export_id].output, experiments[export_id].esami, experiments[export_id].laboratori, experiments[export_id].aule, experiments[export_id].model, experiments[export_id].sessione)
                progress_bar.UpdateBar(500)
                create_calendar.build_calendar(experiments[export_id].esami,experiments[export_id].model,experiments[export_id].sessione, experiments[export_id].output)
                progress_bar.UpdateBar(1000)
                succ_message_gui.update(value='Esperimento #'+str(export_id+1)+" esportato")
                succ_message_gui.update(visible=True)
            else:
                error_message_gui.update(visible=True)
                succ_message_gui.update(visible=False)
                error_message_gui.update(value='Cartella di output non valida')
        elif event[0:11] == "ExamButton_":
            experiment_id=int(event.split("_")[2])-1
            exam_id=int(event.split("_")[1])
            text=window['details_'+str(experiment_id)]
            text.update(value=buildDetailsText(experiments[experiment_id],exam_id))

    window.close()

def buildStatistics(model_output,experiment_count,session):
    return [[sg.Column([[sg.Text("Statistiche:")],
                        [sg.Text(statistics_model.generate_statistics_for_graphic(model_output.model,model_output.esami,model_output.sessione[0][0],model_output.sessione[0][1]),font=("Arial",9))]
                        ])]]

def buildDetailsText(model_output,exam_id):
    result="\n\n"
    result+="📕 Esame: "+model_output.esami[exam_id].short_name+"\n"
    result+="🔢 Giorni durata: "+str(model_output.esami[exam_id].numero_giorni_durata)+"\n"
    result+="\n🏠 Aule richieste: \n"
    if(len(model_output.esami[exam_id].aule_richieste)==0):
        result += "Nessuna aula richiesta\n"
    for index,aula in enumerate(model_output.esami[exam_id].aule_richieste):
        result+=model_output.aule[aula].nome+" | "+str(model_output.esami[exam_id].slot_aule_richieste[index])+" slot\n"
    result += "\n💻 Laboratori richiesti: \n"
    if (len(model_output.esami[exam_id].laboratori_richiesti) == 0):
        result += "Nessun laboratorio richiesto\n"
    for index, lab in enumerate(model_output.esami[exam_id].laboratori_richiesti):
        result += model_output.laboratori[lab].nome + " | " + str(
            model_output.esami[exam_id].laboratori_richiesti_slot[index]) + " slot\n"
    result +="\n⭕ Appelli: \n"

    assegnamenti=model_output.assegnamenti[exam_id]
    for index,assegnamento in enumerate(assegnamenti):
        idAssegnamento=index+1
        if(idAssegnamento<=model_output.esami[exam_id].numero_giorni_durata):
            idAssegnamento=1
        else:
            idAssegnamento=2
        result+="📅 Appello "+str(idAssegnamento)+" | "
        result+=datetime.date.strftime(assegnamento,'%d/%m/%Y')+"\n"

    return result

def buildMonthTab(model_output,experiment_count,year,month):
    # Table Data
    headings = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    cal = calendar.monthcalendar(year, month)
    MAX_ROWS = len(cal)
    MAX_COL = len(cal[0])
    cal_exams = []
    for i in range(MAX_ROWS):
        cal_exams.append([])
        for j in range(MAX_COL):
            cal_exams[i].append([])

    for index, assegnamenti_esame in enumerate(model_output.assegnamenti):
        for assegnamento in assegnamenti_esame:
            if (assegnamento.month == month):
                day = assegnamento.day
                for i in range(MAX_ROWS):
                    for j in range(MAX_COL):
                        if (str(cal[i][j]) == str(day)):
                            cal_exams[i][j].append([model_output.esami[index].short_name, index,
                                                    "black on " + pick_color_for_exam(model_output.esami[index]),str(index)])

    MAX_ROWS_NUM = list()
    for i in range(MAX_ROWS):
        maximus = 1
        for j in range(MAX_COL):
            if len(cal_exams[i][j]) > maximus:
                maximus = len(cal_exams[i][j])
        for j in range(MAX_COL):
            while len(cal_exams[i][j]) < maximus:
                cal_exams[i][j].append([" ", -1, 'black on #64778d',"-1"])
        MAX_ROWS_NUM.append(maximus)

    columm_layout = [[sg.Column([[
        sg.Frame((str(cal[i][k]) if str(cal[i][k]) != '0' else ' '), [[sg.Button(cal_exams[i][k][j][0], pad=(
            (1, 1) if cal_exams[i][k][j][0] != " " else (2, 2)), button_color=cal_exams[i][k][j][2],
                                                                                 font=("Microsoft JhengHei", 9),
                                                                                 size=(20, 1), disabled=(
                False if cal_exams[i][k][j][0] != " " else True), border_width=(
                1 if cal_exams[i][k][j][0] != " " else 0), key=("ExamButton_" + cal_exams[i][k][j][3] +"_" + experiment_count +"_" + str(
                str(random.randint(0, 10000)))), )] for j in
                                                                      range(MAX_ROWS_NUM[i])], pad=(0, 0),
                 border_width=1, key=(i, k), ) for k in
        range(MAX_COL)] for i in range(MAX_ROWS)])]]

    return columm_layout


def buildTwoMonthTab(model_output,experiment_count):
    m_names = '''
   A Gennaio Febbraio Marzo Aprile Maggio Giugno Luglio Agosto Settembre Ottobre Novembre Dicembre'''.split()
    available_models={"model_building":"Default","model_building1":"Modello1","model_building2":"Modello2","model_building3":"Modello3","model_building4":"Modello4","model_building5":"Modello5"}
    data_inizio_sessione = datetime.date.strftime(model_output.sessione[0][0],
                                                  '%d/%m/%Y')
    data_fine_sessione = datetime.date.strftime(model_output.sessione[0][1], '%d/%m/%Y')



    month_1_tab=buildMonthTab(model_output,str(experiment_count),model_output.sessione[0][0].year,model_output.sessione[0][0].month)
    month_2_tab=None
    statistics=buildStatistics(model_output,experiment_count,model_output.sessione)
    if(model_output.sessione[0][0].month!=model_output.sessione[0][1].month):
        month_2_tab=buildMonthTab(model_output,str(experiment_count),model_output.sessione[0][1].year,model_output.sessione[0][1].month)


    columm_layout = [[sg.Column([[sg.TabGroup([[sg.Tab(m_names[model_output.sessione[0][0].month],layout=month_1_tab),
                                    sg.Tab(m_names[model_output.sessione[0][1].month] ,layout=month_2_tab),sg.Tab("Statistiche" ,layout=statistics)]] if month_2_tab!=None
                                              else [[sg.Tab(m_names[model_output.sessione[0][0].month],layout=month_1_tab)]], key='experiment' + str(experiment_count), pad=(0,(10,0)))]]),
                      sg.Column([
                          # Categories sg.Frame
                          [sg.Frame('Input:',
                                    [
                                        [sg.Text(
                                            'Modello utilizzato: ' + str(available_models[model_output.selected_model])
                                            )],
                                        [sg.Text(
                                            'File input: ' + str(os.path.basename(str(model_output.input)))
                                        )],
                                        [sg.Text('Data inizio sessione: ' + str(data_inizio_sessione)
                                              )],
                                        [sg.Text('Data fine sessione:' + str(data_fine_sessione)
                                              )],
                                     ],

                                     pad=(0,(30,0)))],
                          # Information sg.Frame
                          [sg.Frame('Dettagli:',
                                    [[sg.Column([[sg.Button('Esporta risultato esperimento #' + str(experiment_count))],
                                                 [sg.Text('', key="details_" + str(experiment_count-1)
                                                          )]
                                                            ], pad=(0, 0))]])], ], pad=(0, 0), vertical_alignment='t')]]

    return columm_layout





if __name__ == '__main__':
    sg.theme('black')
    # sg.theme('DefaultNoMoreNagging')
    main()

