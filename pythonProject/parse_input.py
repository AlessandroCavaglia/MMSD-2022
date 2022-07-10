# This file parsing the xlsx input
# AULE (Nome,Indisponibilità)
# LABORATORI (Nome,Indisponibilità)
# SESSIONE (Nome, DataInizio, DataFine)
# ESAME(

import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import Classes
import costants

laboratori = []
aule = []
exams = []


def get_non_working_days(sdate, edate):
    data_inizio = datetime.strptime(sdate, '%d/%m/%Y')
    data_fine = datetime.strptime(edate, '%d/%m/%Y')
    delta = data_fine - data_inizio  # as timedelta
    weekend = []
    for i in range(delta.days + 1):
        day = data_inizio + timedelta(days=i)
        if day.weekday() > 4:
            weekend.append(day)

    return weekend


def load_input():
    sessione_df = pd.read_excel('input/input modello.xlsx', sheet_name='Input generali 2.0', skiprows=1,
                                usecols=costants.COLONNE_SESSIONI)
    exams_df = pd.read_excel('input/input modello.xlsx', sheet_name='Corsi I anno triennale')
    print(exams_df)


def load_laboratori():
    laboratorii_df = pd.read_excel('input/input modello.xlsx', sheet_name='Input generali 2.0', skiprows=1,
                                   usecols=costants.COLONNE_LABORATORI)
    for index, row in laboratorii_df.iterrows():
        # row[0] -> Nome Laboratorio -> String
        # row[1] -> Indisponibilità -> String {Data1,...,DataN}
        aule.append(Classes.ExamRoom(row[0], row[1]))


def load_aule():
    aule_df = pd.read_excel('input/input modello.xlsx', sheet_name='Input generali 2.0', skiprows=1,
                            usecols=costants.COLONNE_AULE)
    for index, row in aule_df.iterrows():
        # row[0] -> Nome Aula -> String
        # row[1] -> Indisponibilità -> String {Data1,...,DataN}
        aule.append(Classes.ExamRoom(row[0], row[1]))


def load_exams():
    exams_df = pd.read_excel('input/input modello.xlsx', sheet_name='Corsi I anno triennale')
    for index, row in exams_df.iterrows():
        # row[0] -> Nome Corso -> String
        # row[1] -> Tipologia -> String
        # row[2] -> Docenti -> String
        # row[3] -> Semestri Corso -> String {1,2}
        if '1' not in str(row[3]) and '2' not in str(row[3]):
            return False
        # row[4] -> Numero appelli sessioni estiva/invernali -> int
        # row[5] -> Numero appelli sessioni di settembre -> int
        # row[6] -> Aule Richieste -> String {Aula1,...,AulaN}
        if not aule:
            return False
        # row[7] -> Slot orari richiesti per le aule -> int >= 1 && <= 2
        if row[7] > 2 or row[7] < 1:
            return False
        # row[8] -> Laboratori richiesti -> String {Laboratorio1,...,LaboratorioN}
        if not laboratori:
            return False
        # row[9] -> Slot orari richiesti per i laboratori -> int >= 1 && <= 3
        if row[9] > 3 or row[9] < 1:
            return False
        # row[10] -> Giorni di durata dell'esame -> int
        # row[11] -> Date di preferenza dei professori -> String {Data1,...,DataN}
        # row[12] -> Date di indisponibilità dei professori -> String {Data1,...,DataN}
        # row[13] -> Note -> String
        exams.append(
            Classes.Exam(row[0], row[1], row[2], parse_list(row[3]), 1, row[4], row[5], parse_list(row[6]), row[7],
                         parse_list(row[8]), row[9], parse_list(row[10]), parse_list(row[11]), row[12], row[13]))

    return True


def parse_list(input):
    if ',' in str(input):
        return str(input).split(',')
    return str(input)


if __name__ == '__main__':
    load_input()
    if load_exams():
        print(exams[2].aule_richieste)
    print(get_non_working_days("01/07/2022", "31/07/2022"))
