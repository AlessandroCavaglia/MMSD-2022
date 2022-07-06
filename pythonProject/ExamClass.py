class Exam:
    def __init__(self, nome, tipo, insegnanti, lista_semestri,anno,numero_appelli_sessione_full,
                 numero_appelli_sessione_small,aule_richieste,numero_aule_slot,laboratori_richiesti,
                 numero_lab_slot,numero_giorni_durata,date_preferenza,date_indisponibilita,note):
        self.nome = nome
        self.tipo = tipo
        self.insegnanti = insegnanti
        self.lista_semestri = lista_semestri
        self.anno = anno
        self.numero_appelli_sessione_full = numero_appelli_sessione_full
        self.numero_appelli_sessione_small = numero_appelli_sessione_small
        self.aule_richieste = aule_richieste
        self.numero_aule_slot = numero_aule_slot
        self.laboratori_richiesti = laboratori_richiesti
        self.numero_lab_slot = numero_lab_slot
        self.numero_giorni_durata = numero_giorni_durata
        self.date_preferenza = date_preferenza
        self.date_indisponibilita = date_indisponibilita
        self.note = note