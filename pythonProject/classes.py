from pythonProject.costants import NOME_CORSO, NOME_CORSO_STRONG


class Exam:
    def __init__(self, nome, tipo, insegnanti, lista_semestri, anno, numero_appelli_sessione_full,
                 aule_richieste, numero_aule_slot, laboratori_richiesti,
                 numero_lab_slot, numero_giorni_durata, date_preferenza, date_indisponibilita, note):
        self.nome = nome
        #self.short_name = NOME_CORSO[str.replace(str.replace(nome, '\n', ''),' ', '')]
        self.short_name = getShortName(str(nome))
        self.tipo = tipo
        self.insegnanti = insegnanti
        self.lista_semestri = lista_semestri
        self.anno = anno
        self.numero_appelli = numero_appelli_sessione_full
        self.aule_richieste = aule_richieste
        self.numero_aule_slot = numero_aule_slot
        self.laboratori_richiesti = laboratori_richiesti
        self.numero_lab_slot = numero_lab_slot
        self.numero_giorni_durata = numero_giorni_durata
        self.date_preferenza = date_preferenza
        self.date_indisponibilita = date_indisponibilita
        self.note = note


def getShortName(nome):
    for key in NOME_CORSO_STRONG:
        if key in nome :
            return NOME_CORSO_STRONG[key]

    return "undefined"

class ExamRoom:
    def __init__(self, nome, indisponibilita):
        self.nome = nome
        self.indisponibilita = indisponibilita



class Session:
    def __init__(self, nome, data_inizio, data_fine):
        self.nome = nome
        self.dataInizio = data_inizio
        self.dataFine = data_fine
        self.durata = abs(data_fine - data_inizio).days
