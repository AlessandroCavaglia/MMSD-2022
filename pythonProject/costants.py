COLONNE_LABORATORI = [7, 8]
COLONNE_AULE = [4, 5]
COLONNE_SESSIONI = [1, 2]
COLONNE_PARAMETRI = [10, 11]
# INPUT_FILE_NAME="input modello.xlsx"
# INPUT_FILE_NAME="Input modello sessione estiva.xlsx"
INPUT_FILE_NAME = "Input modello sessione invernale.xlsx"
# INPUT_FILE_NAME="Input modello sessione settembre.xlsx"
OUTPUT_FILE_NAME = "output modello.xlsx"

# Model

MIN_DISTANCE_APPELLI = 10
SLOT_AULE = 2
SLOT_LABORATORI = 3
GUADAGNO_GIORNI_PREFERITI = 2
COSTANTE_IMPORTANZA_PRIMO_ANNO = 4
COSTANTE_IMPORTANZA_SECONDO_ANNO = 4

ANNI_SEMESTRI_COLORI = ['#c0a162','#62c099','#e2f451','#f45a63','#afdcdd','#9be873']

# Mapping
NOME_CORSO = {
    "CalcoloMatricialeeRicercaOperativaMFN0588-corsoA-B-CinsiemeFIGLI:VALEANCHEPERRICERCAOPERATIVAII8036EPERISTITUZIONIDICALCOLOMATRICIALEERICERCAOPERATIVA[MFN1473]": "CMRO",
    "MatematicaDiscretaINF0290corsoA-B-CinsiemeFIGLI:valeancheperMatematicaDiscreta(I8011-S8827)-": "MD",
    "LogicaINF0291corsoA+B+CinsiemeValeancheIstituzionidiLogicaMFN0984(Magistrale)+LogicaMatematica(anno2010)": "L",
    "ProgrammazioneI(MFN0582)corsoA-B-CinsiemeFIGLI:valeancheperProgrammazioneIelaboratorioI8003-S8829": "PROGI",
    "LinguaIngleseI(MFN0590)+inserirenotaFIGLI:valeancheIngleseII8017-S8822": "ING1",
    "ANALISIMATEMATICA-MFN0570corsoA-B-C(insieme)fIgli:valeancheperAnalisimatematicaI8013": "ANM",
    "ArchitetturadegliElaboratoriMFN0586corsoA+B+CseparatiFIGLI:valeancheArchitetturadeglielaboratori-I8001": "ARCELAB",
    "ProgrammazioneIIMFN0585-corsoAeB+Cinsieme,FIGLI:valeancheperI8005-S8830-": "PROGII",
    "ElementidiprobabilitàestatisticaMFN0600corsoAeBinsiemeFigli:valeancheCPSI8023-S8813estatisticaI8035": "ESP",
    "SistemiOperativiMFN0601corsoAecorsoBseparati": "SO",
    "LinguaggiFormalieTraduttori–codiceMFN0603Figli:valeancheperLinguaggieAmbientidiProgrammazione(I8002)eLinguaggidiProgrammazione,I8033valeancheperlamagistralemfn0985,istituzionidilinguaggiformali": "LFT",
    "AlgoritmiestruttureDatiMFN0597CorsoAeBinsiemeFigli:valeancheAlgoritmieSperimentazioniI8031-S8841,AlgoritmieLaboratorioI8018-S8840+INF0211IstituzionidiAlgoritmi(magistrale)": "ASD",
    "BasidatiAeBconprenotazioneseparataMFN0602Figli:valeancheperI8032BasididatiesperimentazioniI8019BasididatielaboratoriovaleanchepermagistraleMFN1476e1477": "DB",
    "EconomiaeGestionedell'ImpresaeDiritto/Mfn0604-PARTEDIECONOMIA-FIGLI:ECONOMIAEGESTIONEDELLEIMPRESEI8037+(corsoperimatematici?)": "EGI",
    "EconomiaeGestionedell'ImpresaeDiritto/Mfn0604PARTEDIDIRITTO": "Privacy",
    "MFN0598FisicacorsoAeBseparatoFIGLI:valeancheperFisicaI8022": "Fisica",
    "ECONOMIAEGESTIONEdell'innovazionemfn0617Figli:organizzazioneedesperienzed'impresaI8048": "EGIN",
    "MFN0608InterazioneUomoMacchinaeTecnologieWeb": "TWEB(IUM)",
    "MFN1353InterazioneUomoMacchinaFIGLI:valeancheI8040-S8819InterazioneUomoMacchinaMFN0986IstituzionidiInterazioneUomoMacchina": "IUM",
    "SistemiInformativi MFN0618FIGLI:valeancheperI8042-S8836SistemiInformativi+ScienzeStatistiche,EconomicheeManageriali": "SISINF",
    "TecnologieWebMFN0634FIGLI:valeancheperLaboratoriodiapplicazionidiRetiI8115": "TWEB",
    "LinguaggieParadigmidiProgrammazione(MFN0610)FIGLI:valeancheperLinguaggieParadigmidiProgrammazioneMFN1354": "LPP",
    "CalcolabilitàecomplessitaINF0090valeancheperCalcolabilitàeComplessitàA(MFN0612)+Corsodi CalcolabilitàeComplessitàB(MFN0939)+esamemagistraledimatematicaMFN0579progettoeanalisidiAlgoritmi": "CEC",
    "ProgrammazioneIII-MFN0605FIGLI:valeancheIstituzionidiprogrammazionedistribuitainrete-LaureaMagistrale-MFN0988eeProgrammazioneinReteelaboratorioI8039": "PROGIII",
    "RetiIMFN1362FIGLI:valeancheperRetieSistemiDistribuiti.I8038-S8833": "RETI",
    "Metodiformalidell'informaticamfn0633FIGLI:valeancheperFondamentidell'InformaticaI8021+INF0190(parteA)": "MDF",
    "LOGICAPERL'INFORMATICAINF0003valeancheperLMInf0102": "LPF",
    "Storiadell'informaticaINF0004+esameperquellidelDAMS+INF0212ISTITUZIONIDISTORIA(MAGISTRALE)+INF0233": "SDI",
    "RETIDIELABORATORI,MFN0635FIGLI:valeancheperA.A2009RetidiTrasmissione(da6CFU)codiceI8117": "RDELAB",
    "SISTEMIINTELLIGENTImfn0607FIGLI:valeancheSistemiIntelligenti(haduecodiciunoperlatriennaleI8041l'altroperlamagistrale)+mettereistituzionidiSistemiIntelligentiMFN0987": "SISINT",
    "SicurezzaMFN0636FIGLI:SicurezzaI8028+sicurezzaImfn0945+INF0099(LM)": "SIC",
    "Sviluppodelleapplicazionisoftware,codicedelmfn0606FIGLI:valeancheperSperimentazionidiIngegneriadelSoftware,I8056-S8400eperISTITUZIONIDISVILUPPOSOFTWARE[MFN0989])magistrale": "SAS"
}
NOME_CORSO_STRONG = {
    "Calcolo Matriciale e Ricerca Operativa": "CMRO",
    "Matematica Discreta": "MATE DISC",
    "Logica": "LOG",
    "Programmazione I": "PROG I",
    "Lingua Inglese I": "ING 1",
    "ANALISI MATEMATICA": "ANALISI",
    "Architettura degli Elaboratori": "ARCH. ELAB",
    "Programmazione II": "PROG II",
    "Elementi di probabilità e statistica": "ELEM. PROB.",
    "Sistemi Operativi": "SIS. OPERATIVI",
    "Linguaggi Formali e Traduttori": "LFT",
    "Algoritmi e strutture Dati": "ALG STRUT. DATI",
    "Basi dati": "BASI DATI",
    "PARTE DIE CONOMIA": "EGI",
    "PARTE DI DIRITTO": "PRIVACY",
    "Fisica": "FISICA",
    "ECONOMIA E GESTIONE dell'innovazione": "EGIN",
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

