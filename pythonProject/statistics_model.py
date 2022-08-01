from datetime import timedelta


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
