import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import classes
import xlsxwriter
import costants
import holidays

def build_exams_output(esami_anno,nome_foglio,laboratori,aule,model,writer):
    esami_df = pd.DataFrame({})
    nomi_esami=[]
    for esame in esami_anno:
        nomi_esami.append(esame.nome)
    esami_df.insert(0,"Nome corso",nomi_esami,True)

    esami_df.to_excel(writer, sheet_name=nome_foglio, index=False)

def build_output(exams,laboratori,aule,model):
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
    build_exams_output(esami_primo_anno,"esami primo anno",laboratori,aule,model,writer)
    build_exams_output(esami_secondo_anno,"esami secondo anno",laboratori,aule,model,writer)
    build_exams_output(esami_terzo_anno,"esami terzo anno",laboratori,aule,model,writer)


    writer.save()





