# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import xlrd as x
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

df = pd.read_excel('input/Calendario_ESAMI_Triennali__ESTATE_2022-2.xls')
print(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
