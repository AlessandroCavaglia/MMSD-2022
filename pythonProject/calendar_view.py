import calendar
from datetime import datetime

def main():
    year = 2023
    month = 6
    calendarz=calendar.month(year, month)

    calendarz=calendarz.replace("\n"," \n ")
    calendarz=edit_calendar(calendarz,datetime.strptime("08/06/2023", '%d/%m/%Y'),'1')
    calendarz=edit_calendar(calendarz,datetime.strptime("08/06/2023", '%d/%m/%Y'),'1')


    print(calendarz)


def edit_calendar(calendar,data,semestre):
    day=data.day
    day_str=" "+str(day)+" "
    index = calendar.find(day_str)
    if index<0:
        return calendar
    scostamento=3
    if(day>=10):
        scostamento=4
    if(semestre=='1'):
        calendar = calendar[:index] + " "+'\033[92m' + str(day)+ '\033[0m'+" " + calendar[index + scostamento:]
    else:
        calendar = calendar[:index] + " "+'\033[93m' + str(day) + '\033[0m'+" " + calendar[index +scostamento:]
    return calendar

if __name__ == '__main__':
    main()