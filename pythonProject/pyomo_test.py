from Classes import Exam
from Classes import ExamRoom
from datetime import datetime
from pyomo.environ import *
import pyomo.environ as pyo

MIN_DISTANCE_APPELLI = 10


def main():
    aule = [ExamRoom("Aula A", []),
            ExamRoom("Aula B", []),
            ExamRoom("Aula C", []),
            ExamRoom("Aula D", []),
            ExamRoom("Aula E", []),
            ExamRoom("Aula F", []),
            ExamRoom("Sala conferenze", [])]
    laboratori = [ExamRoom("Laboratorio Dijkstra", []),
                  ExamRoom("Laboratorio Vonneumann", []),
                  ExamRoom("Laboratorio Turing", []),
                  ExamRoom("Laboratorio Babbage", []),
                  ExamRoom("Laboratorio Postel", [])]

    data_inizio = datetime.strptime("08/06/2023", '%d/%m/%Y')
    data_fine = datetime.strptime("28/07/2023", '%d/%m/%Y')

    exams = list()
    exams.append(
        Exam("CMRO", "Scritto", "Insegnante1, Insegnante 2", [1], 1, 2, 1, [], 0, [0, 2], 1, 2, [], [], "Note"))
    exams.append(
        Exam("MDL", "Scritto", "Insegnante1, Insegnante 2", [1], 1, 2, 1, [0, 1, 2, 3], 1, [], 0, 1, [], [], "Note"))

    model = build_model(aule, laboratori, data_inizio, data_fine, exams)
    opt = pyo.SolverFactory('cplex')
    opt.solve(model)
    print_results(model, exams, data_inizio, data_fine)


def build_model(aule, laboratori, data_inizio, data_fine, exams):
    days = (
                       data_fine - data_inizio).days + 1  # Calculate the number of days of the range counting for also the first and last day

    model = ConcreteModel()
    model.days = range(days)
    model.exams = range(len(exams))

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



    return model


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
