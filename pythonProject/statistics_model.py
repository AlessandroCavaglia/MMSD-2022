from datetime import timedelta, datetime

from pythonProject import classes
class Object(object):
    pass

def generate_statistics(model,exams,data_inizio,data_fine):
    print("------- STATISTICHE -------")
    esami_primo_anno = []
    esami_secondo_anno = []
    esami_terzo_anno = []
    esami_primo_anno_primo_semestre=[]
    esami_primo_anno_secondo_semestre=[]
    esami_secondo_anno_primo_semestre=[]
    esami_secondo_anno_secondo_semestre=[]
    esami_terzo_anno_primo_semestre = []
    esami_terzo_anno_secondo_semestre = []
    durata_sessione = abs(data_fine - data_inizio)
    date_esami_primo_anno = []
    date_esami_secondo_anno = []
    date_esami_terzo_anno = []
    date_esami_primo_anno_primo_semestre = []
    date_esami_primo_anno_secondo_semestre = []
    date_esami_secondo_anno_primo_semestre = []
    date_esami_secondo_anno_secondo_semestre = []
    date_esami_terzo_anno_primo_semestre = []
    date_esami_terzo_anno_secondo_semestre = []
    #Divisione in gruppi
    for esame in exams:
        if (esame.anno == 1):
            esami_primo_anno.append(esame)
            if '1'==esame.lista_semestri[0]:
                esami_primo_anno_primo_semestre.append(esame)
            else:
                esami_primo_anno_secondo_semestre.append(esame)
        if (esame.anno == 2):
            esami_secondo_anno.append(esame)
            if '1' == esame.lista_semestri[0]:
                esami_secondo_anno_primo_semestre.append(esame)
            else:
                esami_secondo_anno_secondo_semestre.append(esame)
        if (esame.anno == 3):
            esami_terzo_anno.append(esame)
            if '1' == esame.lista_semestri[0]:
                esami_terzo_anno_primo_semestre.append(esame)
            else:
                esami_terzo_anno_secondo_semestre.append(esame)

    #Calcolo date degli esami
    for esame in esami_primo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno.append(date_esame)
    for esame in esami_secondo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno.append(date_esame)
    for esame in esami_terzo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno.append(date_esame)

    for esame in esami_primo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno_primo_semestre.append(date_esame)
    for esame in esami_primo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno_secondo_semestre.append(date_esame)

    for esame in esami_secondo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno_primo_semestre.append(date_esame)
    for esame in esami_secondo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno_secondo_semestre.append(date_esame)

    for esame in esami_terzo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else :
            if (len(date_esame)==1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno_primo_semestre.append(date_esame)
    for esame in esami_terzo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno_secondo_semestre.append(date_esame)



    print("-- Distanze esami del primo anno --")
    distanza_media=0
    distanza_minima=1000000
    distanza_massima=-1
    entries=0
    for index1,esame1 in enumerate(esami_primo_anno):
        for index2,esame2 in enumerate(esami_primo_anno):
            if(esame1!=esame2):
                distanza_media += abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                if(abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)<distanza_minima):
                    distanza_minima=abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                if(abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)>distanza_massima):
                    distanza_massima=abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                if (abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                if (abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                entries+=2

    distanza_media = distanza_media/entries
    print("Distanza Media: "+str(distanza_media))
    print("Distanza Minima: "+str(distanza_minima))
    print("Distanza Massima: "+str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del primo anno primo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_primo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_primo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del primo anno secondo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_primo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_primo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del secondo anno --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno):
        for index2, esame2 in enumerate(esami_secondo_anno):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                if (abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                if (abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                if (abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                if (abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del secondo anno primo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_secondo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del secondo anno secondo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_secondo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del terzo anno --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno):
        for index2, esame2 in enumerate(esami_terzo_anno):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                if (abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                if (abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                if (abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                if (abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del terzo anno primo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_terzo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del terzo anno secondo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_terzo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")


    return

def generate_statistics_for_graphic(model,exams,data_inizio,data_fine):
    print("------- STATISTICHE -------")
    output=""
    esami_primo_anno = []
    esami_secondo_anno = []
    esami_terzo_anno = []
    esami_primo_anno_primo_semestre=[]
    esami_primo_anno_secondo_semestre=[]
    esami_secondo_anno_primo_semestre=[]
    esami_secondo_anno_secondo_semestre=[]
    esami_terzo_anno_primo_semestre = []
    esami_terzo_anno_secondo_semestre = []
    durata_sessione = abs(data_fine - data_inizio)
    date_esami_primo_anno = []
    date_esami_secondo_anno = []
    date_esami_terzo_anno = []
    date_esami_primo_anno_primo_semestre = []
    date_esami_primo_anno_secondo_semestre = []
    date_esami_secondo_anno_primo_semestre = []
    date_esami_secondo_anno_secondo_semestre = []
    date_esami_terzo_anno_primo_semestre = []
    date_esami_terzo_anno_secondo_semestre = []
    #Divisione in gruppi
    for esame in exams:
        if (esame.anno == 1):
            esami_primo_anno.append(esame)
            if '1'==esame.lista_semestri[0]:
                esami_primo_anno_primo_semestre.append(esame)
            else:
                esami_primo_anno_secondo_semestre.append(esame)
        if (esame.anno == 2):
            esami_secondo_anno.append(esame)
            if '1' == esame.lista_semestri[0]:
                esami_secondo_anno_primo_semestre.append(esame)
            else:
                esami_secondo_anno_secondo_semestre.append(esame)
        if (esame.anno == 3):
            esami_terzo_anno.append(esame)
            if '1' == esame.lista_semestri[0]:
                esami_terzo_anno_primo_semestre.append(esame)
            else:
                esami_terzo_anno_secondo_semestre.append(esame)

    #Calcolo date degli esami
    for esame in esami_primo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno.append(date_esame)
    for esame in esami_secondo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno.append(date_esame)
    for esame in esami_terzo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno.append(date_esame)

    for esame in esami_primo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno_primo_semestre.append(date_esame)
    for esame in esami_primo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno_secondo_semestre.append(date_esame)

    for esame in esami_secondo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno_primo_semestre.append(date_esame)
    for esame in esami_secondo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno_secondo_semestre.append(date_esame)

    for esame in esami_terzo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else :
            if (len(date_esame)==1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno_primo_semestre.append(date_esame)
    for esame in esami_terzo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index, i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno_secondo_semestre.append(date_esame)



    output+="-- Distanze esami del primo anno -- \n"
    distanza_media=0
    distanza_minima=1000000
    distanza_massima=-1
    entries=0
    for index1,esame1 in enumerate(esami_primo_anno):
        for index2,esame2 in enumerate(esami_primo_anno):
            if(esame1!=esame2):
                distanza_media += abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                if(abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)<distanza_minima):
                    distanza_minima=abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                if(abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)>distanza_massima):
                    distanza_massima=abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                if (abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                if (abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                entries+=2

    distanza_media = distanza_media/entries
    output+="Distanza Media: "+str(distanza_media)+"\n"
    output+="Distanza Minima: "+str(distanza_minima)+"\n"
    output+="Distanza Massima: "+str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del primo anno primo semestre --\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_primo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_primo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del primo anno secondo semestre --\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_primo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_primo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del secondo anno --\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno):
        for index2, esame2 in enumerate(esami_secondo_anno):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                if (abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                if (abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                if (abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                if (abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del secondo anno primo semestre --\n\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_secondo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del secondo anno secondo semestre --\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_secondo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del terzo anno --\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno):
        for index2, esame2 in enumerate(esami_terzo_anno):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                if (abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                if (abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                if (abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                if (abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del terzo anno primo semestre --\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_terzo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"

    output+="-- Distanze esami del terzo anno secondo semestre --\n"
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_terzo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    output+="Distanza Media: " + str(distanza_media)+"\n"
    output+="Distanza Minima: " + str(distanza_minima)+"\n"
    output+="Distanza Massima: " + str(distanza_massima)+"\n"

    output+="-------------------------------------------------------\n\n"


    return output

def generate_statistics_2(model,exams,data_inizio,data_fine):
    print("------- STATISTICHE -------")
    esami_primo_anno = []
    esami_secondo_anno = []
    esami_terzo_anno = []
    esami_primo_anno_primo_semestre=[]
    esami_primo_anno_secondo_semestre=[]
    esami_secondo_anno_primo_semestre=[]
    esami_secondo_anno_secondo_semestre=[]
    esami_terzo_anno_primo_semestre = []
    esami_terzo_anno_secondo_semestre = []
    durata_sessione = abs(data_fine - data_inizio)
    date_esami_primo_anno = []
    date_esami_secondo_anno = []
    date_esami_terzo_anno = []
    date_esami_primo_anno_primo_semestre = []
    date_esami_primo_anno_secondo_semestre = []
    date_esami_secondo_anno_primo_semestre = []
    date_esami_secondo_anno_secondo_semestre = []
    date_esami_terzo_anno_primo_semestre = []
    date_esami_terzo_anno_secondo_semestre = []
    #Divisione in gruppi
    for esame in exams:
        if (esame.anno == 1):
            esami_primo_anno.append(esame)
            if '1'==esame.lista_semestri[0]:
                esami_primo_anno_primo_semestre.append(esame)
            else:
                esami_primo_anno_secondo_semestre.append(esame)
        if (esame.anno == 2):
            esami_secondo_anno.append(esame)
            if '1' == esame.lista_semestri[0]:
                esami_secondo_anno_primo_semestre.append(esame)
            else:
                esami_secondo_anno_secondo_semestre.append(esame)
        if (esame.anno == 3):
            esami_terzo_anno.append(esame)
            if '1' == esame.lista_semestri[0]:
                esami_terzo_anno_primo_semestre.append(esame)
            else:
                esami_terzo_anno_secondo_semestre.append(esame)

    #Calcolo date degli esami
    for esame in esami_primo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno.append(date_esame)
    for esame in esami_secondo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno.append(date_esame)
    for esame in esami_terzo_anno:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno.append(date_esame)

    for esame in esami_primo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno_primo_semestre.append(date_esame)
    for esame in esami_primo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_primo_anno_secondo_semestre.append(date_esame)

    for esame in esami_secondo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno_primo_semestre.append(date_esame)
    for esame in esami_secondo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_secondo_anno_secondo_semestre.append(date_esame)

    for esame in esami_terzo_anno_primo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else :
            if (len(date_esame)==1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno_primo_semestre.append(date_esame)
    for esame in esami_terzo_anno_secondo_semestre:
        index = exams.index(esame)
        date_esame=[]
        for i in range(durata_sessione.days + 1):
            if model.x[index][i].value == 1:
                data = data_inizio + timedelta(days=i)
                date_esame.append(data)
        if(len(date_esame)==4):
            del date_esame[2]
            del date_esame[0]
        else:
            if (len(date_esame) == 1):
                date_esame.append(date_esame[0])
        date_esami_terzo_anno_secondo_semestre.append(date_esame)



    print("-- Distanze esami del primo anno --")
    distanza_media=0
    distanza_minima=1000000
    distanza_massima=-1
    entries=0
    for index1,esame1 in enumerate(esami_primo_anno):
        for index2,esame2 in enumerate(esami_primo_anno):
            if(esame1!=esame2):
                distanza_media += abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                if(abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)<distanza_minima):
                    distanza_minima=abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                if(abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)>distanza_massima):
                    distanza_massima=abs((date_esami_primo_anno[index1][0] - date_esami_primo_anno[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                if (abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                if (abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno[index1][1] - date_esami_primo_anno[index2][1]).days)
                entries+=2

    distanza_media = distanza_media/entries
    print("Distanza Media: "+str(distanza_media))
    print("Distanza Minima: "+str(distanza_minima))
    print("Distanza Massima: "+str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del primo anno primo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_primo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_primo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_primo_semestre[index1][0] - date_esami_primo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_primo_semestre[index1][1] - date_esami_primo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del primo anno secondo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_primo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_primo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_secondo_semestre[index1][0] - date_esami_primo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_primo_anno_secondo_semestre[index1][1] - date_esami_primo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del secondo anno --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno):
        for index2, esame2 in enumerate(esami_secondo_anno):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                if (abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                if (abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno[index1][0] - date_esami_secondo_anno[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                if (abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                if (abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno[index1][1] - date_esami_secondo_anno[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del secondo anno primo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_secondo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_primo_semestre[index1][0] - date_esami_secondo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_primo_semestre[index1][1] - date_esami_secondo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del secondo anno secondo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_secondo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_secondo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_secondo_semestre[index1][0] - date_esami_secondo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_secondo_anno_secondo_semestre[index1][1] - date_esami_secondo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del terzo anno --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno):
        for index2, esame2 in enumerate(esami_terzo_anno):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                if (abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                if (abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno[index1][0] - date_esami_terzo_anno[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                if (abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                if (abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno[index1][1] - date_esami_terzo_anno[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del terzo anno primo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno_primo_semestre):
        for index2, esame2 in enumerate(esami_terzo_anno_primo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_primo_semestre[index1][0] - date_esami_terzo_anno_primo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_primo_semestre[index1][1] - date_esami_terzo_anno_primo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")

    print("-- Distanze esami del terzo anno secondo semestre --")
    distanza_media = 0
    distanza_minima = 1000000
    distanza_massima = -1
    entries = 0
    for index1, esame1 in enumerate(esami_terzo_anno_secondo_semestre):
        for index2, esame2 in enumerate(esami_terzo_anno_secondo_semestre):
            if (esame1 != esame2):
                distanza_media += abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_secondo_semestre[index1][0] - date_esami_terzo_anno_secondo_semestre[index2][0]).days)
                distanza_media += abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days) < distanza_minima):
                    distanza_minima = abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                if (abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days) > distanza_massima):
                    distanza_massima = abs((date_esami_terzo_anno_secondo_semestre[index1][1] - date_esami_terzo_anno_secondo_semestre[index2][1]).days)
                entries += 2

    distanza_media = distanza_media / entries
    print("Distanza Media: " + str(distanza_media))
    print("Distanza Minima: " + str(distanza_minima))
    print("Distanza Massima: " + str(distanza_massima))

    print("-------------------------------------------------------")


    return

if __name__ == '__main__':
    exams = []
    data_inizio=datetime.strptime("09/06/22", '%d/%m/%y')
    data_fine=datetime.strptime("29/07/22", '%d/%m/%y')
    exams.append(classes.Exam("CMRO", "", "", ["1"], 1, 2, [],[],
                         [0,2],[1,1], 1, [], [], ""))
    exams.append(classes.Exam("MATE DISC", "", "", ["1"], 1, 2, [0,1,2,3],[1,1,1,1],
                         [],[], 1, [], [], ""))
    exams.append(classes.Exam("LOGICA", "", "", ["1"], 1, 2, [0, 1, 2, 3], [1, 1, 1, 1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("PROG 1", "", "", ["1"], 1, 2, [], [],
                              [0,1,2], [1,1,1], 1, [], [], ""))

    exams.append(classes.Exam("ANALISI", "", "", ["2"], 1, 2, [], [],
                              [0,1,2], [1,1,1], 1, [], [], ""))
    exams.append(classes.Exam("ARCH ELAB", "", "", ["2"], 1, 2, [], [],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("PROG 2", "", "", ["2"], 1, 2, [], [],
                              [0,2], [1,1], 2, [], [], ""))
    exams.append(classes.Exam("INGLESE", "", "", ["2"], 1, 2, [], [],
                              [], [], 1, [], [], ""))

    exams.append(classes.Exam("STATISTICA", "", "", ["1"], 2, 2, [], [],
                              [1,2], [1,1], 1, [], [], ""))
    exams.append(classes.Exam("SIS OPERATIVI", "", "", ["1"], 2, 2, [], [],
                              [2], [1], 1, [], [], ""))
    exams.append(classes.Exam("LFT", "", "", ["1"], 2, 2, [], [],
                              [1], [1], 1, [], [], ""))
    exams.append(classes.Exam("ALGO", "", "", ["2"], 2, 2, [], [],
                              [1,2], [1,1], 1, [], [], ""))
    exams.append(classes.Exam("BASI DATI", "", "", ["2"], 2, 2, [0,1,2,3], [1,1,1,1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("EGINB", "", "", ["2"], 2, 2, [0, 1, 2], [1, 1, 1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("EGINB DIRITTO", "", "", ["2"], 2, 2, [4], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("FISICA", "", "", ["2"], 2, 2, [], [],
                              [], [], 1, [], [], ""))

    exams.append(classes.Exam("EGINN", "", "", ["1"], 3, 2, [0,1,2], [1,1,1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("IUMTWEB", "", "", ["1"], 3, 2, [0, 1], [1, 1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("SIS INF", "", "", ["1"], 3, 2, [5], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("TWEB", "", "", ["1"], 3, 2, [5], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("LPP", "", "", ["1"], 3, 2, [2], [1],
                              [1], [1], 1, [], [], ""))
    exams.append(classes.Exam("CALC E COMPL", "", "", ["1"], 3, 2, [], [],
                              [1], [1], 1, [], [], ""))
    exams.append(classes.Exam("PROG 3", "", "", ["1"], 3, 2, [0], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("RETI 1", "", "", ["1"], 3, 2, [0], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("MFDI", "", "", ["2"], 3, 2, [2], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("SIS INT", "", "", ["2"], 3, 2, [5], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("SICUREZZA", "", "", ["2"], 3, 2, [0], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("SAS", "", "", ["2"], 3, 2, [0,1], [1,1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("LOGICA", "", "", ["2"], 3, 2, [5], [1],
                              [], [], 1, [], [], ""))
    exams.append(classes.Exam("STORIA", "", "", ["2"], 3, 2, [], [],
                              [2], [1], 1, [], [], ""))
    exams.append(classes.Exam("RETI ELAB", "", "", ["2"], 3, 2, [1,2], [1,1],
                              [], [], 1, [], [], ""))

    model=Object()
    model.x=[[Object() for i in range(abs(data_fine - data_inizio).days+1)] for i in range(len(exams))]

    for i in range(len(exams)):
        for j in range(abs(data_fine - data_inizio).days+1):
            model.x[i][j].value=0

    model.x[0][5].value=1
    model.x[0][26].value=1

    model.x[1][4].value=1
    model.x[1][31].value=1

    model.x[2][7].value=1
    model.x[2][35].value=1

    model.x[3][11].value=1
    model.x[3][39].value=1

    model.x[4][0].value=1
    model.x[4][28].value=1

    model.x[5][3].value=1
    model.x[5][21].value=1

    model.x[6][6].value=1
    model.x[6][7].value=1
    model.x[6][32].value=1
    model.x[6][33].value=1

    model.x[7][7].value=1
    model.x[7][33].value=1

    model.x[8][12].value=1
    model.x[8][41].value=1

    model.x[9][7].value=1
    model.x[9][27].value=1

    model.x[10][1].value=1
    model.x[10][24].value=1

    model.x[11][4].value=1
    model.x[11][38].value=1

    model.x[12][10].value=1
    model.x[12][31].value=1

    model.x[13][3].value=1
    model.x[13][21].value=1

    model.x[14][5].value=1
    model.x[14][24].value=1

    model.x[15][12].value=1
    model.x[15][35].value=1

    model.x[16][3].value=1
    model.x[16][21].value=1

    model.x[17][4].value=1
    model.x[17][33].value=1

    model.x[18][6].value=1
    model.x[18][24].value=1

    model.x[19][11].value=1
    model.x[19][34].value=1

    model.x[20][5].value=1
    model.x[20][25].value=1

    model.x[21][17].value=1
    model.x[21][35].value=1

    model.x[22][8].value=1
    model.x[22][39].value=1

    model.x[23][10].value=1
    model.x[23][32].value=1

    model.x[24][11].value=1
    model.x[24][40].value=1

    model.x[25][3].value=1
    model.x[25][33].value=1

    model.x[26][1].value=1
    model.x[26][24].value=1

    model.x[27][5].value=1
    model.x[27][28].value=1

    model.x[28][10].value=1
    model.x[28][38].value=1

    model.x[29][8].value=1
    model.x[29][35].value=1

    model.x[30][6].value=1
    model.x[30][27].value=1

    generate_statistics_2(model,exams,data_inizio,data_fine)