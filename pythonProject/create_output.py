import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import classes
import xlsxwriter
import costants
import holidays
import calendar

def build_exams_output(esami_anno, nome_foglio, laboratori, aule, model, writer, exams, sessione):
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
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = sessione[0][0] + timedelta(days=i)
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


    esami_df.insert(4, "Primo appello", appelli_estivi1, True)
    esami_df.insert(5, "Secondo appello", appelli_estivi2, True)

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

def build_exams_output_riassunto(esami_primo_anno,esami_secondo_anno,esami_terzo_anno, nome_foglio, laboratori, aule, model, writer, exams, sessione):
    esami_df = pd.DataFrame({})
    nomi_esami = []
    appelli_estivi1 = []
    appelli_estivi2 = []
    aule_lab=[]

    esami_primo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    esami_secondo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    esami_terzo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    nomi_esami.append("")
    prev='1'
    esami_primo_anno_primo_semestre=1
    esami_primo_anno_secondo_semestre=1
    for esame in esami_primo_anno:
        if(esame.lista_semestri[0]!=prev):
            nomi_esami.append("")
            prev='2'
        if esame.lista_semestri[0] == '1':
            esami_primo_anno_primo_semestre+=1
        else:
            esami_primo_anno_secondo_semestre+=1
        nomi_esami.append(esame.short_name)
    prev = '1'
    appelli_estivi1.append("Esami primo anno primo semestre")
    appelli_estivi2.append("")
    for esame in esami_primo_anno:
        if (esame.lista_semestri[0] != prev):
            appelli_estivi1.append("Esami primo anno secondo semestre")
            appelli_estivi2.append("")
            prev = '2'
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = sessione[0][0] + timedelta(days=i)
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

    prev='1'
    aule_lab.append("")
    for esame in esami_primo_anno:
        if (esame.lista_semestri[0] != prev):
            aule_lab.append("")
            prev = '2'
        exams_request=""
        for aula_richiesta in esame.aule_richieste:
            exams_request+=" "+aule[aula_richiesta].nome+","
        for lab_richiesto in esame.laboratori_richiesti:
            exams_request+=" "+laboratori[lab_richiesto].nome+","
        exams_request=exams_request[0:-1]
        exams_request=exams_request.replace("Laboratorio","Lab.")
        exams_request=exams_request.replace("laboratorio","lab.")
        exams_request=exams_request.replace("Dijkstra","Dij.")
        exams_request=exams_request.replace("dijkstra","dij.")
        exams_request=exams_request.replace("Turing","Tur.")
        exams_request=exams_request.replace("turing","tur.")
        exams_request=exams_request.replace("Vonneumann","Von.")
        exams_request=exams_request.replace("vonneumann","von.")
        exams_request=exams_request.replace("Babbage","Bab.")
        exams_request=exams_request.replace("Babbage","bab.")
        exams_request=exams_request.replace("postel","pos.")
        exams_request=exams_request.replace("Postel","Pos.")
        exams_request=exams_request.replace("Conferenze","Conf.")
        exams_request=exams_request.replace("conferenze","conf.")
        aule_lab.append(exams_request)

    nomi_esami.append("")
    prev = '1'
    esami_secondo_anno_primo_semestre = 1
    esami_secondo_anno_secondo_semestre = 1
    for esame in esami_secondo_anno:
        if (esame.lista_semestri[0] != prev):
            nomi_esami.append("")
            prev = '2'
        if(esame.lista_semestri[0]=='1'):
            esami_secondo_anno_primo_semestre+=1
        else:
            esami_secondo_anno_secondo_semestre+=1
        nomi_esami.append(esame.short_name)
    prev = '1'
    appelli_estivi1.append("Esami secondo anno primo semestre")
    appelli_estivi2.append("")
    for esame in esami_secondo_anno:
        if (esame.lista_semestri[0] != prev):
            appelli_estivi1.append("Esami secondo anno secondo semestre")
            appelli_estivi2.append("")
            prev = '2'
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = sessione[0][0] + timedelta(days=i)
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
    prev = '1'
    aule_lab.append("")
    for esame in esami_secondo_anno:
        if (esame.lista_semestri[0] != prev):
            aule_lab.append("")
            prev = '2'
        exams_request = ""
        for aula_richiesta in esame.aule_richieste:
            exams_request += " " + aule[aula_richiesta].nome+","
        for lab_richiesto in esame.laboratori_richiesti:
            exams_request += " " + laboratori[lab_richiesto].nome +","
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
        aule_lab.append(exams_request)

    nomi_esami.append("")
    prev = '1'
    esami_terzo_anno_primo_semestre = 1
    esami_terzo_anno_secondo_semestre = 1
    for esame in esami_terzo_anno:
        if (esame.lista_semestri[0] != prev):
            nomi_esami.append("")
            prev = '2'
        if(esame.lista_semestri[0]=='1'):
            esami_terzo_anno_primo_semestre+=1
        else:
            esami_terzo_anno_secondo_semestre+=1
        nomi_esami.append(esame.short_name)
    prev = '1'
    appelli_estivi1.append("Esami terzo anno primo semestre")
    appelli_estivi2.append("")
    for esame in esami_terzo_anno:
        if (esame.lista_semestri[0] != prev):
            appelli_estivi1.append("Esami terzo anno secondo semestre")
            appelli_estivi2.append("")
            prev = '2'
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = sessione[0][0] + timedelta(days=i)
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
    prev = '1'
    aule_lab.append("")
    for esame in esami_terzo_anno:
        if (esame.lista_semestri[0] != prev):
            aule_lab.append("")
            prev = '2'
        exams_request = ""
        for aula_richiesta in esame.aule_richieste:
            exams_request += " " + aule[aula_richiesta].nome+","
        for lab_richiesto in esame.laboratori_richiesti:
            exams_request += " " + laboratori[lab_richiesto].nome+","
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
        aule_lab.append(exams_request)


    esami_df.insert(0, "Primo appello", appelli_estivi1, True)
    esami_df.insert(1, "Secondo appello", appelli_estivi2, True)
    esami_df.insert(2, "Aule e laboratori richiesti", aule_lab, True)
    esami_df.insert(3, "Nome corso", nomi_esami, True)


    esami_df.to_excel(writer, sheet_name=nome_foglio, index=False)

    # set formatting
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
        print(val.values)
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
    appelli_estivi1 = []
    appelli_estivi2 = []
    aule_lab=[]

    esami_primo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    esami_secondo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    esami_terzo_anno.sort(key=lambda esame:esame.lista_semestri[0])
    nomi_esami.append("")
    prev='1'
    esami_primo_anno_primo_semestre=1
    esami_primo_anno_secondo_semestre=1
    for esame in esami_primo_anno:
        if(esame.lista_semestri[0]!=prev):
            nomi_esami.append("")
            prev='2'
        if esame.lista_semestri[0] == '1':
            esami_primo_anno_primo_semestre+=1
        else:
            esami_primo_anno_secondo_semestre+=1
        nomi_esami.append(esame.short_name)
    prev = '1'
    appelli_estivi1.append("Esami primo anno primo semestre")
    appelli_estivi2.append("")
    for esame in esami_primo_anno:
        if (esame.lista_semestri[0] != prev):
            appelli_estivi1.append("Esami primo anno secondo semestre")
            appelli_estivi2.append("")
            prev = '2'
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = sessione[0][0] + timedelta(days=i)
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

    prev='1'
    aule_lab.append("")
    for esame in esami_primo_anno:
        if (esame.lista_semestri[0] != prev):
            aule_lab.append("")
            prev = '2'
        exams_request=""
        for aula_richiesta in esame.aule_richieste:
            exams_request+=" "+aule[aula_richiesta].nome+","
        for lab_richiesto in esame.laboratori_richiesti:
            exams_request+=" "+laboratori[lab_richiesto].nome+","
        exams_request=exams_request[0:-1]
        exams_request=exams_request.replace("Laboratorio","Lab.")
        exams_request=exams_request.replace("laboratorio","lab.")
        exams_request=exams_request.replace("Dijkstra","Dij.")
        exams_request=exams_request.replace("dijkstra","dij.")
        exams_request=exams_request.replace("Turing","Tur.")
        exams_request=exams_request.replace("turing","tur.")
        exams_request=exams_request.replace("Vonneumann","Von.")
        exams_request=exams_request.replace("vonneumann","von.")
        exams_request=exams_request.replace("Babbage","Bab.")
        exams_request=exams_request.replace("Babbage","bab.")
        exams_request=exams_request.replace("postel","pos.")
        exams_request=exams_request.replace("Postel","Pos.")
        exams_request=exams_request.replace("Conferenze","Conf.")
        exams_request=exams_request.replace("conferenze","conf.")
        aule_lab.append(exams_request)

    nomi_esami.append("")
    prev = '1'
    esami_secondo_anno_primo_semestre = 1
    esami_secondo_anno_secondo_semestre = 1
    for esame in esami_secondo_anno:
        if (esame.lista_semestri[0] != prev):
            nomi_esami.append("")
            prev = '2'
        if(esame.lista_semestri[0]=='1'):
            esami_secondo_anno_primo_semestre+=1
        else:
            esami_secondo_anno_secondo_semestre+=1
        nomi_esami.append(esame.short_name)
    prev = '1'
    appelli_estivi1.append("Esami secondo anno primo semestre")
    appelli_estivi2.append("")
    for esame in esami_secondo_anno:
        if (esame.lista_semestri[0] != prev):
            appelli_estivi1.append("Esami secondo anno secondo semestre")
            appelli_estivi2.append("")
            prev = '2'
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = sessione[0][0] + timedelta(days=i)
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
    prev = '1'
    aule_lab.append("")
    for esame in esami_secondo_anno:
        if (esame.lista_semestri[0] != prev):
            aule_lab.append("")
            prev = '2'
        exams_request = ""
        for aula_richiesta in esame.aule_richieste:
            exams_request += " " + aule[aula_richiesta].nome+","
        for lab_richiesto in esame.laboratori_richiesti:
            exams_request += " " + laboratori[lab_richiesto].nome +","
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
        aule_lab.append(exams_request)

    nomi_esami.append("")
    prev = '1'
    esami_terzo_anno_primo_semestre = 1
    esami_terzo_anno_secondo_semestre = 1
    for esame in esami_terzo_anno:
        if (esame.lista_semestri[0] != prev):
            nomi_esami.append("")
            prev = '2'
        if(esame.lista_semestri[0]=='1'):
            esami_terzo_anno_primo_semestre+=1
        else:
            esami_terzo_anno_secondo_semestre+=1
        nomi_esami.append(esame.short_name)
    prev = '1'
    appelli_estivi1.append("Esami terzo anno primo semestre")
    appelli_estivi2.append("")
    for esame in esami_terzo_anno:
        if (esame.lista_semestri[0] != prev):
            appelli_estivi1.append("Esami terzo anno secondo semestre")
            appelli_estivi2.append("")
            prev = '2'
        index = exams.index(esame)
        date_esitive_esame = []
        durata_sessione = abs(sessione[0][1] - sessione[0][0])
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = sessione[0][0] + timedelta(days=i)
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
    prev = '1'
    aule_lab.append("")
    for esame in esami_terzo_anno:
        if (esame.lista_semestri[0] != prev):
            aule_lab.append("")
            prev = '2'
        exams_request = ""
        for aula_richiesta in esame.aule_richieste:
            exams_request += " " + aule[aula_richiesta].nome+","
        for lab_richiesto in esame.laboratori_richiesti:
            exams_request += " " + laboratori[lab_richiesto].nome+","
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
        aule_lab.append(exams_request)


    esami_df.insert(0, "Primo appello", appelli_estivi1, True)
    esami_df.insert(1, "Secondo appello", appelli_estivi2, True)
    esami_df.insert(2, "Aule e laboratori richiesti", aule_lab, True)
    esami_df.insert(3, "Nome corso", nomi_esami, True)

    sorted_df = esami_df.sort_values(by="Primo appello")
    #print(sorted_df)

    sorted_df.to_excel(writer, sheet_name=nome_foglio, index=False)

    # set formatting
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
    blank = workbook.add_format({
        "bg_color": "#ffffff",
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


def findExam(df,exam,sem):
    for esame in df:
        if esame.nome == exam and sem == esame.lista_semestri[0]:
            return True

def build_output(exams, laboratori, aule, model, sessioni):
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
        #print(esame.nome,esame.short_name)
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



    writer.save()
