# This file parsing the xlsx input
# AULE (Nome,Indisponibilità)
# LABORATORI (Nome,Indisponibilità)
# SESSIONE (Nome, DataInizio, DataFine)
# ESAME(
import os.path

import PySimpleGUI as sg

print = sg.Print  # TODO modificare in base a che output vogliamo

import pandas as pd
from datetime import datetime, timedelta
import classes
import costants
import create_output
import create_calendar
import holidays

#import model_building3 as building
import pyomo.environ as pyo

sessioni = []  # Managed as an array but in reality it contains only one session, so we use the positions sessioni[0][0] e sessioni[0][1]
laboratori = []
aule = []
exams = []
ERRORE = ""


def print_GUI_error(GUI_obj, message):
    if '' != GUI_obj:
        GUI_obj.update(visible=True, value=message)


def printParametri(building):
    print("Distanza minima appelli: " + str(building.MIN_DISTANCE_APPELLI))
    print("Slot giornalieri aule: " + str(building.SLOT_AULE))
    print("Slot giornalieri laboratorio: " + str(building.SLOT_LABORATORI))
    print("Guadagno giorni preferiti: " + str(building.GUADAGNO_GIORNI_PREFERITI))
    print("Importanza primo anno: " + str(building.COSTANTE_IMPORTANZA_PRIMO_ANNO))
    print("Importanza secondo anno: " + str(building.COSTANTE_IMPORTANZA_SECONDO_ANNO))
    print("Importanza terzo anno: " + str(building.COSTANTE_IMPORTANZA_TERZO_ANNO))


def printLaboratori():
    print("LABORATORI:")
    for lab in laboratori:
        print(lab.nome)
        print(lab.indisponibilita)


def printAule():
    print("Aule:")
    for aula in aule:
        print(aula.nome)
        print(aula.indisponibilita)


def printSessioni():
    print("Sessioni:")
    for index, sessione in enumerate(sessioni):
        print("Sessione " + str(index + 1) + " Data inizio: " + str(sessione[0]) + " Data fine: " + str(sessione[1]))


def printCorsi():
    print("Esami:")
    for corso in exams:
        print("Nome: " + str(corso.nome))
        print("Tipo: "+str(corso.tipo))
        print("Insegnanti: "+str(corso.insegnanti))
        print("Lista semestri: "+str(corso.lista_semestri))
        print("Anno: "+str(corso.anno))
        print("Numero appelli sessione: "+str(corso.numero_appelli))
        print("Aule richieste: "+str(corso.aule_richieste))
        print("Slot aule: "+str(corso.numero_aule_slot))
        print("Laboratori richiesti: "+str(corso.laboratori_richiesti))
        print("Slot laboratori: "+str(corso.numero_lab_slot))
        print("Durata giorni: "+str(corso.numero_giorni_durata))
        print("Date di preferenza: "+str(corso.date_preferenza))
        print("Date di indisponibilità: "+str(corso.date_indisponibilita))
        print("Note: "+str(corso.note))


def get_non_working_days(data_inizio, data_fine):
    delta = data_fine - data_inizio  # as timedelta
    weekend = []
    for i in range(delta.days + 1):
        day = data_inizio + timedelta(days=i)
        if day.weekday() > 4:
            weekend.append(day)
        # Aggiungo i giorni festivi
        if day in holidays.Italy(years=data_inizio.year) and day not in weekend:
            weekend.append(day)
    return weekend


def load_date(input, error_message_gui):  # Errori gestiti da testare a fondo
    if input != '':
        sessioni_df = pd.read_excel(input, sheet_name='Input generali', skiprows=1,
                                    usecols=costants.COLONNE_SESSIONI)
    else:
        sessioni_df = pd.read_excel('input/' + costants.INPUT_FILE_NAME, sheet_name='Input generali', skiprows=1,
                                    usecols=costants.COLONNE_SESSIONI)
    for index, row in sessioni_df.iterrows():
        # row[0] -> Data  Inizio -> Date
        # row[1] -> Data fine -> Dateù
        if not pd.isnull(row[0]) and not pd.isnull(row[1]):
            sessioni.append([])
            try:
                if datetime.strptime(str(row[1]).strip(), '%Y-%m-%d %H:%M:%S') > datetime.strptime(str(row[0]).strip(),
                                                                                                   '%Y-%m-%d %H:%M:%S'):
                    sessioni[index].append(datetime.strptime(str(row[0]).strip(), '%Y-%m-%d %H:%M:%S'))
                    sessioni[index].append(datetime.strptime(str(row[1]).strip(), '%Y-%m-%d %H:%M:%S'))
                else:
                    print("Data finale successiva alla data iniziale")
                    print_GUI_error(error_message_gui, "Data finale successiva alla data iniziale")
                    return False
            except:
                print("Date in formato errato tra le seguenti: ", row[0], " e ", row[1])
                print_GUI_error(error_message_gui, "Date in formato errato tra le seguenti: " + row[0] + " e " + row[1])
                return False
    return True


def load_laboratori(input, error_message_gui):  # Errori gestiti da testare a fondo
    if input != '':
        laboratorii_df = pd.read_excel(input, sheet_name='Input generali', skiprows=1,
                                       usecols=costants.COLONNE_LABORATORI)
    else:
        laboratorii_df = pd.read_excel('input/' + costants.INPUT_FILE_NAME, sheet_name='Input generali', skiprows=1,
                                       usecols=costants.COLONNE_LABORATORI)
    for index, row in laboratorii_df.iterrows():
        # row[0] -> Nome Laboratorio -> String
        # row[1] -> Indisponibilità -> String {Data1,...,DataN}
        if not pd.isnull(row[0]):
            dateindisp = []
            if not pd.isnull(row[1]):
                dateindisp = parse_list(row[1])
                for index in range(len(dateindisp)):
                    if '00:00:00' in dateindisp[index]:
                        try:
                            dateindisp[index] = datetime.strptime(dateindisp[index], '%Y-%m-%d %H:%M:%S')
                        except:
                            print("Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido")
                            print_GUI_error(error_message_gui,
                                            "Data di indisponibilità del laboratorio " + row[
                                                0] + " in un formato non valido")
                            return False
                    else:
                        try:
                            dateindisp[index] = datetime.strptime(dateindisp[index].strip(), '%d/%m/%Y')
                        except:
                            print("Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido")
                            print_GUI_error(error_message_gui,
                                            "Data di indisponibilità del laboratorio " + row[
                                                0] + " in un formato non valido")
                            return False
                    found = False  # Per ogni data di indisponibilità verifico che sia in qualche sessione
                    for sessione in sessioni:
                        if dateindisp[index] >= sessione[0] and dateindisp[index] <= sessione[1]:
                            found = True
                    if not found:
                        print("Data di indisponibilità del laboratorio " + row[
                            0] + " non è in nessuna sessione di quelle impostate")
                        print_GUI_error(error_message_gui,
                                        "Data di indisponibilità del laboratorio " + row[
                                            0] + " non è in nessuna sessione di quelle impostate")
                        return False
            laboratori.append(classes.ExamRoom(row[0], dateindisp))
    return True


def load_aule(input, error_message_gui):  # Errori gestiti da testare a fondo
    if input != '':
        aule_df = pd.read_excel(input, sheet_name='Input generali', skiprows=1,
                                usecols=costants.COLONNE_AULE)
    else:
        aule_df = pd.read_excel('input/' + costants.INPUT_FILE_NAME, sheet_name='Input generali', skiprows=1,
                                usecols=costants.COLONNE_AULE)
    for index, row in aule_df.iterrows():
        # row[0] -> Nome Aula -> String
        # row[1] -> Indisponibilità -> String {Data1,...,DataN}
        if not pd.isnull(row[0]):
            dateindisp = []
            if not pd.isnull(row[1]):
                dateindisp = parse_list(row[1])
                for index in range(len(dateindisp)):
                    if '00:00:00' in dateindisp[index]:
                        try:
                            dateindisp[index] = datetime.strptime(dateindisp[index], '%Y-%m-%d %H:%M:%S')
                        except:
                            print("Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido")
                            print_GUI_error(error_message_gui,
                                            "Data di indisponibilità del laboratorio " + row[
                                                0] + " in un formato non valido")
                            return False
                    else:
                        try:
                            dateindisp[index] = datetime.strptime(dateindisp[index].strip(), '%d/%m/%Y')
                        except:
                            print("Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido")
                            print_GUI_error(error_message_gui,
                                            "Data di indisponibilità del laboratorio " + row[
                                                0] + " in un formato non valido")
                            return False
                found = False  # Per ogni data di indisponibilità verifico che sia in qualche sessione
                for sessione in sessioni:
                    if dateindisp[index] >= sessione[0] and dateindisp[index] <= sessione[1]:
                        found = True
                if not found:
                    print("Data di indisponibilità del laboratorio " + row[
                        0] + " non è in nessuna sessione di quelle impostate")
                    print_GUI_error(error_message_gui,
                                    "Data di indisponibilità del laboratorio " + row[
                                        0] + " non è in nessuna sessione di quelle impostate")
                    return False
            aule.append(classes.ExamRoom(row[0], dateindisp))
    return True


def load_parametri(input, building, error_message_gui):  # Errori gestiti da testare a fondo
    if input != '':
        parametri_df = pd.read_excel(input, sheet_name='Input generali', skiprows=1,
                                usecols=costants.COLONNE_PARAMETRI)
    else:
        parametri_df = pd.read_excel('input/' + costants.INPUT_FILE_NAME, sheet_name='Input generali', skiprows=1,
                                usecols=costants.COLONNE_PARAMETRI)
    for index, row in parametri_df.iterrows():
        # row[0] -> Nome parametro -> String
        # row[1] -> Value -> int
        if not pd.isnull(row[0]):
            if (row[0] == "Distanza appelli"):
                val = row[1]
                try:
                    int_val = int(val)
                    building.MIN_DISTANCE_APPELLI = int_val
                except:
                    print("Dato non valido per Distanza appelli: " + str(row[1]))
                    print_GUI_error(error_message_gui,
                                    "Dato non valido per Distanza appelli: " + str(row[1]))
                    return False
            else:
                if (row[0] == "Slot giornalieri aule"):
                    val = row[1]
                    try:
                        int_val = int(val)
                        building.SLOT_AULE = int_val
                    except:
                        print("Dato non valido per Slot giornalieri aule: " + str(row[1]))
                        print_GUI_error(error_message_gui,
                                        "Dato non valido per Slot giornalieri aule: " + str(row[1]))
                        return False
                else:
                    if (row[0] == "Slot giornalieri laboratori"):
                        val = row[1]
                        try:
                            int_val = int(val)
                            building.SLOT_LABORATORI = int_val
                        except:
                            print("Dato non valido per Slot giornalieri laboratori: " + str(row[1]))
                            print_GUI_error(error_message_gui,
                                            "Dato non valido per Slot giornalieri laboratori: " + str(row[1]))
                            return False
                    else:
                        if (row[0] == "Guadagno giorni preferiti"):
                            val = row[1]
                            try:
                                int_val = int(val)
                                building.GUADAGNO_GIORNI_PREFERITI = int_val
                            except:
                                print("Dato non valido per Guadagno giorni preferiti: " + str(row[1]))
                                print_GUI_error(error_message_gui,
                                                "Dato non valido per Guadagno giorni preferiti: " + str(row[1]))
                                return False
                        else:
                            if (row[0] == "Importanza primo anno"):
                                val = row[1]
                                try:
                                    int_val = int(val)
                                    building.COSTANTE_IMPORTANZA_PRIMO_ANNO = int_val
                                except:
                                    print("Dato non valido per Importanza primo anno: " + str(row[1]))
                                    print_GUI_error(error_message_gui,
                                                    "Dato non valido per Importanza primo anno: " + str(row[1]))
                                    return False
                            else:
                                if (row[0] == "Importanza secondo anno"):
                                    val = row[1]
                                    try:
                                        int_val = int(val)
                                        building.COSTANTE_IMPORTANZA_SECONDO_ANNO = int_val
                                    except:
                                        print("Dato non valido per Importanza secondo anno: " + str(row[1]))
                                        print_GUI_error(error_message_gui,
                                                        "Dato non valido per Importanza secondo anno: " + str(row[1]))
                                        return False
                                else:
                                    if (row[0] == "Importanza terzo anno"):
                                        val = row[1]
                                        try:
                                            int_val = int(val)
                                            building.COSTANTE_IMPORTANZA_TERZO_ANNO = int_val
                                        except:
                                            print("Dato non valido per Importanza terzo anno: " + str(row[1]))
                                            print_GUI_error(error_message_gui,
                                                            "Dato non valido per Importanza terzo anno: " + str(row[1]))
                                            return False
                                    else:
                                        print("Tipologia del parametro non comprensibile")
                                        print_GUI_error(error_message_gui,
                                                        "Tipologia del parametro non comprensibile")
                                        return False
    return True


def load_exams(input, nome_foglio, anno, error_message_gui):
    aule_richieste = []
    laboratori_richiesti = []
    date_indisponibilita = []
    date_preferenza = []
    note = ""
    print(input)
    if input != '':
        exams_df = pd.read_excel(input, sheet_name=nome_foglio)
    else:
        exams_df = pd.read_excel('input/' + costants.INPUT_FILE_NAME, sheet_name=nome_foglio)
    for index, row in exams_df.iterrows():
        # row[0] -> Nome Corso -> String
        # row[1] -> Tipologia -> String
        # row[2] -> Docenti -> String
        # row[3] -> Semestri Corso -> String {1,2}
        # row[4] -> Numero appelli sessioni  -> int
        # row[5] -> Aule Richieste -> String {Aula1,...,AulaN}
        # row[6] -> Slot orari richiesti per le aule -> int >= 1 && <= 2
        # row[7] -> Laboratori richiesti -> String {Laboratorio1,...,LaboratorioN}
        # row[8] -> Slot orari richiesti per i laboratori -> int >= 1 && <= 3
        # row[9] -> Giorni di durata dell'esame -> int
        # row[10] -> Date di preferenza dei professori -> String {Data1,...,DataN}
        # row[11] -> Date di indisponibilità dei professori -> String {Data1,...,DataN}
        # row[12] -> Note -> String
        semestri = str(row[3]).replace('.0', '')
        semestri = parse_list(semestri, '.')
        for semestre in semestri:
            if semestre != "1" and semestre != "2":
                print("Formato dei semestri errato " + str(row[3]))
                print_GUI_error(error_message_gui,
                                "[Errore caricamento esami "+str(anno)+" anno riga "+str(index+2)+"] \nFormato dei semestri errato " + str(row[3]))
                return False
        try:
            if int(row[4])<=0:
                print("Formato del numero appelli errato " + str(row[4]))
                print_GUI_error(error_message_gui,
                                "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                    index + 2) + "] \nFormato del numero appelli errato: " + str(row[4]))
                return False
        except ValueError:
            print("Formato del numero appelli errato " + str(row[4]))
            print_GUI_error(error_message_gui,
                            "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                index + 2) + "] \nFormato del numero appelli errato: " + str(row[4]))
            return False


        if not pd.isnull(row[5]):  # Controllo che gli esami abbiano aule esistenti inseriti in input generali
            aule_richieste = parse_list(row[5])
            for index_aule_richieste in range(len(aule_richieste)):
                for index, aula in enumerate(aule):
                    if not check_exist(aule, str(aule_richieste[index_aule_richieste]).strip()):
                        print("Errore nel caricamento del flusso " + str(
                            aule_richieste[index_aule_richieste]).strip() + " mancante")
                        print_GUI_error(error_message_gui,
                                        "[Errore caricamento esami "+str(anno)+" anno riga "+str(index+2)+"] \n L'aula '" + str(
                                            aule_richieste[index_aule_richieste]).strip() + "' inserita non è valida.")
                        return False

        if not pd.isnull(row[5]):  # Parsifico le aule e inserisco l'indice associato ad esse
            aule_richieste = parse_list(row[5])
            for index_aule_richieste in range(len(aule_richieste)):
                for index, aula in enumerate(aule):
                    if str(aula.nome).strip() == str(aule_richieste[index_aule_richieste]).strip():
                        aule_richieste[index_aule_richieste] = index

        if pd.isnull(row[6]):
            row[6] = 0
        try:
            if int( row[6]) < 0:
                print("Formato degli slot orari richiesti per le aule errato" + str(row[6]))
                print_GUI_error(error_message_gui,
                                "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                    index + 2) + "] \nFormato degli slot orari richiesti per le aule errato" + str(row[6]))
                return False
        except ValueError:
            print("Formato degli slot orari richiesti per le aule errato" + str(row[6]))
            print_GUI_error(error_message_gui,
                            "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                index + 2) + "] \nFormato degli slot orari richiesti per le aule errato" + str(row[6]))
            return False

        if not pd.isnull(row[7]):  # Controllo che gli esami abbiano laboratori esistenti inseriti in input generali
            laboratori_richiesti = parse_list(row[7])
            for index_laboratori_richieste in range(len(laboratori_richiesti)):
                if laboratori_richiesti[index_laboratori_richieste] != '' and laboratori_richiesti[
                    index_laboratori_richieste] != ' ':
                    for index, lab in enumerate(laboratori):
                        if not check_exist(laboratori, str(laboratori_richiesti[index_laboratori_richieste]).strip()):
                            print("Errore nel caricamento del flusso " + str(
                                laboratori_richiesti[index_laboratori_richieste]).strip() + " mancante")
                            print_GUI_error(error_message_gui, "[Errore caricamento esami "+str(anno)+" anno riga "+str(index+2)+"] \nIl laboratorio '" + str(
                                            laboratori_richiesti[index_laboratori_richieste]).strip() + "' inserito non è valido.")
                            return False

        if not pd.isnull(row[7]):  # Parsifico i laboratori e inserisco gli indici associati ad essi
            laboratori_richiesti = parse_list(row[7])
            for index_laboratori_richieste in range(len(laboratori_richiesti)):
                if laboratori_richiesti[index_laboratori_richieste] != '' and laboratori_richiesti[
                    index_laboratori_richieste] != ' ':
                    for index, lab in enumerate(laboratori):
                        if str(lab.nome).strip() == str(laboratori_richiesti[index_laboratori_richieste]).strip():
                            laboratori_richiesti[index_laboratori_richieste] = index

        if pd.isnull(row[8]):
            row[8] = 0
        try:
            if int( row[8]) < 0:
                print("Formato degli slot orari richiesti per i laboratori errato" + str(row[8]))
                print_GUI_error(error_message_gui,
                                "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                    index + 2) + "] \nFormato degli slot orari richiesti per i laboratori errato: " + str(row[8]))
                return False
        except ValueError:
            print("Formato degli slot orari richiesti per i laboratori errato" + str(row[8]))
            print_GUI_error(error_message_gui,
                            "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                index + 2) + "] \nFormato degli slot orari richiesti per i laboratori errato: " + str(row[8]))
            return False

        if pd.isnull(row[9]):
            row[9] = 0
        try:
            if int( row[9]) <= 0:
                print("Formato dei giorni durata esame errato" + str(row[9]))
                print_GUI_error(error_message_gui,
                                "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                    index + 2) + "] \nFormato dei giorni durata esame errato: " + str(row[9]))
                return False
        except ValueError:
            print("Formato dei giorni durata esame errato" + str(row[9]))
            print_GUI_error(error_message_gui,
                            "[Errore caricamento esami " + str(anno) + " anno riga " + str(
                                index + 2) + "] \nFormato dei giorni durata esame errato: " + str(row[9]))
            return False

        if not pd.isnull(row[12]):
            note = row[12]
        if not pd.isnull(row[10]):
            date_preferenza = parse_list(row[10])
            for index_preferenza in range(len(date_preferenza)):
                if '00:00:00' in date_preferenza[index_preferenza]:
                    date = datetime.strptime(
                        date_preferenza[index_preferenza], '%Y-%m-%d %H:%M:%S')
                    if date < sessioni[0][0] or date > sessioni[0][
                        1]:
                        print("Date di preferenza errate, non comprese nella sessione Inizio(" + str(
                            sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        print_GUI_error(error_message_gui, "[Errore caricamento esami "+str(anno)+" anno] \nDate di preferenza errate, non comprese nella sessione "
                                                           "Inizio(" + str(sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        return False
                    date_preferenza[index_preferenza] = date
                else:
                    date = datetime.strptime(
                        date_preferenza[index_preferenza].strip(), '%d/%m/%Y')
                    if date < sessioni[0][0] or date > sessioni[0][
                        1]:
                        print("Date di preferenza errate, non comprese nella sessione Inizio(" + str(
                            sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        print_GUI_error(error_message_gui, "[Errore caricamento esami "+str(anno)+" anno] \nDate di preferenza errate, non comprese nella sessione \nInizio(" + str(
                            sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        return False
                    date_preferenza[index_preferenza] = date

        if not pd.isnull(row[11]):
            date_indisponibilita = parse_list(row[11])
            for index_indisponibilita in range(len(date_indisponibilita)):
                if '00:00:00' in date_indisponibilita[index_indisponibilita]:
                    date = datetime.strptime(
                        date_indisponibilita[index_indisponibilita], '%Y-%m-%d %H:%M:%S')
                    if date < sessioni[0][0] or date > sessioni[0][
                        1]:
                        print("Date di indisponibilità errate, non comprese nella sessione Inizio(" + str(
                            sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        print_GUI_error(error_message_gui,
                                        "[Errore caricamento esami "+str(anno)+" anno] \nDate di indisponibilità errate, non comprese nella sessione: \nInizio(" + str(
                            sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        return False
                    date_indisponibilita[index_indisponibilita] = date
                else:
                    date = datetime.strptime(
                        date_indisponibilita[index_indisponibilita].strip(), '%d/%m/%Y')
                    if date < sessioni[0][0] or date > sessioni[0][1]:
                        print("Date di indisponibilità errate, non comprese nella sessione: Inizio(" + str(
                            sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        print_GUI_error(error_message_gui,
                                        "[Errore caricamento esami "+str(anno)+" anno] \nDate di indisponibilità errate, non comprese nella sessione: \nInizio(" + str(
                            sessioni[0][0]) + "-" + str(sessioni[0][1]) + ") inserito: " + str(date))
                        print(ERRORE)
                        return False
                    date_indisponibilita[index_indisponibilita] = date

        giorni_indisponibili = get_non_working_days(sessioni[0][0], sessioni[0][1])
        date_indisponibilita = [*date_indisponibilita, *giorni_indisponibili]

        exams.append(
            classes.Exam(row[0], row[1], row[2], semestri, anno, int(row[4]), aule_richieste, int(row[6]),
                         laboratori_richiesti, int(row[8]), int(row[9]), date_preferenza, date_indisponibilita, note))
        aule_richieste = []
        laboratori_richiesti = []
        date_indisponibilita = []
        date_preferenza = []

    return True


def check_exist(examRooms, name):
    for exameRoom in examRooms:
        if str(exameRoom.nome) == name:
            return True
    return False


def parse_list(input, delimiter=','):
    if delimiter in str(input):
        return str(input).split(delimiter)
    return [str(input)]


def main():
    building = __import__("model_building7")
    if not load_date('',''):
        return
    printSessioni()
    if not load_parametri('', building, ''):
        return
    printParametri(building)
    if not load_laboratori('', ''):
        return
    printLaboratori()
    if not load_aule('', ''):
        return
    printAule()
    if not load_exams('', 'Corsi I anno triennale', 1, ''):
        return
    if not load_exams('', 'Corsi II anno triennale', 2, ''):
        return
    if not load_exams('', 'Corsi III anno triennale', 3, ''):
        return
    printCorsi()

    # Test del modello
    data_inizio = sessioni[0][0]  # Data inizio sessione estiva
    data_fine = sessioni[0][1]  # Data fine sessione estiva
    model = building.build_model(aule, laboratori, data_inizio, data_fine, exams)
    opt = pyo.SolverFactory('cplex')
    #opt.options['preprocessing presolve'] = 'n'
    #opt.options['mip tolerances mipgap'] = 0.1
    #opt.options['mip tolerances absmipgap'] = 0.1
    opt.options['timelimit'] = 1 * 1 * 30
    path = os.path.join('log', str(datetime.today().strftime('Resolution_%d-%m-%y_%H-%M-%S.log')))
    opt.solve(model, logfile=path)
    #building.print_results(model, exams, data_inizio, data_fine)
    create_output.build_output('', '', exams, laboratori, aule, model, sessioni)
    create_calendar.build_calendar(exams, model, sessioni, '')


def runModel(input, output, progressbar, error_message_gui, model, advanced_settings):
    building = __import__(model)

    print('Modello utilizzato: ', model)
    print('Advanced settings: ', advanced_settings)
    print("--- PARSING FILE INPUT ---")
    while len(sessioni)>0:
        sessioni.pop()
    if not load_date(input, error_message_gui):
        return False
    printSessioni()
    progressbar.UpdateBar(100)
    if not load_parametri(input, building,error_message_gui):
        return False
    printParametri(building)
    progressbar.UpdateBar(200)
    while len(laboratori)>0:
        laboratori.pop()
    if not load_laboratori(input, error_message_gui):
        return False
    printLaboratori()
    progressbar.UpdateBar(250)
    while len(aule) > 0:
        aule.pop()
    if not load_aule(input, error_message_gui):
        return False
    printAule()
    while len(exams) > 0:
        exams.pop()
    if not load_exams(input, 'Corsi I anno triennale', 1, error_message_gui):
        return False
    if not load_exams(input, 'Corsi II anno triennale', 2, error_message_gui):
        return False
    if not load_exams(input, 'Corsi III anno triennale', 3, error_message_gui):
        return False
    printCorsi()

    progressbar.UpdateBar(500)
    data_inizio = sessioni[0][0]  # Data inizio sessione
    data_fine = sessioni[0][1]  # Data fine sessione
    print("--- COSTRUZIONE DEL MODELLO ---")
    model = building.build_model(aule, laboratori, data_inizio, data_fine, exams)
    opt = pyo.SolverFactory('cplex')
    #opt.options['preprocessing presolve'] = 'n'
    try:
        if (advanced_settings['time_limit'] != "None" and int(advanced_settings['time_limit']) > 0):
            opt.options['timelimit'] = int(advanced_settings['time_limit']) * 60
    except ValueError:
        pass

    try:
        if (advanced_settings['gap_tollerance'] != "None" and float(advanced_settings['gap_tollerance']) > 0 and float(
                advanced_settings['gap_tollerance']) < 1):
            opt.options['mip tolerances mipgap'] = round(float(advanced_settings['gap_tollerance']), 2)
            opt.options['mip tolerances absmipgap'] = round(float(advanced_settings['gap_tollerance']), 2)
    except ValueError:
        pass

    path = os.path.join('log', str(datetime.today().strftime('Resolution_%d-%m-%y_%H-%M-%S.log')))
    print("--- RISOLUZIONE DEL MODELLO ---")
    opt.solve(model, logfile=path)
    print("--- RISOLUZIONE  COMPLETATA ---")
    progressbar.UpdateBar(750)
    building.print_results(model, exams, data_inizio, data_fine)
    progressbar.UpdateBar(800)
    print("--- COSTRUZIONE OUTPUT ---")
    create_output.build_output(input, output, exams, laboratori, aule, model, sessioni)
    progressbar.UpdateBar(900)
    create_calendar.build_calendar(exams, model, sessioni, output)
    progressbar.UpdateBar(1000)
    print("--- ESECUZIONE COMPLETATA ---")
    return True


if __name__ == '__main__':
    main()
