#This file parsing the xlsx input
# AULE (Nome,Indisponibilità)
# LABORATORI (Nome,Indisponibilità)
# SESSIONE (Nome, DataInizio, DataFine)
# ESAME(

import pandas as pd

aule_df = pd.read_excel('input/input modello.xlsx',sheet_name='Input generali 2.0',skiprows=1,usecols=[4,5])
laboratorio_df = pd.read_excel('input/input modello.xlsx',sheet_name='Input generali 2.0',skiprows=1,usecols=[7,8])
sessione_df = pd.read_excel('input/input modello.xlsx',sheet_name='Input generali 2.0',skiprows=1,usecols=[1,2])
print(aule_df,laboratorio_df,sessione_df)