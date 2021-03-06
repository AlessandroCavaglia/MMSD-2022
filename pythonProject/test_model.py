from classes import Exam
from classes import ExamRoom
from datetime import datetime
from model_building import *
import pyomo.environ as pyo


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

    data_inizio = datetime.strptime("09/06/2023", '%d/%m/%Y')
    data_fine = datetime.strptime("23/06/2023", '%d/%m/%Y')

    exams = list()
    exams.append(
        Exam("CMRO", "Scritto", "Insegnante1, Insegnante 2", [1], 1, 2, 1, [], 0, [0, 1], 3, 2, [], [], "Note"))
    exams.append(
        Exam("CMRO2", "Scritto", "Insegnante1, Insegnante 2", [1], 2, 2, 1, [], 0, [0, 1], 1, 2, [], [], "Note"))

    model = build_model(aule, laboratori, data_inizio, data_fine, exams)
    opt = pyo.SolverFactory('cplex')
    opt.solve(model)
    print_results(model, exams, data_inizio, data_fine)





if __name__ == '__main__':
    main()
