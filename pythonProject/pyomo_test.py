from Classes import Exam
from Classes import ExamRoom
from datetime import datetime
from pyomo.environ import *
import pyomo.environ as pyo

MIN_DISTANCE_APPELLI = 10
SLOT_AULE = 2
SLOT_LABORATORI = 3


def main():
    aule = [ExamRoom("Aula A", []),
            ExamRoom("Aula B", []),
            ExamRoom("Aula C", []),
            ExamRoom("Aula D", []),
            ExamRoom("Aula E", []),
            ExamRoom("Aula F", []),
            ExamRoom("Sala conferenze", [])]
    laboratori = [ExamRoom("Laboratorio Dijkstra", [datetime.strptime("09/06/2023", '%d/%m/%Y')]), #NECESSARIO BUGFIX PER ASSEGNIAMENTO GIORNI CONTIGUI
                  ExamRoom("Laboratorio Vonneumann", []),
                  ExamRoom("Laboratorio Turing", []),
                  ExamRoom("Laboratorio Babbage", []),
                  ExamRoom("Laboratorio Postel", [])]

    data_inizio = datetime.strptime("08/06/2023", '%d/%m/%Y')
    data_fine = datetime.strptime("28/07/2023", '%d/%m/%Y')

    exams = list()
    exams.append(
        Exam("CMRO", "Scritto", "Insegnante1, Insegnante 2", [1], 1, 2, 1, [], 0, [0, 1], 3, 2, [], [], "Note"))
    exams.append(
        Exam("MDL", "Scritto", "Insegnante1, Insegnante 2", [1], 1, 2, 1, [0, 1, 2, 3], 2, [], 0, 1, [], [], "Note"))

    model = build_model(aule, laboratori, data_inizio, data_fine, exams)
    opt = pyo.SolverFactory('cplex')
    opt.solve(model)
    print_results(model, exams, data_inizio, data_fine)


def build_model(aule, laboratori, data_inizio, data_fine, exams):
    days = (data_fine - data_inizio).days + 1  # Calculate the number of days of the range counting for also the first and last day

    model = ConcreteModel()
    model.days = range(days)
    model.exams = range(len(exams))
    model.aule = range(len(aule))
    model.lab = range(len(laboratori))
    model.richieste_lab_esami=build_richieste_lab_esami(exams,laboratori)
    model.richieste_aule_esami=build_richieste_aule_esami(exams,aule)
    model.aule_disponibilita=build_aule_disponibilita(aule,days,data_inizio)
    model.lab_disponibilita=build_lab_disponibilita(laboratori,days,data_inizio)

    model.x = Var(model.exams, model.days, within=pyo.Binary)
    model.dummy = Var(within=pyo.NonNegativeIntegers)
    model.obj = Objective(expr=model.dummy)

    model.correct_exam_days = ConstraintList()  # Assegniamo esattamente il numero di giorni richiesto da un esame
    for i in model.exams:
        model.correct_exam_days.add(
            sum(model.x[i, j] for j in model.days) == (
                        exams[i].numero_appelli_sessione_full * exams[i].numero_giorni_durata))

    model.min_distance_appelli = ConstraintList()  # Per ogni esame la distanza minima tra i due appelli deve essere almeno MIN_DISTANCE_APPELLI
    for esame in model.exams:
        for giorno_1 in model.days:
            for giorno_2 in model.days:
                if giorno_1 != giorno_2 and abs(giorno_1 - giorno_2) >= exams[esame].numero_giorni_durata:
                    model.min_distance_appelli.add(
                        (abs(giorno_1 - giorno_2) - 1) * (model.x[esame,giorno_1] * model.x[esame,giorno_2]) +
                        (days * (1 - (model.x[esame,giorno_1] * model.x[esame,giorno_2]))) >= MIN_DISTANCE_APPELLI)

    model.assegniamenti_contigui = ConstraintList()  #Per ogni esame assegno i giorni contigui necessari
    for esame in model.exams:
        if(exams[esame].numero_giorni_durata>1):
            for giorno in range(1,days-exams[esame].numero_giorni_durata):
                model.assegniamenti_contigui.add(
                    ((1-model.x[esame,giorno-1]) * model.x[esame,giorno] * exams[esame].numero_giorni_durata) <=
                    sum(model.x[esame,giorno_2] for giorno_2 in range(giorno,giorno+exams[esame].numero_giorni_durata))
                )

    model.limiti_aule = ConstraintList()  # Per ogni giorno non superiamo i limiti di assegniamento delle aule
    for giorno in model.days:
        for aula in model.aule:
            found=False
            for exam in exams:
                if(aula in exam.aule_richieste):
                    found=True
            if found:
                model.limiti_aule.add((
                    sum(model.x[esame, giorno] * model.richieste_aule_esami[esame][aula]
                        for esame in model.exams) <=
                    model.aule_disponibilita[aula][giorno]
                ))

    model.limiti_lab = ConstraintList()  # Per ogni giorno non superiamo i limiti di assegniamento delle aule
    for giorno in model.days:
        for lab in model.lab:
            found = False
            for exam in exams:
                if (lab in exam.laboratori_richiesti):
                    found = True
            if found:
                model.limiti_lab.add((
                        sum(model.x[esame, giorno] * model.richieste_lab_esami[esame][lab]
                            for esame in model.exams) <=
                        model.lab_disponibilita[lab][giorno]
                ))

    return model

def build_richieste_lab_esami(exams,laboratori):
    richieste_lab_esami = list()  # Lista di laboratori richiesti dagli esami, per ogni esame assegna un array di dimensione aule elementi settati a 0
    for exam_index in range(len(exams)):
        richieste_lab_esami.append(list())
        for lab_index in range(len(laboratori)):
            richieste_lab_esami[exam_index].append(0)
        # Ora attivo i lab richiesti
        for lab in exams[exam_index].laboratori_richiesti:
            richieste_lab_esami[exam_index][lab] = exams[exam_index].numero_lab_slot
    return richieste_lab_esami

def build_richieste_aule_esami(exams,aule):
    richieste_aule_esami = list()  # Lista di aule richieste dagli esami, per ogni esame assegna un array di dimensione aule elementi settati a 0
    for exam_index in range(len(exams)):
        richieste_aule_esami.append(list())
        for aula_index in range(len(aule)):
            richieste_aule_esami[exam_index].append(0)
        # Ora attivo le aule richieste
        for aula in exams[exam_index].aule_richieste:
            richieste_aule_esami[exam_index][aula] = exams[exam_index].numero_aule_slot
    return richieste_aule_esami

def build_lab_disponibilita(laboratori,days,data_inizio):
    lab_disponibilita = list()  # Lista di giorni di disponibilità dei laboratori, per ogni laboratorio assegna un array di dimensione days elementi settati a 1
    for lab_index in range(len(laboratori)):
        lab_disponibilita.append(list())
        for giorno in range(days):
            lab_disponibilita[lab_index].append(SLOT_LABORATORI)
        # Ora metto a 0 i giorni di indisponibilita
        for data_indisponibilita in laboratori[lab_index].indisponibilita:
            distance = (data_indisponibilita - data_inizio).days
            lab_disponibilita[lab_index][distance] = 0
    return lab_disponibilita

def build_aule_disponibilita(aule,days,data_inizio):
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


def print_results(model, exams, data_inizio, data_fine):
    days = (data_fine - data_inizio).days + 1
    for i in range(len(exams)):
        print(exams[i].nome)
        for j in range(days):
            print("[", end="")
            if (int(model.x[i, j].value) == 1):
                print('\033[92m' + str(int(model.x[i, j].value)) + '\033[0m', end="]")
            else:
                print(int(model.x[i, j].value), end="]")

        print("]")


if __name__ == '__main__':
    main()
