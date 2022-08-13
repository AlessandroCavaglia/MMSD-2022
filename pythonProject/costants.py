COLONNE_LABORATORI = [7, 8]
COLONNE_AULE = [4, 5]
COLONNE_SESSIONI = [1, 2]
COLONNE_PARAMETRI = [10, 11]
# INPUT_FILE_NAME="input modello.xlsx"
INPUT_FILE_NAME="Input modello sessione estiva.xlsx"
#INPUT_FILE_NAME = "Input modello sessione invernale.xlsx"
# INPUT_FILE_NAME="Input modello sessione settembre.xlsx"
OUTPUT_FILE_NAME = "output modello.xlsx"

# Model
MIN_DISTANCE_APPELLI = 10
SLOT_AULE = 2
SLOT_LABORATORI = 3
GUADAGNO_GIORNI_PREFERITI = 2
COSTANTE_IMPORTANZA_PRIMO_ANNO = 4
COSTANTE_IMPORTANZA_SECONDO_ANNO = 4

# utilizzati per l'utput dei corsi
ANNI_SEMESTRI_COLORI = ['#c0a162', '#62c099', '#e2f451', '#f45a63', '#afdcdd', '#9be873']

# Mapping nome corso
NOME_CORSO_STRONG = {
    "Calcolo Matriciale e Ricerca Operativa": "CMRO",
    "Matematica Discreta": "MATE DISC",
    "Logica": "LOG",
    "ProgrammazioneI": "PROG I",
    "Lingua Inglese I": "ING 1",
    "ANALISI MATEMATICA": "ANALISI",
    "Architettura degli Elaboratori": "ARCH. ELAB",
    "ProgrammazioneII": "PROG II",
    "Elementi di probabilità e statistica": "ELEM. PROB.",
    "Sistemi Operativi": "SIS. OPERATIVI",
    "Linguaggi Formali e Traduttori": "LFT",
    "Algoritmi e strutture Dati": "ALG STRUT. DATI",
    "Basi dati": "BASI DATI",
    "PARTE DI ECONOMIA": "EGI",
    "PARTE DI DIRITTO": "PRIVACY",
    "Fisica": "FISICA",
    "ECONOMIA E GESTIONEdell'innovazione": "EGIN",
    "MFN0608": "T.WEB(IUM)",
    "MFN1353": "IUM",
    "Sistemi Informativi": "SIS. INF.",
    "MFN0634": "T.WEB",
    "Linguaggi e Paradigmi di Programmazione": "LPP",
    "Calcolabilità e complessita": "CALC. E COMPL.",
    "ProgrammazioneIII": "PROG III",
    "MFN1362": "RETI",
    "Metodi formali dell'informatica": "METODI FORMALI INF.",
    "LOGICA PER L'INFORMATICA": "LOGICA PER INF.",
    "Storia dell'informatica": "STORIA INF.",
    "RETI DI ELABORATORI": "RETI ELAB.",
    "SISTEMI INTELLIGENTI": "SIS. INT.",
    "Sicurezza": "SICUREZZA",
    "Sviluppo delle applicazioni software": "SVIL. APP SOFT."
}

NOME_CORSO_CODE = {
    "MFN0588": "CMRO",
    "INF0290": "MATE DISC",
    "MFN0984": "LOG",
    "MFN0582": "PROG I",
    "MFN0570": "ANALISI",
    "MFN0586": "ARCH. ELAB",
    "MFN0585": "PROG II",
    "MFN0590": "ING 1",
    "MFN0600": "ELEM. PROB.",
    "MFN0601": "SIS. OPERATIVI",
    "MFN0603": "LFT",
    "MFN0597": "ALG STRUT. DATI",
    "MFN0602": "BASI DATI",
    "Mfn0604": "EGI",
    "Mfn0604": "PRIVACY",
    "MFN0598": "FISICA",
    "mfn0617": "EGIN",
    "MFN0608": "T.WEB(IUM)",
    "MFN1353": "IUM",
    "MFN0618": "SIS. INF.",
    "MFN0634": "T.WEB",
    "MFN0610": "LPP",
    "MFN0612": "CALC. E COMPL.",
    "MFN0605": "PROG III",
    "MFN1362": "RETI",
    "mfn0633": "METODI FORMALI INF.",
    "mfn0607": "SIS. INT.",
    "MFN0636": "SICUREZZA",
    "mfn0606": "SVIL. APP SOFT.",
    "INF0003": "LOGICA PER INF.",
    "INF0004": "STORIA INF.",
    "MFN0635": "RETI ELAB."
}

# default advanced settings per cplex
ADVANCED_SETTINGS = {
    "time_limit": "None",
    "gap_tollerance": "None"
}

# Nome dei modelli mostrati nel dropdown all'interno della GUI
MODEL = ['Default Model', 'Variation Model 1', 'Variation Model 2', 'Variation Model 3']

# Associazione chive valore nomi modelli nella GUI file.py
MODEL_MAPPING = {
    'Default Model': 'model_building',
    'Variation Model 1': 'model_building1',
    'Variation Model 2': 'model_building2',
    'Variation Model 3': 'model_building3'
}
