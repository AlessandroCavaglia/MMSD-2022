from datetime import timedelta

import costants
from mpcal import MplCalendar
import mpcal
import PySimpleGUI as sg

print = sg.Print  # TODO modificare in base a che output vogliamo




def build_calendar(exams, model, sessioni,output):
    data_inizio=sessioni[0][0]
    data_fine=sessioni[0][1]
    esami_primo_anno = []
    esami_secondo_anno = []
    esami_terzo_anno = []
    for esame in exams:
        # print(esame.nome,esame.short_name)
        if (esame.anno == 1):
            esami_primo_anno.append(esame)
        if (esame.anno == 2):
            esami_secondo_anno.append(esame)
        if (esame.anno == 3):
            esami_terzo_anno.append(esame)
    if(data_inizio.month==data_fine.month):
        create_calendar(exams,exams,model,data_inizio.year,data_inizio.month,data_inizio,"Calendario Generale.jpg", abs(data_fine - data_inizio),output)
        create_calendar(esami_primo_anno,exams,model,data_inizio.year,data_inizio.month,data_inizio,"Calendario Primo Anno.jpg", abs(data_fine - data_inizio),output)
        create_calendar(esami_secondo_anno,exams,model,data_inizio.year,data_inizio.month,data_inizio,"Calendario Secondo Anno.jpg", abs(data_fine - data_inizio),output)
        create_calendar(esami_terzo_anno,exams,model,data_inizio.year,data_inizio.month,data_inizio,"Calendario Terzo Anno.jpg", abs(data_fine - data_inizio),output)
    else:
        create_calendar(exams,exams,model,data_inizio.year,data_inizio.month,data_inizio,"Calendario Generale "+mpcal.m_names[data_inizio.month-1]+".jpg", abs(data_fine - data_inizio),output)
        create_calendar(exams,exams,model,data_fine.year,data_fine.month,data_inizio,"Calendario Generale "+mpcal.m_names[data_fine.month-1]+".jpg", abs(data_fine - data_inizio),output)

        create_calendar(esami_primo_anno, exams, model, data_inizio.year, data_inizio.month, data_inizio, "Calendario Primo Anno "+mpcal.m_names[data_inizio.month-1]+".jpg", abs(data_fine - data_inizio), output)
        create_calendar(esami_primo_anno, exams, model, data_fine.year, data_fine.month, data_inizio, "Calendario Primo Anno "+mpcal.m_names[data_fine.month-1]+".jpg", abs(data_fine - data_inizio), output)

        create_calendar(esami_secondo_anno, exams, model, data_inizio.year, data_inizio.month, data_inizio, "Calendario Secondo Anno "+mpcal.m_names[data_inizio.month-1]+".jpg", abs(data_fine - data_inizio), output)
        create_calendar(esami_secondo_anno, exams, model, data_fine.year, data_fine.month, data_inizio, "Calendario Secondo Anno "+mpcal.m_names[data_fine.month-1]+".jpg",abs(data_fine - data_inizio), output)

        create_calendar(esami_terzo_anno, exams, model, data_inizio.year, data_inizio.month, data_inizio, "Calendario Terzo Anno "+mpcal.m_names[data_inizio.month-1]+".jpg", abs(data_fine - data_inizio), output)
        create_calendar(esami_terzo_anno, exams, model, data_fine.year, data_fine.month, data_inizio, "Calendario Terzo Anno "+mpcal.m_names[data_fine.month-1]+".jpg", abs(data_fine - data_inizio), output)


    return


def create_calendar(esami,exams,model,anno_sessione,mese_sessione,data_inizio_sessione,nome_calendario,durata_sessione,output):
    cal = MplCalendar(anno_sessione, mese_sessione)
    for esame in esami:
        index = exams.index(esame)
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio_sessione + timedelta(days=i)
                if data.month == mese_sessione:
                    cal.add_event(data.day,esame.short_name,pick_color_for_exam(esame))


    cal.show(nome_calendario,output)
    return


def pick_color_for_exam(exam):
    if exam.anno==1 and exam.lista_semestri[0]=='1':
        return costants.ANNI_SEMESTRI_COLORI[0]
    if exam.anno==1 and exam.lista_semestri[0]=='2':
        return costants.ANNI_SEMESTRI_COLORI[1]
    if exam.anno==2 and exam.lista_semestri[0]=='1':
        return costants.ANNI_SEMESTRI_COLORI[2]
    if exam.anno==2 and exam.lista_semestri[0]=='2':
        return costants.ANNI_SEMESTRI_COLORI[3]
    if exam.anno==3 and exam.lista_semestri[0]=='1':
        return costants.ANNI_SEMESTRI_COLORI[4]
    if exam.anno==3 and exam.lista_semestri[0]=='2':
        return costants.ANNI_SEMESTRI_COLORI[5]

    return 'white'