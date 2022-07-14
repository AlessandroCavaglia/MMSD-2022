import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import classes
import xlsxwriter
import costants
import holidays

def build_exams_output(esami_anno,nome_foglio,laboratori,aule,model_sessione_invernale,model_sessione_estiva,model_sessione_settembre,writer,exams,sessione):
    esami_df = pd.DataFrame({})
    nomi_esami=[]
    for esame in esami_anno:
        nomi_esami.append(esame.nome)
    esami_df.insert(0,"Nome corso",nomi_esami,True)
    tipologia_esami=[]
    for esame in esami_anno:
        tipologia_esami.append(esame.tipo)
    esami_df.insert(1,"Tipologia",tipologia_esami,True)
    docenti_esami=[]
    for esame in esami_anno:
        docenti_esami.append(esame.insegnanti)
    esami_df.insert(2,"Docenti",docenti_esami,True)
    semestri_esami = []
    for esame in esami_anno:
        semestri=str(esame.lista_semestri)
        semestri=semestri.replace("[","")
        semestri=semestri.replace("]","")
        semestri=semestri.replace("'","")
        semestri_esami.append(semestri)
    esami_df.insert(3, "Semestre", semestri_esami, True)
    '''appelli_invernali=[]
    #TODO CALCOLARE APPELLI INVERNALI
    esami_df.insert(4, "Date appelli invernali", appelli_invernali, True)'''
    appelli_estivi = []
    for esame in esami_anno:
        index=exams.index(esame)
        date_esitive_esame=[]
        durata_sessione = abs(sessione[1][1]-sessione[1][0])
        for i in range(durata_sessione.days):
            if model_sessione_estiva.x[index,i].value==1:

                data = sessione[1][0] + timedelta(days=i)
                date_esitive_esame.append(str(data))
        date_esitive_esame=str(date_esitive_esame)
        date_esitive_esame = date_esitive_esame.replace("[", "")
        date_esitive_esame = date_esitive_esame.replace("]", "")
        date_esitive_esame = date_esitive_esame.replace("'", "")
        date_esitive_esame = date_esitive_esame.replace("00:00:00", "")
        appelli_estivi.append(date_esitive_esame)


    esami_df.insert(4, "Date appelli estivi", appelli_estivi, True)
    '''appelli_settembre= []
    # TODO CALCOLARE APPELLI SETTEMBRE
    esami_df.insert(6, "Date appelli settembre", appelli_settembre, True)'''
    esami_df.to_excel(writer, sheet_name=nome_foglio, index=False)

def build_output(exams,laboratori,aule,model_sessione_invernale,model_sessione_estiva,model_sessione_settembre,sessioni):
    #Move the general input page to the new document
    sessioni_df = pd.read_excel('input/' + costants.INPUT_FILE_NAME, sheet_name='Input generali 2.0')
    writer = pd.ExcelWriter('output/'+costants.OUTPUT_FILE_NAME, engine='xlsxwriter')
    for column in sessioni_df.columns:
        if('Unnamed' in column):
            sessioni_df.rename(columns = {column : ''}, inplace = True)
    sessioni_df.to_excel(writer, sheet_name='Input generali', index=False)
    esami_primo_anno=[]
    esami_secondo_anno=[]
    esami_terzo_anno=[]
    for esame in exams:
        if(esame.anno==1):
            esami_primo_anno.append(esame)
        if (esame.anno == 2):
            esami_secondo_anno.append(esame)
        if (esame.anno == 3):
            esami_terzo_anno.append(esame)
    build_exams_output(esami_primo_anno,"esami primo anno",laboratori,aule,model_sessione_invernale,model_sessione_estiva, model_sessione_settembre,writer,exams,sessioni)
    build_exams_output(esami_secondo_anno,"esami secondo anno",laboratori,aule,model_sessione_invernale,model_sessione_estiva,model_sessione_settembre,writer,exams,sessioni)
    build_exams_output(esami_terzo_anno,"esami terzo anno",laboratori,aule,model_sessione_invernale,model_sessione_estiva,model_sessione_settembre,writer,exams,sessioni)


    writer.save()





