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
import holidays


from model_building import *
import pyomo.environ as pyo

laboratori = []
aule = []
exams = []

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

def get_non_working_days(sdate, edate):
    data_inizio = datetime.strptime(sdate, '%d/%m/%Y')
    data_fine = datetime.strptime(edate, '%d/%m/%Y')
    delta = data_fine - data_inizio  # as timedelta
    weekend = []
    for i in range(delta.days + 1):
        day = data_inizio + timedelta(days=i)
        if day.weekday() > 4:
            weekend.append(day)
    #Aggiungo i giorni festivi
        if day in holidays.Italy(years=data_inizio.year) and day not in weekend:
            weekend.append(day)
    return weekend


def load_input():
    sessione_df = pd.read_excel('input/input modello.xlsx', sheet_name='Input generali 2.0', skiprows=1,
                                usecols=costants.COLONNE_SESSIONI)
    exams_df = pd.read_excel('input/input modello.xlsx', sheet_name='Corsi I anno triennale')
    #print(exams_df)


def load_laboratori():
    laboratorii_df = pd.read_excel('input/input modello.xlsx', sheet_name='Input generali 2.0', skiprows=1,
                                   usecols=costants.COLONNE_LABORATORI)
    for index, row in laboratorii_df.iterrows():
        # row[0] -> Nome Laboratorio -> String
        # row[1] -> Indisponibilità -> String {Data1,...,DataN}
        if not pd.isnull(row[0]):
            dateindisp=[]
            if not pd.isnull(row[1]):
                dateindisp=parse_list(row[1])
                for index in range(len(dateindisp)):
                    if '00:00:00' in dateindisp[index]:
                        dateindisp[index] = datetime.strptime(dateindisp[index], '%Y-%m-%d %H:%M:%S')
                    else:
                        dateindisp[index] = datetime.strptime(dateindisp[index].strip(), '%d/%m/%Y')
            #TODO CONTROLLO CHE LA DATA SIA IN FORMATO CORRETTO
            #TODO CONTROLLO CHE LA DATA SIA CONTENUTA TRA LA DATA DI INIZIO E DI FINE
            laboratori.append(classes.ExamRoom(row[0], dateindisp))


def load_aule():
    aule_df = pd.read_excel('input/input modello.xlsx', sheet_name='Input generali 2.0', skiprows=1,
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
                        dateindisp[index] = datetime.strptime(dateindisp[index], '%Y-%m-%d %H:%M:%S')
                    else:
                        dateindisp[index] = datetime.strptime(dateindisp[index].strip(), '%d/%m/%Y')

                # TODO CONTROLLO CHE LA DATA SIA IN FORMATO CORRETTO
                # TODO CONTROLLO CHE LA DATA SIA CONTENUTA TRA LA DATA DI INIZIO E DI FINE
            aule.append(classes.ExamRoom(row[0], dateindisp))


def load_exams_first_year():
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
        semestri=str(row[3]).replace('.0','')
        aule_richieste=[]
        laboratori_richiesti=[]
        date_indisponibilita=[]
        date_preferenza=[]
        note=""
        #TODO VERIFICARE CHE OGNI AULA E LABORATORIO SIA NEL NOSTRO ELENCO
        if  not pd.isnull(row[6]):
            aule_richieste=parse_list(row[6])
            for index_aule_richieste in range(len(aule_richieste)):
                for index,aula in enumerate(aule):
                    if str(aula.nome).strip()==str(aule_richieste[index_aule_richieste]).strip():
                        aule_richieste[index_aule_richieste] = index

        if pd.isnull(row[7]):
            row[7]=0
        if  not pd.isnull(row[8]):
            laboratori_richiesti=parse_list(row[8])
            for index_laboratori_richieste in range(len(laboratori_richiesti)):
                for index,lab in enumerate(laboratori):
                    if str(lab.nome).strip() == str(laboratori_richiesti[index_laboratori_richieste]).strip():
                        laboratori_richiesti[index_laboratori_richieste] = index


        if pd.isnull(row[9]):
            row[9]=0
        if not pd.isnull(row[13]):
            note=row[13]
        if not pd.isnull(row[11]):
            date_preferenza = parse_list(row[11])
            for index_preferenza in range(len(date_preferenza)):
                if '00:00:00' in date_preferenza[index_preferenza]:
                    date_preferenza[index_preferenza] = datetime.strptime(date_preferenza[index_preferenza], '%Y-%m-%d %H:%M:%S')
                else:
                    date_preferenza[index_preferenza] = datetime.strptime(date_preferenza[index_preferenza].strip(), '%d/%m/%Y')
        if not pd.isnull(row[12]):
            date_indisponibilita=parse_list(row[12])
            for index_indisponibilita in range(len(date_indisponibilita)):
                if '00:00:00' in date_indisponibilita[index_indisponibilita]:
                    date_indisponibilita[index_indisponibilita] = datetime.strptime(date_indisponibilita[index_indisponibilita], '%Y-%m-%d %H:%M:%S')
                else:
                    date_indisponibilita[index_indisponibilita] = datetime.strptime(date_indisponibilita[index_indisponibilita].strip(), '%d/%m/%Y')

        giorni_indisponibili=get_non_working_days("09/06/2023", "28/07/2023") #UTILIZZARE DATE GIUSTE
        date_indisponibilita=[*date_indisponibilita,*giorni_indisponibili]


        exams.append(
            classes.Exam(row[0], row[1], row[2], parse_list(semestri,'.'), 1, int(row[4]), int(row[5]), aule_richieste, int(row[7]),
                         laboratori_richiesti, int(row[9]), int(row[10]), date_preferenza, date_indisponibilita, note))

    return True


def parse_list(input,delimiter=','):
    if delimiter in str(input):
        return str(input).split(delimiter)
    return [str(input)]


if __name__ == '__main__':
    #load_input()
    #TODO GESTIRE ERRORI
    load_laboratori()
    load_aule()
    printAule()
    printLaboratori()
    if load_exams_first_year():
        printCorsi()
        #print(exams[2].aule_richieste)



    #print(get_non_working_days("01/07/2022", "31/07/2022"))

    #Prova del modello sui dati di input
    data_inizio = datetime.strptime("09/06/2023", '%d/%m/%Y')
    data_fine = datetime.strptime("28/07/2023", '%d/%m/%Y')
    model = build_model(aule, laboratori, data_inizio, data_fine, exams)
    opt = pyo.SolverFactory('cplex')
    opt.solve(model)
    print_results(model, exams, data_inizio, data_fine)

