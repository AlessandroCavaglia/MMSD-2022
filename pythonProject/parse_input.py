# This file parsing the xlsx input
# AULE (Nome,Indisponibilità)
# LABORATORI (Nome,Indisponibilità)
# SESSIONE (Nome, DataInizio, DataFine)
# ESAME(

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import classes
import costants
import create_output
import holidays

from model_building import *
import pyomo.environ as pyo

sessioni = []
laboratori = []
aule = []
exams = []
ERRORE = ""


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
        print("Nome")
        print(corso.nome)
        print("Tipo")
        print(corso.tipo)
        print("Insegnanti")
        print(corso.insegnanti)
        print("Lista semestri")
        print(corso.lista_semestri)
        print("Anno")
        print(corso.anno)
        print("Numero appelli sessione full")
        print(corso.numero_appelli_sessione_full)
        print("Numero appelli sessione small")
        print(corso.numero_appelli_sessione_small)
        print("Aule richieste")
        print(corso.aule_richieste)
        print("Slot aule")
        print(corso.numero_aule_slot)
        print("Laboratori richiesti")
        print(corso.laboratori_richiesti)
        print("Slot laboratori")
        print(corso.numero_lab_slot)
        print("Durata giorni")
        print(corso.numero_giorni_durata)
        print("Date di preferenza")
        print(corso.date_preferenza)
        print("Date di indisponibilità")
        print(corso.date_indisponibilita)
        print("Note")
        print(corso.note)


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


def load_date():  # Errori gestiti da testare a fondo
    sessioni_df = pd.read_excel('input/'+costants.INPUT_FILE_NAME, sheet_name='Input generali 2.0', skiprows=1,
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
                    return False
            except:
                print("Date in formato errato tra le seguenti: ", row[0], " e ", row[1])
                return False
    return True


def load_laboratori():  # Errori gestiti da testare a fondo
    laboratorii_df = pd.read_excel('input/'+costants.INPUT_FILE_NAME, sheet_name='Input generali 2.0', skiprows=1,
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
                            ERRORE = "Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido"
                            return False
                    else:
                        try:
                            dateindisp[index] = datetime.strptime(dateindisp[index].strip(), '%d/%m/%Y')
                        except:
                            ERRORE = "Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido"
                            return False
                    found = False  # Per ogni data di indisponibilità verifico che sia in qualche sessione
                    for sessione in sessioni:
                        if dateindisp[index] >= sessione[0] and dateindisp[index] <= sessione[1]:
                            found = True
                    if not found:
                        ERRORE = "Data di indisponibilità del laboratorio " + row[
                            0] + " non è in nessuna sessione di quelle impostate"
                        return False
            laboratori.append(classes.ExamRoom(row[0], dateindisp))
    return True


def load_aule():  # Errori gestiti da testare a fondo
    aule_df = pd.read_excel('input/'+costants.INPUT_FILE_NAME, sheet_name='Input generali 2.0', skiprows=1,
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
                            ERRORE = "Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido"
                            return False
                    else:
                        try:
                            dateindisp[index] = datetime.strptime(dateindisp[index].strip(), '%d/%m/%Y')
                        except:
                            ERRORE = "Data di indisponibilità del laboratorio " + row[0] + " in un formato non valido"
                            return False
                found = False  # Per ogni data di indisponibilità verifico che sia in qualche sessione
                for sessione in sessioni:
                    if dateindisp[index] >= sessione[0] and dateindisp[index] <= sessione[1]:
                        found = True
                if not found:
                    ERRORE = "Data di indisponibilità del laboratorio " + row[
                        0] + " non è in nessuna sessione di quelle impostate"
                    return False
            aule.append(classes.ExamRoom(row[0], dateindisp))
    return True


def load_exams_first_year():
    aule_richieste = []
    laboratori_richiesti = []
    date_indisponibilita = []
    date_preferenza = []
    note = ""
    exams_df = pd.read_excel('input/'+costants.INPUT_FILE_NAME, sheet_name='Corsi I anno triennale')
    for index, row in exams_df.iterrows():
        # row[0] -> Nome Corso -> String
        # row[1] -> Tipologia -> String
        # row[2] -> Docenti -> String
        # row[3] -> Semestri Corso -> String {1,2}
        # row[4] -> Numero appelli sessioni estiva/invernali -> int
        # row[5] -> Numero appelli sessioni di settembre -> int
        # row[6] -> Aule Richieste -> String {Aula1,...,AulaN}
        # row[7] -> Slot orari richiesti per le aule -> int >= 1 && <= 2
        # row[8] -> Laboratori richiesti -> String {Laboratorio1,...,LaboratorioN}
        # row[9] -> Slot orari richiesti per i laboratori -> int >= 1 && <= 3
        # row[10] -> Giorni di durata dell'esame -> int
        # row[11] -> Date di preferenza dei professori -> String {Data1,...,DataN}
        # row[12] -> Date di indisponibilità dei professori -> String {Data1,...,DataN}
        # row[13] -> Note -> String
        semestri = str(row[3]).replace('.0', '')
        semestri = parse_list(semestri, '.')
        for semestre in semestri:
            if semestre != "1" and semestre != "2":
                ERRORE = " Formato dei semestri errato " + str(row[3])
                return False

        if not pd.isnull(row[6]):  # Controllo che gli esami abbiano aule esistenti inseriti in input generali
            aule_richieste = parse_list(row[6])
            for index_aule_richieste in range(len(aule_richieste)):
                for index, aula in enumerate(aule):
                    if not check_exist(aule, str(aule_richieste[index_aule_richieste]).strip()):
                        ERRORE = "Errore nel caricamento del flusso " + str(
                            aule_richieste[index_aule_richieste]).strip() + " mancante"
                        return False

        if not pd.isnull(row[6]):  # Parsifico le aule e inserisco l'indice associato ad esse
            aule_richieste = parse_list(row[6])
            for index_aule_richieste in range(len(aule_richieste)):
                for index, aula in enumerate(aule):
                    if str(aula.nome).strip() == str(aule_richieste[index_aule_richieste]).strip():
                        aule_richieste[index_aule_richieste] = index

        if pd.isnull(row[7]):
            row[7] = 0

        if not pd.isnull(row[8]):  # Controllo che gli esami abbiano laboratori esistenti inseriti in input generali
            laboratori_richiesti = parse_list(row[8])
            for index_laboratori_richieste in range(len(laboratori_richiesti)):
                for index, lab in enumerate(laboratori):
                    if not check_exist(laboratori, str(laboratori_richiesti[index_laboratori_richieste]).strip()):
                        ERRORE = "Errore nel caricamento del flusso " + str(
                            laboratori_richiesti[index_laboratori_richieste]).strip() + " mancante"
                        return False

        if not pd.isnull(row[8]):  # Parsifico i laboratori e inserisco gli indici associati ad essi
            laboratori_richiesti = parse_list(row[8])
            for index_laboratori_richieste in range(len(laboratori_richiesti)):
                for index, lab in enumerate(laboratori):
                    if str(lab.nome).strip() == str(laboratori_richiesti[index_laboratori_richieste]).strip():
                        laboratori_richiesti[index_laboratori_richieste] = index

        if pd.isnull(row[9]):
            row[9] = 0
        if not pd.isnull(row[13]):
            note = row[13]
        if not pd.isnull(row[11]):
            date_preferenza = parse_list(row[11])
            for index_preferenza in range(len(date_preferenza)):
                if '00:00:00' in date_preferenza[index_preferenza]:
                    date = datetime.strptime(
                        date_preferenza[index_preferenza], '%Y-%m-%d %H:%M:%S')
                    if date < sessioni[1][0] or date > sessioni[1][1]: # TODO: UTILIZZARE DATE GIUSTE ATTUALMENTE SI LAVORA SEMPRE SULLA SESSIONE ESTIVA
                        ERRORE = "Date di preferenza errate, non comprese nella sessione Inizio(" + str(
                            sessioni[1][0]) + "-" + str(sessioni[1][1]) + ") inserito: " + str(date)
                        return False
                    date_preferenza[index_preferenza] = date
                else:
                    date = datetime.strptime(
                        date_preferenza[index_preferenza].strip(), '%d/%m/%Y')
                    if date < sessioni[1][0] or date > sessioni[1][1]: #TODO: UTILIZZARE DATE GIUSTE ATTUALMENTE SI LAVORA SEMPRE SULLA SESSIONE ESTIVA
                        ERRORE = "Date di preferenza errate, non comprese nella sessione Inizio(" + str(
                            sessioni[1][0]) + "-" + str(sessioni[1][1]) + ") inserito: " + str(date)
                        return False
                    date_preferenza[index_preferenza] = date


        if not pd.isnull(row[12]):
            date_indisponibilita = parse_list(row[12])
            for index_indisponibilita in range(len(date_indisponibilita)):
                if '00:00:00' in date_indisponibilita[index_indisponibilita]:
                    date = datetime.strptime(
                        date_indisponibilita[index_indisponibilita], '%Y-%m-%d %H:%M:%S')
                    if date < sessioni[1][0] or date > sessioni[1][1]: #TODO: UTILIZZARE DATE GIUSTE ATTUALMENTE SI LAVORA SEMPRE SULLA SESSIONE ESTIVA
                        ERRORE = "Date di indisponibilità errate, non comprese nella sessione Inizio(" + str(
                            sessioni[1][0]) + "-" + str(sessioni[1][1]) + ") inserito: " + str(date)
                        return False
                    date_indisponibilita[index_indisponibilita] = date
                else:
                    date = datetime.strptime(
                        date_indisponibilita[index_indisponibilita].strip(), '%d/%m/%Y')
                    if date < sessioni[1][0] or date > sessioni[1][1]: #TODO: UTILIZZARE DATE GIUSTE ATTUALMENTE SI LAVORA SEMPRE SULLA SESSIONE ESTIVA
                        ERRORE = "Date di indisponibilità errate, non comprese nella sessione: Inizio(" + str(
                            sessioni[1][0]) + "-" + str(sessioni[1][1]) + ") inserito: " + str(date)
                        print(ERRORE)
                        return False
                    date_indisponibilita[index_indisponibilita] = date

        giorni_indisponibili = get_non_working_days(sessioni[1][0], sessioni[1][
            1])  # UTILIZZARE DATE GIUSTE ATTUALMENTE SI LAVORA SEMPRE SULLA SESSIONE ESTIVA
        date_indisponibilita = [*date_indisponibilita, *giorni_indisponibili]

        exams.append(
            classes.Exam(row[0], row[1], row[2], semestri, 1, int(row[4]), int(row[5]), aule_richieste, int(row[7]),
                         laboratori_richiesti, int(row[9]), int(row[10]), date_preferenza, date_indisponibilita, note))

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
    if not load_date():
        print("Errore durante il caricamento delle sessioni: " + ERRORE)
        return
    printSessioni()
    if not load_laboratori():
        print("Errore durante il caricamento dei laboratori: " + ERRORE)
        return
    printLaboratori()
    print(check_exist(laboratori, "Laboratorio Dijkstra"))
    if not load_aule():
        print("Errore durante il caricamento delle aule: " + ERRORE)
        return
    printAule()
    if not load_exams_first_year():
        print("Errore durante il caricamento dei corsi del primo anno: " + ERRORE)
        return
    printCorsi()

    # Test del modello
    data_inizio = sessioni[1][0]  # Data inizio sessione estiva
    data_fine = sessioni[1][1]  # Data fine sessione estiva
    model = build_model(aule, laboratori, data_inizio, data_fine, exams)
    opt = pyo.SolverFactory('cplex')
    opt.solve(model)
    print_results(model, exams, data_inizio, data_fine)
    create_output.build_output(exams, laboratori, aule, "",model,"",sessioni)

if __name__ == '__main__':
    main()
