from classes import Exam
from classes import ExamRoom
from datetime import datetime,timedelta
from pyomo.environ import *
import pyomo.environ as pyo
import holidays

MIN_DISTANCE_APPELLI = 10
SLOT_AULE = 2
SLOT_LABORATORI = 3
GUADAGNO_GIORNI_PREFERITI = 2
COSTANTE_IMPORTANZA_PRIMO_ANNO = 4
COSTANTE_IMPORTANZA_SECONDO_ANNO = 4

def get_non_working_days(data_inizio, data_fine):

    delta = data_fine - data_inizio  # as timedelta
    weekend = []
    for i in range(delta.days + 1):
        day = data_inizio + timedelta(days=i)
        if day.weekday() > 4:
            weekend.append( (day - data_inizio).days)
    #Aggiungo i giorni festivi
        if day in holidays.Italy(years=data_inizio.year) and day not in weekend:
            weekend.append((day - data_inizio).days)
    return weekend

def build_model(aule, laboratori, data_inizio, data_fine, exams):
    model = ConcreteModel()
    days = (data_fine - data_inizio).days + 1  # Calculate the number of days of the range counting for also the first and last day

    #Parametri del modello
    model.days = range(days)
    model.exams = range(len(exams))
    model.aule = range(len(aule))
    model.lab = range(len(laboratori))
    model.richieste_lab_esami = build_richieste_lab_esami(exams, laboratori)
    model.richieste_aule_esami = build_richieste_aule_esami(exams, aule)
    model.aule_disponibilita = build_aule_disponibilita(aule, days, data_inizio)
    model.lab_disponibilita = build_lab_disponibilita(laboratori, days, data_inizio)
    model.preferenze_professori = build_preferenze_professori(exams, days, data_inizio)


    #Variabili
    model.x = Var(model.exams, model.days, within=pyo.Binary)
    model.dummy_primo_anno = Var(within=pyo.NonNegativeIntegers)
    model.dummy_secondo_anno = Var(within=pyo.NonNegativeIntegers)

    #Funzione obiettivo
    def obj_rule(model):
        return sum(model.x[esame,giorno]*model.preferenze_professori[esame][giorno] for giorno in model.days for esame in model.exams) - (model.dummy_primo_anno * COSTANTE_IMPORTANZA_PRIMO_ANNO + model.dummy_secondo_anno*COSTANTE_IMPORTANZA_SECONDO_ANNO)
    model.obj = Objective(expr=obj_rule,sense=maximize)


    #Vincoli
    model.correct_exam_days = ConstraintList()  # Assegniamo esattamente il numero di giorni richiesto da un esame
    for i in model.exams:
        model.correct_exam_days.add(
            sum(model.x[i, j] for j in model.days) == (
                    exams[i].numero_appelli_sessione_full * exams[i].numero_giorni_durata))

    model.min_distance_appelli = ConstraintList()  # Per ogni esame la distanza minima tra i due appelli deve essere almeno MIN_DISTANCE_APPELLI
    for esame in model.exams:
        for giorno in range(days-1):
            lower_bound=0
            if giorno-MIN_DISTANCE_APPELLI>0:
                lower_bound=giorno-MIN_DISTANCE_APPELLI
            upper_bound=days-1
            if giorno+MIN_DISTANCE_APPELLI<upper_bound:
                upper_bound=giorno+MIN_DISTANCE_APPELLI
            model.min_distance_appelli.add(     #Per ogni esame se siamo nell'ultimo giorno di assegnamento, nei successivi MIN_DISTANCE_APPELLI giorni non ci devono essere assegniamenti
                (1-model.x[esame,giorno] + (model.x[esame,giorno+1]))*days >=
                sum(model.x[esame,giorno_2] for giorno_2 in range((giorno+1) , upper_bound))
            )
            if exams[esame].numero_giorni_durata > 1:
                model.min_distance_appelli.add(     #Per ogni esame se siamo nell'ultimo giorno di assegnamento nei precedenti MIN_DISTANCE_APPELLI  giorno abbiamo un numero di assegnamenti pari a num_giorni_duarat
                    (model.x[esame, giorno] * (1 - model.x[esame, giorno + 1])) * exams[esame].numero_giorni_durata +
                    (model.x[esame,giorno+1])* days +
                    (1-model.x[esame, giorno]) * days >=
                    sum(model.x[esame, giorno_2] for giorno_2 in range(giorno, lower_bound-1, -1))
                )
        if exams[esame].numero_giorni_durata > 1:
            model.min_distance_appelli.add(
                # Per ogni esame se siamo nell'ultimo giorno di assegnamento nei precedenti MIN_DISTANCE_APPELLI  giorno abbiamo un numero di assegnamenti pari a num_giorni_duarat
                (model.x[esame, days - 1]) * exams[esame].numero_giorni_durata +
                (1 - model.x[esame, days - 1]) * days >=
                sum(model.x[esame, giorno_2] for giorno_2 in range(days - 1, days - 1 - MIN_DISTANCE_APPELLI, -1))
            )


    model.assegniamenti_contigui = ConstraintList()  # Per ogni esame assegno i giorni contigui necessari
    for esame in model.exams:
        if (exams[esame].numero_giorni_durata > 1):
            for giorno in range(1, days - exams[esame].numero_giorni_durata):
                model.assegniamenti_contigui.add(
                    ((1 - model.x[esame, (giorno - 1)]) * model.x[esame, giorno] * exams[esame].numero_giorni_durata) <=
                    sum(model.x[esame, giorno_2] for giorno_2 in
                        range(giorno, (giorno + exams[esame].numero_giorni_durata)))
                )
            model.assegniamenti_contigui.add(
                (model.x[esame, 0] * exams[esame].numero_giorni_durata) <=
                sum(model.x[esame, giorno_2] for giorno_2 in
                    range(exams[esame].numero_giorni_durata))
            )

    model.limiti_aule = ConstraintList()  # Per ogni giorno non superiamo i limiti di assegniamento delle aule
    for giorno in model.days:
        for aula in model.aule:
            found = False
            esami_in_aula=[]
            for index,exam in enumerate(exams):
                if (aula in exam.aule_richieste):
                    found = True
                    esami_in_aula.append(index)
            if found:
                model.limiti_aule.add((
                        sum(model.x[esame, giorno] * model.richieste_aule_esami[esame][aula]
                            for esame in esami_in_aula) <=
                        model.aule_disponibilita[aula][giorno]
                ))

    model.limiti_lab = ConstraintList()  # Per ogni giorno non superiamo i limiti di assegniamento delle aule
    for giorno in model.days:
        for lab in model.lab:
            found = False
            esame_in_lab=[]
            for index,exam in enumerate(exams):
                if (lab in exam.laboratori_richiesti):
                    found = True
                    esame_in_lab.append(index)
            if found:
                model.limiti_lab.add((
                        sum(model.x[esame, giorno] * model.richieste_lab_esami[esame][lab]
                            for esame in esame_in_lab) <=
                        model.lab_disponibilita[lab][giorno]
                ))
    model.indisp_professori = ConstraintList()  # Per ogni esame non lo assegno nei giorni di indisponibilità dei professori
    for exam in model.exams:
        for day in model.days:
            if model.preferenze_professori[exam][day] == 0:
                model.indisp_professori.add(
                    model.x[exam, day] == 0
                )

    model.esami_stesso_semestre_diversi = ConstraintList()  # Non assegno due esami dello stesso semestre lo stesso giorno
    esami_semestre=list()       #Creo una lista di dimensione [anni][semestre] che contiene liste di corsi
    for anno in range(3):
        esami_semestre.append([])
        for semestre in range(2):
            esami_semestre[anno].append([])
            for esame in model.exams:
                if exams[esame].anno==(anno+1):
                    if(semestre+1) in exams[esame].lista_semestri:
                        esami_semestre[anno][semestre].append(esame)
            if len(esami_semestre[anno][semestre]) > 1:
                for giorno in model.days:
                    model.esami_stesso_semestre_diversi.add(
                        sum(model.x[esame1,giorno] for esame1 in esami_semestre[anno][semestre])<=1
                    )

    model.esami_primo_anno_diversi = ConstraintList()  # Provo a non assegnare due esami del primo anno lo stesso giorno
    esami_primo_anno = list()  # Creo una lista di dimensione [anni][semestre] che contiene liste di corsi
    for esame in model.exams:
        if exams[esame].anno == 1:
            esami_primo_anno.append(esame)
    if len(esami_primo_anno) > 1:
        for giorno in model.days:
            model.esami_stesso_semestre_diversi.add(
                sum(model.x[esame1, giorno] for esame1 in esami_primo_anno) <= 1 + model.dummy_primo_anno)

    model.esami_secondo_anno_diversi = ConstraintList()  # Provo a non assegnare due esami del secondo anno lo stesso giorno
    esami_secondo_anno = list()  # Creo una lista di dimensione [anni][semestre] che contiene liste di corsi
    for esame in model.exams:
        if exams[esame].anno == 2:
            esami_secondo_anno.append(esame)
    if len(esami_secondo_anno) > 1:
        for giorno in model.days:
            model.esami_stesso_semestre_diversi.add(
                sum(model.x[esame1, giorno] for esame1 in esami_secondo_anno) <= 1 + model.dummy_secondo_anno)



    return model


def build_richieste_lab_esami(exams, laboratori):
    richieste_lab_esami = list()  # Lista di laboratori richiesti dagli esami, per ogni esame assegna un array di dimensione aule elementi settati a 0
    for exam_index in range(len(exams)):
        richieste_lab_esami.append(list())
        for lab_index in range(len(laboratori)):
            richieste_lab_esami[exam_index].append(0)
        # Ora attivo i lab richiesti
        for lab in exams[exam_index].laboratori_richiesti:
            richieste_lab_esami[exam_index][lab] = exams[exam_index].numero_lab_slot
    return richieste_lab_esami


def build_richieste_aule_esami(exams, aule):
    richieste_aule_esami = list()  # Lista di aule richieste dagli esami, per ogni esame assegna un array di dimensione aule elementi settati a 0
    for exam_index in range(len(exams)):
        richieste_aule_esami.append(list())
        for aula_index in range(len(aule)):
            richieste_aule_esami[exam_index].append(0)
        # Ora attivo le aule richieste
        for aula in exams[exam_index].aule_richieste:
            richieste_aule_esami[exam_index][aula] = exams[exam_index].numero_aule_slot
    return richieste_aule_esami


def build_lab_disponibilita(laboratori, days, data_inizio):
    lab_disponibilita = list()  # Lista di giorni di disponibilità dei laboratori, per ogni laboratorio assegna un array di dimensione days elementi settati a 1
    for lab_index in range(len(laboratori)):
        lab_disponibilita.append(list())
        for giorno in range(days):
            lab_disponibilita[lab_index].append(SLOT_LABORATORI)
        # Ora metto a 0 i giorni di indisponibilita
        for data_indisponibilita in laboratori[lab_index].indisponibilita:
            distance = (data_indisponibilita - data_inizio).days
            if distance>=0 and distance<len(lab_disponibilita[lab_index]):
                lab_disponibilita[lab_index][distance] = 0
    return lab_disponibilita


def build_aule_disponibilita(aule, days, data_inizio):
    aule_disponibilita = list()  # Lista di giorni di disponibilità delle aule, per ogni aula assegna un array di dimensione days elementi settati a 1
    for aula_index in range(len(aule)):
        aule_disponibilita.append(list())
        for giorno in range(days):
            aule_disponibilita[aula_index].append(SLOT_AULE)
        # Ora metto a 0 i giorni di indisponibilita
        for data_indisponibilita in aule[aula_index].indisponibilita:
            distance = (data_indisponibilita - data_inizio).days
            aule_disponibilita[aula_index][distance] = 0
    return aule_disponibilita


def build_preferenze_professori(exams, days, data_inizio):
    preferenze_professori = list()  # Lista di giorni di disponibilità delle aule, per ogni aula assegna un array di dimensione days elementi settati a 1
    for exam_index in range(len(exams)):
        preferenze_professori.append(list())
        for giorno in range(days):
            preferenze_professori[exam_index].append(1)
        # Ora metto a 0 i giorni di indisponibilita
        for data_indisponibilita in exams[exam_index].date_indisponibilita:
            distance = (data_indisponibilita - data_inizio).days
            preferenze_professori[exam_index][distance] = 0
        for data_preferenza in exams[exam_index].date_preferenza:
            distance = (data_preferenza - data_inizio).days
            preferenze_professori[exam_index][distance] = GUADAGNO_GIORNI_PREFERITI
        # Ora metto a costante moltiplicativa le date preferite
    return preferenze_professori

def print_results(model, exams, data_inizio, data_fine):
    giorni_indisp_generali=get_non_working_days(data_inizio,data_fine)

    days = (data_fine - data_inizio).days + 1
    for i in range(len(exams)):
        print(exams[i].nome)
        for j in range(days):
            if j in giorni_indisp_generali:
                print('\033[91m',end="")
            print("[", end="")
            if (int(model.x[i, j].value) == 1):
                print('\033[92m' + str(int(model.x[i, j].value)) + '\033[0m', end="]")
            else:
                print(int(model.x[i, j].value), end="]")
            print('\033[0m', end="")

        print("]")
    print("Dummy primo anno: ", '\033[92m', model.dummy_primo_anno.value, '\033[0m')
    print("Dummy secondo anno: ", '\033[92m', model.dummy_secondo_anno.value, '\033[0m')


