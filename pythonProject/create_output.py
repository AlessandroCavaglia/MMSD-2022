import pandas as pd
from datetime import datetime, timedelta
from calendar_view import *
import numpy as np
import classes
import xlsxwriter
import costants
import holidays
import calendar


def build_exams_output(esami_anno, nome_foglio, laboratori, aule, model_sessione_invernale, model_sessione_estiva,
                       model_sessione_settembre, writer, exams, sessione):
    esami_df = pd.DataFrame({})
    nomi_esami = []
    for esame in esami_anno:
        nomi_esami.append(esame.nome)
    esami_df.insert(0, "Nome corso", nomi_esami, True)
    tipologia_esami = []
    for esame in esami_anno:
        tipologia_esami.append(esame.tipo)
    esami_df.insert(1, "Tipologia", tipologia_esami, True)
    docenti_esami = []
    for esame in esami_anno:
        docenti_esami.append(esame.insegnanti)
    esami_df.insert(2, "Docenti", docenti_esami, True)
    semestri_esami = []
    for esame in esami_anno:
        semestri = str(esame.lista_semestri)
        semestri = semestri.replace("[", "")
        semestri = semestri.replace("]", "")
        semestri = semestri.replace("'", "")
        semestri_esami.append(semestri)
    esami_df.insert(3, "Semestre", semestri_esami, True)
    appelli_estivi1 = []
    appelli_estivi2 = []





    for esame in esami_anno:
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[1][1] - sessione[1][0])
        for i in range(durata_sessione.days + 1):
            if model_sessione_estiva.x[index, i].value == 1:
                data = sessione[1][0] + timedelta(days=i)
                date_esitive_esame.append(str(data))
        date_esitive_esame1=""
        for i in range(esame.numero_giorni_durata):
            date_esitive_esame1 +=" "+ date_esitive_esame[i]

        date_esitive_esame1 = date_esitive_esame1.replace("[", "")
        date_esitive_esame1 = date_esitive_esame1.replace("]", "")
        date_esitive_esame1 = date_esitive_esame1.replace("'", "")
        date_esitive_esame1 = date_esitive_esame1.replace("00:00:00", "")
        appelli_estivi1.append(date_esitive_esame1)

        if(len(date_esitive_esame)>esame.numero_giorni_durata):
            date_esitive_esame2=""
            for i in range(esame.numero_giorni_durata):
                date_esitive_esame2 +=" "+ date_esitive_esame[esame.numero_giorni_durata + i]
            date_esitive_esame2 = date_esitive_esame2.replace("[", "")
            date_esitive_esame2 = date_esitive_esame2.replace("]", "")
            date_esitive_esame2 = date_esitive_esame2.replace("'", "")
            date_esitive_esame2 = date_esitive_esame2.replace("00:00:00", "")
            appelli_estivi2.append(date_esitive_esame2)
        else:
            appelli_estivi2.append('')


    esami_df.insert(4, "Date appelli estivi primo appello", appelli_estivi1, True)
    esami_df.insert(5, "Date appelli estivi secondo appello", appelli_estivi2, True)

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

def build_exams_output_riassunto(esami_anno, nome_foglio, laboratori, aule, model_sessione_invernale, model_sessione_estiva,
                       model_sessione_settembre, writer, exams, sessione):
    esami_df = pd.DataFrame({})
    nomi_esami = []
    for esame in esami_anno:
        nomi_esami.append(esame.nome)
    esami_df.insert(0, "Nome corso", nomi_esami, True)
    appelli_estivi1 = []
    appelli_estivi2 = []
    for esame in esami_anno:
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[1][1] - sessione[1][0])
        for i in range(durata_sessione.days + 1):
            if model_sessione_estiva.x[index, i].value == 1:
                data = sessione[1][0] + timedelta(days=i)
                date_esitive_esame.append(str(data))
        date_esitive_esame1 = ""
        for i in range(esame.numero_giorni_durata):
            date_esitive_esame1 += " " + date_esitive_esame[i]
        date_esitive_esame1 = date_esitive_esame1.replace("[", "")
        date_esitive_esame1 = date_esitive_esame1.replace("]", "")
        date_esitive_esame1 = date_esitive_esame1.replace("'", "")
        date_esitive_esame1 = date_esitive_esame1.replace("00:00:00", "")
        appelli_estivi1.append(date_esitive_esame1)
        if (len(date_esitive_esame) > esame.numero_giorni_durata):
            date_esitive_esame2 = ""
            for i in range(0, esame.numero_giorni_durata):
                date_esitive_esame2 += " " + date_esitive_esame[esame.numero_giorni_durata + i]
            date_esitive_esame2 = date_esitive_esame2.replace("[", "")
            date_esitive_esame2 = date_esitive_esame2.replace("]", "")
            date_esitive_esame2 = date_esitive_esame2.replace("'", "")
            date_esitive_esame2 = date_esitive_esame2.replace("00:00:00", "")
            appelli_estivi2.append(date_esitive_esame2)
        else:
            appelli_estivi2.append('')


    esami_df.insert(1, "Date appelli estivi primo appello", appelli_estivi1, True)
    esami_df.insert(2, "Date appelli estivi secondo appello", appelli_estivi2, True)
    '''appelli_settembre= []
    # TODO CALCOLARE APPELLI SETTEMBRE
    esami_df.insert(6, "Date appelli settembre", appelli_settembre, True)'''
    esami_df.to_excel(writer, sheet_name=nome_foglio, index=False)

    # set formatting
    workbook = writer.book
    worksheet = writer.sheets[nome_foglio]
    worksheet.set_zoom(90)
    worksheet.set_column("A:A", 150)
    worksheet.set_column("B:C", 50)
    worksheet.set_column("D:D", 15, workbook.add_format({"align": "center"}))
    worksheet.set_column("E:E", 50)
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



def build_output(exams, laboratori, aule, model_sessione_invernale, model_sessione_estiva, model_sessione_settembre,
                 sessioni):
    # Move the general input page to the new document
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
        if (esame.anno == 1):
            esami_primo_anno.append(esame)
        if (esame.anno == 2):
            esami_secondo_anno.append(esame)
        if (esame.anno == 3):
            esami_terzo_anno.append(esame)
    build_exams_output(esami_primo_anno, "esami primo anno", laboratori, aule, model_sessione_invernale,
                       model_sessione_estiva, model_sessione_settembre, writer, exams, sessioni)
    build_exams_output_riassunto(esami_primo_anno, "esami primo anno riassunto", laboratori, aule, model_sessione_invernale,
                       model_sessione_estiva, model_sessione_settembre, writer, exams, sessioni)
    build_exams_output(esami_secondo_anno, "esami secondo anno", laboratori, aule, model_sessione_invernale,
                       model_sessione_estiva, model_sessione_settembre, writer, exams, sessioni)
    build_exams_output_riassunto(esami_secondo_anno, "esami secondo anno riassunto", laboratori, aule, model_sessione_invernale,
                       model_sessione_estiva, model_sessione_settembre, writer, exams, sessioni)
    build_exams_output(esami_terzo_anno, "esami terzo anno", laboratori, aule, model_sessione_invernale,
                       model_sessione_estiva, model_sessione_settembre, writer, exams, sessioni)
    build_exams_output_riassunto(esami_terzo_anno, "esami terzo anno riassunto", laboratori, aule, model_sessione_invernale,
                       model_sessione_estiva, model_sessione_settembre, writer, exams, sessioni)

    writer.save()
