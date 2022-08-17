import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import classes
import xlsxwriter
import costants
import holidays
import calendar
import PySimpleGUI as sg

print = sg.Print  # TODO modificare in base a che output vogliamo

def extract_exams_names(exams):
    data = []
    for esame in exams:
        data.append(esame.nome)
    return data

def extract_exams_type(exams):
    data = []
    for esame in exams:
        data.append(esame.tipo)
    return data

def extract_exams_teachers(exams):
    data = []
    for esame in exams:
        data.append(esame.insegnanti)
    return data

def extract_exams_semestre(exams):
    data = []
    for esame in exams:
        semestri = str(esame.lista_semestri)
        semestri = semestri.replace("[", "")
        semestri = semestri.replace("]", "")
        semestri = semestri.replace("'", "")
        data.append(semestri)
    return data

def extract_appelli(exams,model,sessione):
    appello_1 = []
    appello_2 = []
    for esame in exams:
        index = exams.index(esame)
        date_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value > 0.5:
                data = sessione[0][0] + timedelta(days=i)
                date_esame.append(str(data))
        print(str(len(date_esame))+" "+str(esame.numero_giorni_durata)+" "+esame.nome)
        data_esame_1=""
        for i in range(esame.numero_giorni_durata):
            data_esame_1 +=" "+ date_esame[i]

        data_esame_1 = data_esame_1.replace("[", "")
        data_esame_1 = data_esame_1.replace("]", "")
        data_esame_1 = data_esame_1.replace("'", "")
        data_esame_1 = data_esame_1.replace("00:00:00", "")
        appello_1.append(data_esame_1)
        if(len(date_esame)>esame.numero_giorni_durata):
            for i in range(esame.numero_giorni_durata):
                data_esame_2=""
                if (esame.numero_giorni_durata + i >= len(date_esame)):
                    print("POSSIBILE ERRORE IN ASSEGNAMENTO DATE")
                    data_esame_2 += " "
                else:
                    data_esame_2 +=" "+ date_esame[esame.numero_giorni_durata + i]
            data_esame_2 = data_esame_2.replace("[", "")
            data_esame_2 = data_esame_2.replace("]", "")
            data_esame_2 = data_esame_2.replace("'", "")
            data_esame_2 = data_esame_2.replace("00:00:00", "")
            appello_2.append(data_esame_2)
        else:
            appello_2.append('')
    return (appello_1,appello_2)



def build_exams_output(esami_anno, nome_foglio, laboratori, aule, model, writer, exams, sessione):
    esami_df = pd.DataFrame({})

    esami_df.insert(0, "Nome corso",  extract_exams_names(esami_anno), True)


    esami_df.insert(1, "Tipologia", extract_exams_type(esami_anno), True)


    esami_df.insert(2, "Docenti", extract_exams_teachers(esami_anno), True)


    esami_df.insert(3, "Semestre", extract_exams_semestre(esami_anno), True)


    (primi_appelli,secondi_appelli)=extract_appelli(esami_anno,model,sessione)


    esami_df.insert(4, "Primo appello", primi_appelli, True)
    esami_df.insert(5, "Secondo appello", secondi_appelli, True)
    esami_df.to_excel(writer, sheet_name=nome_foglio, index=False)

    # set formatting
    workbook = writer.book
    worksheet = writer.sheets[nome_foglio]
    worksheet.set_zoom(90)
    worksheet.set_column("A:A", 150)
    worksheet.set_column("B:C", 50)
    worksheet.set_column("D:D", 15, workbook.add_format({"align": "center"}))
    worksheet.set_column("E:F", 50)
    worksheet.set_row(1, 12)

    header_format = workbook.add_format({
        "bg_color": "#ededed",
        "align": "center",
        "valign": "vcenter",
        "bold": True,
        "font_size": 12
    })


    for col_num, value in enumerate(esami_df.columns.values):  # setting header formatting only for the first row
           worksheet.write(0, col_num, value, header_format)


def extract_short_names_riassunto(esami):
    prev = '1'
    nomi_esami=[]
    primo_semestre = 1
    secondo_semestre = 1
    nomi_esami.append("")
    for esame in esami:
        if (esame.lista_semestri[0] != prev):
            nomi_esami.append("")
            prev = '2'
        if esame.lista_semestri[0] == '1':
            primo_semestre += 1
        else:
            secondo_semestre += 1
        nomi_esami.append(esame.short_name)
    return (nomi_esami,primo_semestre,secondo_semestre)

def extract_date_appelli_riassunto(esami,label_primo_semestre,label_secondo_semestre,exams,sessione,model):
    appelli_1=[]
    appelli_2=[]
    prev = '1'
    appelli_1.append(label_primo_semestre)
    appelli_2.append("")
    for esame in esami:
        if (esame.lista_semestri[0] != prev):
            appelli_1.append(label_secondo_semestre)
            appelli_2.append("")
            prev = '2'
        index = exams.index(esame)
        date_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value > 0.5:
                data = sessione[0][0] + timedelta(days=i)
                date_esame.append(str(data))
        data_1 = ""
        for i in range(esame.numero_giorni_durata):
            data_1 += " " + date_esame[i]
        data_1 = data_1.replace("[", "")
        data_1 = data_1.replace("]", "")
        data_1 = data_1.replace("'", "")
        data_1 = data_1.replace("00:00:00", "")
        appelli_1.append(data_1)
        if (len(date_esame) > esame.numero_giorni_durata):
            date_2 = ""
            for i in range(esame.numero_giorni_durata):
                if(esame.numero_giorni_durata + i>=len(date_esame)):
                    print("POSSIBILE ERRORE IN ASSEGNAMENTO DATE")
                    date_2 += " "
                else:
                    date_2 += " " + date_esame[esame.numero_giorni_durata + i]
            date_2 = date_2.replace("[", "")
            date_2 = date_2.replace("]", "")
            date_2 = date_2.replace("'", "")
            date_2 = date_2.replace("00:00:00", "")
            appelli_2.append(date_2)
        else:
            appelli_2.append('')
    return (appelli_1,appelli_2)

def fix_aula_lab(exams_request):
    exams_request = exams_request[0:-1]
    exams_request = exams_request.replace("Laboratorio", "Lab.")
    exams_request = exams_request.replace("laboratorio", "lab.")
    exams_request = exams_request.replace("Dijkstra", "Dij.")
    exams_request = exams_request.replace("dijkstra", "dij.")
    exams_request = exams_request.replace("Turing", "Tur.")
    exams_request = exams_request.replace("turing", "tur.")
    exams_request = exams_request.replace("Vonneumann", "Von.")
    exams_request = exams_request.replace("vonneumann", "von.")
    exams_request = exams_request.replace("Babbage", "Bab.")
    exams_request = exams_request.replace("Babbage", "bab.")
    exams_request = exams_request.replace("postel", "pos.")
    exams_request = exams_request.replace("Postel", "Pos.")
    exams_request = exams_request.replace("Conferenze", "Conf.")
    exams_request = exams_request.replace("conferenze", "conf.")
    return exams_request

def extract_aule_lab_riassunto(esami,aule,laboratori,exams):
    aule_lab=[]
    prev = '1'
    aule_lab.append("")
    for esame in esami:
        if (esame.lista_semestri[0] != prev):
            aule_lab.append("")
            prev = '2'
        exams_request = ""
        for aula_richiesta in esame.aule_richieste:
            exams_request += " " + aule[aula_richiesta].nome + ","
        for lab_richiesto in esame.laboratori_richiesti:
            exams_request += " " + laboratori[lab_richiesto].nome + ","
        exams_request=fix_aula_lab(exams_request)
        aule_lab.append(exams_request)

    return aule_lab


def build_exams_output_riassunto(esami_primo_anno,esami_secondo_anno,esami_terzo_anno, nome_foglio, laboratori, aule, model, writer, exams, sessione):
    esami_df = pd.DataFrame({})
    nomi_esami = []
    appelli_1 = []
    appelli_2 = []
    aule_lab=[]

    esami_primo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    esami_secondo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    esami_terzo_anno.sort(key=lambda esame:esame.lista_semestri[0])

    #Esami del primo anno
    (nomi_primo_anno,esami_primo_anno_primo_semestre,esami_primo_anno_secondo_semestre)=extract_short_names_riassunto(esami_primo_anno)
    nomi_esami=nomi_esami+nomi_primo_anno
    (appelli_primo_anno_1,appelli_primo_anno_2)=extract_date_appelli_riassunto(esami_primo_anno,"Esami primo anno primo semestre","Esami primo anno secondo semestre",exams,sessione,model)
    appelli_1=appelli_1+appelli_primo_anno_1
    appelli_2=appelli_2+appelli_primo_anno_2
    aule_lab_primo_anno=extract_aule_lab_riassunto(esami_primo_anno,aule,laboratori,exams)
    aule_lab=aule_lab+aule_lab_primo_anno

    # Esami del secondo anno
    (nomi_secondo_anno, esami_secondo_anno_primo_semestre,
     esami_secondo_anno_secondo_semestre) = extract_short_names_riassunto(esami_secondo_anno)
    nomi_esami = nomi_esami + nomi_secondo_anno
    (appelli_secondo_anno_1, appelli_secondo_anno_2) = extract_date_appelli_riassunto(esami_secondo_anno,"Esami secondo anno primo semestre","Esami secondo anno secondo semestre",exams, sessione, model)
    appelli_1 = appelli_1 + appelli_secondo_anno_1
    appelli_2 = appelli_2 + appelli_secondo_anno_2
    aule_lab_secondo_anno = extract_aule_lab_riassunto(esami_secondo_anno, aule, laboratori, exams)
    aule_lab = aule_lab + aule_lab_secondo_anno

    # Esami del terzo anno
    (nomi_terzo_anno, esami_terzo_anno_primo_semestre,esami_terzo_anno_secondo_semestre) = extract_short_names_riassunto(esami_terzo_anno)
    nomi_esami = nomi_esami + nomi_terzo_anno
    (appelli_terzo_anno_1, appelli_terzo_anno_2) = extract_date_appelli_riassunto(esami_terzo_anno,"Esami terzo anno primo semestre","Esami terzo anno secondo semestre",exams, sessione, model)
    appelli_1 = appelli_1 + appelli_terzo_anno_1
    appelli_2 = appelli_2 + appelli_terzo_anno_2
    aule_lab_terzo_anno = extract_aule_lab_riassunto(esami_terzo_anno, aule, laboratori, exams)
    aule_lab = aule_lab + aule_lab_terzo_anno



    esami_df.insert(0, "Primo appello", appelli_1, True)
    esami_df.insert(1, "Secondo appello", appelli_2, True)
    esami_df.insert(2, "Aule e laboratori richiesti", aule_lab, True)
    esami_df.insert(3, "Nome corto del corso ", nomi_esami, True)


    esami_df.to_excel(writer, sheet_name=nome_foglio, index=False)

    # FORMATTING
    workbook = writer.book
    worksheet = writer.sheets[nome_foglio]
    worksheet.set_zoom(140)
    worksheet.set_column("A:A", 40)
    worksheet.set_column("B:B", 40)
    worksheet.set_column("C:C", 50)
    worksheet.set_column("D:D", 200)



    header_format = workbook.add_format({
        "bg_color": "#ededed",
        "align": "center",
        "valign": "vcenter",
        "bold": True,
        "font_size": 12
    })
    format_primo_anno_primo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[0],
    })
    format_primo_anno_secondo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[1],
    })
    format_secondo_anno_primo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[2],
    })
    format_secondo_anno_secondo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[3],
    })
    format_terzo_anno_primo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[4],
    })
    format_terzo_anno_secondo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[5],
    })



    for col_num, value in enumerate(esami_df.columns.values):  # setting header formatting only for the first row
            worksheet.write(0, col_num, value, header_format)

    for row_num, val in esami_df.iterrows():
        #print(val.values)
        for col_num in range(0,4):
            if row_num >= 0 and row_num <= esami_primo_anno_primo_semestre+1:
                worksheet.write(row_num + 1, col_num, val.values[col_num], format_primo_anno_primo_semestre)
            if row_num >= esami_primo_anno_primo_semestre and row_num <= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre):
                worksheet.write(row_num + 1, col_num, val.values[col_num], format_primo_anno_secondo_semestre)
            if row_num >= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre) and row_num <= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre+esami_secondo_anno_primo_semestre):
                worksheet.write(row_num + 1, col_num, val.values[col_num], format_secondo_anno_primo_semestre)
            if row_num >= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre+esami_secondo_anno_primo_semestre) and row_num <= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre+esami_secondo_anno_primo_semestre+esami_secondo_anno_secondo_semestre):
                worksheet.write(row_num + 1, col_num, val.values[col_num], format_secondo_anno_secondo_semestre)
            if row_num >= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre+esami_secondo_anno_primo_semestre+esami_secondo_anno_secondo_semestre) and row_num <= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre+esami_secondo_anno_primo_semestre+esami_secondo_anno_secondo_semestre+esami_terzo_anno_primo_semestre):
                worksheet.write(row_num + 1, col_num, val.values[col_num], format_terzo_anno_primo_semestre)
            if row_num >= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre+esami_secondo_anno_primo_semestre+esami_secondo_anno_secondo_semestre+esami_terzo_anno_primo_semestre) and row_num <= (esami_primo_anno_primo_semestre + esami_primo_anno_secondo_semestre+esami_secondo_anno_primo_semestre+esami_secondo_anno_secondo_semestre+esami_terzo_anno_primo_semestre+esami_terzo_anno_secondo_semestre):
                worksheet.write(row_num + 1, col_num, val.values[col_num], format_terzo_anno_secondo_semestre)

def build_exams_output_riassunto_2(esami_primo_anno,esami_secondo_anno,esami_terzo_anno, nome_foglio, laboratori, aule, model, writer, exams, sessione):
    esami_df = pd.DataFrame({})
    nomi_esami = []
    appelli_1 = []
    appelli_2 = []
    aule_lab = []

    esami_primo_anno.sort(key=lambda esame: esame.lista_semestri[0])
    esami_secondo_anno.sort(key=lambda esame: esame.lista_semestri[0])
    esami_terzo_anno.sort(key=lambda esame: esame.lista_semestri[0])

    # Esami del primo anno
    (nomi_primo_anno, esami_primo_anno_primo_semestre,
     esami_primo_anno_secondo_semestre) = extract_short_names_riassunto(esami_primo_anno)
    nomi_esami = nomi_esami + nomi_primo_anno
    (appelli_primo_anno_1, appelli_primo_anno_2) = extract_date_appelli_riassunto(esami_primo_anno,
                                                                                  "Esami primo anno primo semestre",
                                                                                  "Esami primo anno secondo semestre",
                                                                                  exams, sessione, model)
    appelli_1 = appelli_1 + appelli_primo_anno_1
    appelli_2 = appelli_2 + appelli_primo_anno_2
    aule_lab_primo_anno = extract_aule_lab_riassunto(esami_primo_anno, aule, laboratori, exams)
    aule_lab = aule_lab + aule_lab_primo_anno

    # Esami del secondo anno
    (nomi_secondo_anno, esami_secondo_anno_primo_semestre,
     esami_secondo_anno_secondo_semestre) = extract_short_names_riassunto(esami_secondo_anno)
    nomi_esami = nomi_esami + nomi_secondo_anno
    (appelli_secondo_anno_1, appelli_secondo_anno_2) = extract_date_appelli_riassunto(esami_secondo_anno,
                                                                                      "Esami secondo anno primo semestre",
                                                                                      "Esami secondo anno secondo semestre",
                                                                                      exams, sessione, model)
    appelli_1 = appelli_1 + appelli_secondo_anno_1
    appelli_2 = appelli_2 + appelli_secondo_anno_2
    aule_lab_secondo_anno = extract_aule_lab_riassunto(esami_secondo_anno, aule, laboratori, exams)
    aule_lab = aule_lab + aule_lab_secondo_anno

    # Esami del terzo anno
    (nomi_terzo_anno, esami_terzo_anno_primo_semestre,
     esami_terzo_anno_secondo_semestre) = extract_short_names_riassunto(esami_terzo_anno)
    nomi_esami = nomi_esami + nomi_terzo_anno
    (appelli_terzo_anno_1, appelli_terzo_anno_2) = extract_date_appelli_riassunto(esami_terzo_anno,
                                                                                  "Esami terzo anno primo semestre",
                                                                                  "Esami terzo anno secondo semestre",
                                                                                  exams, sessione, model)
    appelli_1 = appelli_1 + appelli_terzo_anno_1
    appelli_2 = appelli_2 + appelli_terzo_anno_2
    aule_lab_terzo_anno = extract_aule_lab_riassunto(esami_terzo_anno, aule, laboratori, exams)
    aule_lab = aule_lab + aule_lab_terzo_anno

    esami_df.insert(0, "Primo appello", appelli_1, True)
    esami_df.insert(1, "Secondo appello", appelli_2, True)
    esami_df.insert(2, "Aule e laboratori richiesti", aule_lab, True)
    esami_df.insert(3, "Nome corto del corso ", nomi_esami, True)

    sorted_df = esami_df.sort_values(by="Primo appello")
    # print(sorted_df)

    sorted_df.to_excel(writer, sheet_name=nome_foglio, index=False)

    # FORMATTING
    workbook = writer.book
    worksheet = writer.sheets[nome_foglio]
    worksheet.set_zoom(140)
    worksheet.set_column("A:A", 40)
    worksheet.set_column("B:B", 40)
    worksheet.set_column("C:C", 50)
    worksheet.set_column("D:D", 200)

    header_format = workbook.add_format({
        "bg_color": "#ededed",
        "align": "center",
        "valign": "vcenter",
        "bold": True,
        "font_size": 12
    })
    format_primo_anno_primo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[0],
    })
    format_primo_anno_secondo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[1],
    })
    format_secondo_anno_primo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[2],
    })
    format_secondo_anno_secondo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[3],
    })
    format_terzo_anno_primo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[4],
    })
    format_terzo_anno_secondo_semestre = workbook.add_format({
        "bg_color": costants.ANNI_SEMESTRI_COLORI[5],
    })
    blank = workbook.add_format({
        "bg_color": '#ffffff'
    })



    for col_num, value in enumerate(sorted_df.columns.values):  # setting header formatting only for the first row
            worksheet.write(0, col_num, value, header_format)


    row_num = 1
    for indice, val in sorted_df.sort_values(by="Primo appello").iterrows():
        for col_num in range(0,4):
            if findExam(esami_primo_anno,val.values[3],"1"):
                worksheet.write(row_num , col_num, val.values[col_num], format_primo_anno_primo_semestre)
            if findExam(esami_primo_anno, val.values[3], "2"):
                worksheet.write(row_num , col_num, val.values[col_num], format_primo_anno_secondo_semestre)
            if findExam(esami_secondo_anno, val.values[3], "1"):
                worksheet.write(row_num , col_num, val.values[col_num], format_secondo_anno_primo_semestre)
            if findExam(esami_secondo_anno, val.values[3], "2"):
                worksheet.write(row_num , col_num, val.values[col_num], format_secondo_anno_secondo_semestre)
            if findExam(esami_terzo_anno, val.values[3], "1"):
                worksheet.write(row_num , col_num, val.values[col_num], format_terzo_anno_primo_semestre)
            if findExam(esami_terzo_anno, val.values[3], "2"):
                worksheet.write(row_num , col_num, val.values[col_num], format_terzo_anno_secondo_semestre)

        if val.values[0] == "Esami primo anno primo semestre":
            worksheet.write(row_num, 0, ' ',blank)
            worksheet.write(row_num + 1, 0, val.values[0], format_primo_anno_primo_semestre)
        if val.values[0] == "Esami primo anno secondo semestre":
            worksheet.write(row_num+ 1, 0, val.values[0], format_primo_anno_secondo_semestre)
        if val.values[0] == "Esami secondo anno primo semestre":
            worksheet.write(row_num+ 1, 0, val.values[0], format_secondo_anno_primo_semestre)
        if val.values[0] == "Esami secondo anno secondo semestre":
            worksheet.write(row_num+ 1, 0, val.values[0], format_secondo_anno_secondo_semestre)
        if val.values[0] == "Esami terzo anno primo semestre":
            worksheet.write(row_num + 1, 0, val.values[0], format_terzo_anno_primo_semestre)
        if val.values[0] == "Esami terzo anno secondo semestre":
            worksheet.write(row_num + 1, 0, val.values[0], format_terzo_anno_secondo_semestre)
        row_num += 1

def get_esami_semestri(exams):
    esami_primo_anno_primo_semestre = []
    esami_primo_anno_secondo_semestre = []
    esami_secondo_anno_primo_semestre = []
    esami_secondo_anno_secondo_semestre = []
    esami_terzo_anno_primo_semestre = []
    esami_terzo_anno_secondo_semestre = []
    for esame in exams:
        if (esame.anno == 1):
            if '1' == esame.lista_semestri[0]:
                esami_primo_anno_primo_semestre.append(esame)
            else:
                esami_primo_anno_secondo_semestre.append(esame)
        if (esame.anno == 2):
            if '1' == esame.lista_semestri[0]:
                esami_secondo_anno_primo_semestre.append(esame)
            else:
                esami_secondo_anno_secondo_semestre.append(esame)
        if (esame.anno == 3):
            if '1' == esame.lista_semestri[0]:
                esami_terzo_anno_primo_semestre.append(esame)
            else:
                esami_terzo_anno_secondo_semestre.append(esame)
    return(esami_primo_anno_primo_semestre,esami_primo_anno_secondo_semestre,esami_secondo_anno_primo_semestre,esami_secondo_anno_secondo_semestre,esami_terzo_anno_primo_semestre,esami_terzo_anno_secondo_semestre)

def get_date_esami(esame,model,durata_sessione,data_inizio,exams):
    date=[]
    for esame in esame:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value > 0.5:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date.append(date_esame)
    return date

def calculate_distanze(date,esami):
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami):
        for index2, esame2 in enumerate(esami):
            if (esame1 != esame2):
                distanza_media += abs((date[index1][0] - date[index2][0]).days)
                if (abs((date[index1][0] - date[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date[index1][0] - date[index2][0]).days)
                if (abs((date[index1][0] - date[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date[index1][0] - date[index2][0]).days)
                distanza_media += abs((date[index1][1] - date[index2][1]).days)
                if (abs((date[index1][1] - date[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date[index1][1] - date[index2][1]).days)
                if (abs((date[index1][1] - date[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date[index1][1] - date[index2][1]).days)
                entries += 2
    distanza_media = distanza_media / entries
    return (round(distanza_media,2),round(distanza_minima,2),round(distanza_massima,2))


def build_statistiche(esami_primo_anno,esami_secondo_anno,esami_terzo_anno, nome_foglio, laboratori, aule, model, writer, exams, sessione):
    nome_stat=['Primo Anno','Primo Anno Primo Semestre','Primo Anno Secondo Semestre','Secondo Anno','Secondo Anno Primo Semestre','Secondo Anno Secondo Semestre','Terzo Anno','Terzo Anno Primo Semestre','Terzo Anno Secondo Semestre']

    distanza_media = []
    distanza_minima=[]
    distanza_massima=[]


    (esami_primo_anno_primo_semestre, esami_primo_anno_secondo_semestre, esami_secondo_anno_primo_semestre,
     esami_secondo_anno_secondo_semestre, esami_terzo_anno_primo_semestre, esami_terzo_anno_secondo_semestre)=get_esami_semestri(exams)

    durata_sessione = abs(sessione[0][1] - sessione[0][0])

    date_esami_primo_anno=get_date_esami(esami_primo_anno,model,durata_sessione,sessione[0][0],exams)
    date_esami_primo_anno_primo_semestre=get_date_esami(esami_primo_anno_primo_semestre,model,durata_sessione,sessione[0][0],exams)
    date_esami_primo_anno_secondo_semestre=get_date_esami(esami_primo_anno_secondo_semestre,model,durata_sessione,sessione[0][0],exams)

    date_esami_secondo_anno = get_date_esami(esami_secondo_anno, model, durata_sessione, sessione[0][0],exams)
    date_esami_secondo_anno_primo_semestre = get_date_esami(esami_secondo_anno_primo_semestre, model, durata_sessione,sessione[0][0],exams)
    date_esami_secondo_anno_secondo_semestre = get_date_esami(esami_secondo_anno_secondo_semestre, model, durata_sessione,sessione[0][0],exams)

    date_esami_terzo_anno = get_date_esami(esami_terzo_anno, model, durata_sessione, sessione[0][0],exams)
    date_esami_terzo_anno_primo_semestre = get_date_esami(esami_terzo_anno_primo_semestre, model, durata_sessione,sessione[0][0],exams)
    date_esami_terzo_anno_secondo_semestre = get_date_esami(esami_terzo_anno_secondo_semestre, model, durata_sessione,sessione[0][0],exams)

    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_primo_anno,esami_primo_anno)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)
    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_primo_anno_primo_semestre,esami_primo_anno_primo_semestre)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)
    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_primo_anno_secondo_semestre, esami_primo_anno_secondo_semestre)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)

    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_secondo_anno,esami_secondo_anno)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)
    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_secondo_anno_primo_semestre, esami_secondo_anno_primo_semestre)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)
    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_secondo_anno_secondo_semestre, esami_secondo_anno_secondo_semestre)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)

    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_terzo_anno,esami_terzo_anno)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)
    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_terzo_anno_primo_semestre, esami_terzo_anno_primo_semestre)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)
    (distanza_media_val, distanza_minima_val, distanza_massima_val) = calculate_distanze(date_esami_terzo_anno_secondo_semestre, esami_terzo_anno_secondo_semestre)
    distanza_minima.append(distanza_minima_val)
    distanza_massima.append(distanza_massima_val)
    distanza_media.append(distanza_media_val)

    statistiche_df = pd.DataFrame({})
    statistiche_df.insert(0, "Periodo", nome_stat, True)
    statistiche_df.insert(1, "Distanza media", distanza_media, True)
    statistiche_df.insert(2, "Distanza minima", distanza_minima, True)
    statistiche_df.insert(3, "Distanza massima ", distanza_massima, True)

    statistiche_df.to_excel(writer, sheet_name="Statistiche", index=False)
    workbook = writer.book
    worksheet = writer.sheets['Statistiche']
    worksheet.set_zoom(150)
    worksheet.set_column("A:A", 30)
    worksheet.set_column("B:D", 20)


def findExam(df,exam,sem):
    for esame in df:
        if (esame.nome == exam or esame.short_name == exam) and sem == esame.lista_semestri[0]:
            return True

def build_output(input,output,exams, laboratori, aule, model, sessioni):
    # Move the general input page to the new document

    if(output != '' and input != ''):
        sessioni_df = pd.read_excel(input, sheet_name='Input generali')
        #print(output + '/' + costants.OUTPUT_FILE_NAME)
        writer = pd.ExcelWriter(output + '/' + costants.OUTPUT_FILE_NAME, engine='xlsxwriter')
    else:
        sessioni_df = pd.read_excel('input/' + costants.INPUT_FILE_NAME, sheet_name='Input generali')
        writer = pd.ExcelWriter('output/' + costants.OUTPUT_FILE_NAME, engine='xlsxwriter')
    for column in sessioni_df.columns:
        if ('Unnamed' in column):
            sessioni_df.rename(columns={column: ''}, inplace=True)
    sessioni_df.to_excel(writer, sheet_name='Input generali', index=False)

    workbook = writer.book
    worksheet = writer.sheets['Input generali']
    worksheet.set_zoom(90)

    header_format = workbook.add_format({
        "bg_color": "#ededed",
        "align": "center",
        "valign": "vcenter",
        "bold": True,
        "font_size": 12
    })

    column_format = workbook.add_format({
        "align": "center",
        "valign": "vcenter",
        "bold": True,
    })

    worksheet.set_column("A:A", 20, column_format)
    worksheet.set_column("B:C", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 40)
    worksheet.set_column("H:H", 20)
    worksheet.set_column("I:I", 40)

    for col_num, value in enumerate(sessioni_df.columns.values):  # setting header formatting
        worksheet.write(0, col_num, value, header_format)


    esami_primo_anno = []
    esami_secondo_anno = []
    esami_terzo_anno = []
    for esame in exams:
       # print(esame.nome[esame.nome.lower().find('mfn'):esame.nome.lower().find('mfn')+7],esame.short_name)
        if (esame.anno == 1):
            esami_primo_anno.append(esame)
        if (esame.anno == 2):
            esami_secondo_anno.append(esame)
        if (esame.anno == 3):
            esami_terzo_anno.append(esame)
    build_exams_output(esami_primo_anno, "esami primo anno", laboratori, aule,
                       model, writer, exams, sessioni)
    build_exams_output(esami_secondo_anno, "esami secondo anno", laboratori, aule,
                       model, writer, exams, sessioni)
    build_exams_output(esami_terzo_anno, "esami terzo anno", laboratori, aule,
                       model, writer, exams, sessioni)
    build_exams_output_riassunto(esami_primo_anno,esami_secondo_anno,esami_terzo_anno, "Risultati riassunti per anno", laboratori, aule,
                                 model, writer, exams, sessioni)
    build_exams_output_riassunto_2(esami_primo_anno, esami_secondo_anno, esami_terzo_anno, "Risultati riassunti per data",
                                 laboratori, aule,
                                 model, writer, exams, sessioni)

    build_statistiche(esami_primo_anno, esami_secondo_anno, esami_terzo_anno,
                                   "Risultati riassunti per data",
                                   laboratori, aule,
                                   model, writer, exams, sessioni)

    writer.save()
    print("Salvataggio file di ouput: "+output + '/' + costants.OUTPUT_FILE_NAME)
