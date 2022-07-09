# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
from datetime import datetime

import xlrd as x
import openpyxl as op
import pandas as pd
import Classes

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

#init aule
df = pd.read_excel('input/input modello.xlsx',skiprows=8, index_col=0, na_values=['string1', 'string2'],dtype={'Nome Aula': str, 'Date indisponibilità (Divise da ,)': datetime})
df = df.reset_index()
aule = []
for index, row in df.iterrows():
    if(row['Nome Aula']):
        aule.append(Classes.ExamRoom(row['Nome Aula'],row['Date indisponibilità (Divise da ,)']))
        print(row['Nome Aula'],row['Date indisponibilità (Divise da ,)'])

print(aule[5].indisponibilita)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
