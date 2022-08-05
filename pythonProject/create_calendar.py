from calendar_view.calendar import Calendar
from calendar_view.core.event import EventStyles
from calendar_view.calendar import Calendar
from calendar_view.config import style
from calendar_view.core import data
from calendar_view.core.event import Event

config = data.CalendarConfig(
    lang='en',
    title='Massage. Antonio',
    dates='2022-06-06 - 2022-06-30',
    show_year=True,
    title_vertical_align='top'
)

def build_calendar(exams, laboratori, aule, model, sessioni):
    calendar = Calendar.build(config)
    calendar.add_event(day='2022-06-22', start='00:00', end='23:59',  style=EventStyles.GRAY)
    calendar.add_event(day='2022-06-23', start='00:00', end='23:59',  style=EventStyles.RED)
    #calendar.add_event(day_of_week=5, start='09:00', end='12:00', style=EventStyles.RED)
    #calendar.add_event(day_of_week=5, start='10:00', end='13:00', style=EventStyles.BLUE)
    #calendar.add_event(day_of_week=6, start='15:00', end='18:00')
    calendar.save("output/simple_view.png")
    return


if __name__ == '__main__':
    build_calendar('','','','','')