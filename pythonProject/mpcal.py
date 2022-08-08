import calendar
import os

import matplotlib.pyplot as plt

calendar.setfirstweekday(0) # Sunday is 1st day in US
w_days = 'Lun Mar Mer Gio Ven Sab Dom'.split()
m_names = '''
Gennaio Febbraio Marzo Aprile Maggio Giugno Luglio Agosto Settembre Ottobre Novembre Dicembre'''.split()



class MplCalendar(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.cal = calendar.monthcalendar(year, month)
        # A month of events are stored as a list of lists of list.
        # Nesting, from outer to inner, Week, Day, Event_str
        # Save the events data in the same format
        self.events = [[[] for day in week] for week in self.cal]

    def _monthday_to_index(self, day):
        for week_n, week in enumerate(self.cal):
            try:
                i = week.index(day)
                return week_n, i
            except ValueError:
                pass
         # couldn't find the day

    def add_event(self, day, event_str,color='white'):
        week, w_day = self._monthday_to_index(day)
        self.events[week][w_day].append((event_str,color))

    def _render(self, nome):
        'create the calendar figure'
        plot_defaults = dict(
            sharex=True,
            sharey=True,
            figsize=(11, 15),
            dpi=200,

        )
        plot_defaults.update()
        f, axs = plt.subplots(
            len(self.cal), 7,
            **plot_defaults
        )
        f.subplots_adjust(left=0.01, bottom=0.01, right=0.99, top=0.92, wspace=0, hspace=0)

        for week, ax_row in enumerate(axs):
            for week_day, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.cal[week][week_day] != 0:
                    ax.text(.02, .98,
                            str(self.cal[week][week_day]),
                            verticalalignment='top',
                            horizontalalignment='left')
                contents = self.events[week][week_day]
                for index,content in enumerate(contents):
                    text = ax.text(.04, .87-(0.135*index), content[0],
                                   verticalalignment='top',
                                   horizontalalignment='left',
                                   fontsize=9
                                   )
                    text.set_bbox(dict(facecolor=content[1], alpha=0.5, edgecolor='black'))

        # use the titles of the first row as the weekdays
        for n, day in enumerate(w_days):
            axs[0][n].set_title(day)

        # Place subplots in a close grid
        f.subplots_adjust(hspace=0)
        f.subplots_adjust(wspace=0)
        f.suptitle(nome.replace(".jpg","") + ' ' + str(self.year),
                   fontsize=20, fontweight='bold')

    def show(self,nome):
        self._render(nome)
        path = os.path.join('output', nome)
        plt.savefig(path)
        #plt.show()


    def save(self, filename, **kwargs):
        'save the calendar to the specified image file.'
        self._render(**kwargs)
        plt.savefig(filename)