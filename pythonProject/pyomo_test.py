from ExamClass import Exam
from datetime import datetime

def main():
    aule=["Aula A",
        "Aula B",
        "Aula C",
        "Aula D",
        "Aula E",
        "Aula F",
        "Sala conferenze"]
    laboratori=["Laboratorio Dijkstra",
                "Laboratorio Vonneumann",
                "Laboratorio Turing",
                "Laboratorio Babbage",
                "Laboratorio Postel"]

    data_inizio =datetime.strptime("08/06/2023", '%d/%m/%y')
    data_fine =datetime.strptime("28/07/2023", '%d/%m/%y')

    exams=list()
    exams.append(Exam("CMRO","Scritto","Insegnante1, Insegnante 2",[1],1,2,1,[],0,[0,2],1,1,[],[],"Note"))
    exams.append(Exam("MDL","Scritto","Insegnante1, Insegnante 2",[1],1,2,1,[0,1,2,3],1,[],0,1,[],[],"Note"))









if __name__ == '__main__':
    main()