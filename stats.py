# Header File: stats.py
# Display Stats For Habits in Ness App.
# History:
# Date    Programmer   - Description
# ---------- ---------- ----------------------------
# 05/04/2021     Ricardo Josue Colindres      - Created

from tkinter import *
from tkinter import ttk
from datetime import datetime
from data import Data, General
from database import DataBase
from styles import Styles


class Stats:

    #! ******************************** Properties *******************************

    def __init__(self, master, username='ricardocolindres@me.com'):

        self.username = username

        self.myDataBase = DataBase(self.username)

        # Load User Info
        self.user_info = self.myDataBase.load()

        # ******************************** Main Window *******************************

        self.master = master
        self.master.title('Ness')
        # self.master.iconbitmap(icon_image)
        self.master.resizable(False, False)
        self.master.geometry("760x665")
        self.master.configure(background='#fffff3')
        self.now = datetime.now()

        # Define grid 21 x 19
        master_rows = 0
        while master_rows < 21:
            self.master.rowconfigure(master_rows, minsize=31.5)
            master_rows += 1

        master_column = 0
        while master_column < 19:
            self.master.columnconfigure(master_column, minsize=40)
            master_column += 1

        # ******************************** Define Styles *******************************

        self.s = Styles()

        # ******************************** Define Frames *******************************

        # *Welcome Frame Construction ------------------------------

        self.frame_stats_header = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_stats_header.grid(row=0, column=0, rowspan=4, columnspan=19)

        # Define grid 4 x 19
        logo_rows = 0
        while logo_rows < 4:
            self.frame_stats_header.rowconfigure(logo_rows, minsize=31.5)
            logo_rows += 1

        logo_column = 0
        while logo_column < 19:
            self.frame_stats_header.columnconfigure(logo_column, minsize=40)
            logo_column += 1

        # *Top1 Frame Construction ------------------------------

        self.frame_stats_subheader = ttk.Frame(
            self.master, relief=FLAT, style='Pink.TFrame')
        self.frame_stats_subheader.grid(
            row=4, column=0, rowspan=2, columnspan=19)

        # Define grid 2 x 19
        stats_subheader_row = 0
        while stats_subheader_row < 2:
            self.frame_stats_subheader.rowconfigure(
                stats_subheader_row, minsize=31.5)
            stats_subheader_row += 1

        stats_subheader_column = 0
        while stats_subheader_column < 19:
            self.frame_stats_subheader.columnconfigure(
                stats_subheader_column, minsize=40)
            stats_subheader_column += 1

        # *Info Panel 1 Frame Construction ------------------------------

        self.frame_habit_data = ttk.Frame(
            self.master, relief=FLAT, style='Yellow.TFrame')
        self.frame_habit_data.grid(row=6, column=0, rowspan=6, columnspan=19)

        # Define grid 1 x 19
        habit_data_row = 0
        while habit_data_row < 6:
            self.frame_habit_data.rowconfigure(habit_data_row, minsize=31.5)
            habit_data_row += 1

        habit_data_column = 0
        while habit_data_column < 19:
            self.frame_habit_data.columnconfigure(
                habit_data_column, minsize=40)
            habit_data_column += 1

        # *Info Panel 2 Frame Construction ------------------------------

        self.frame_general_data = ttk.Frame(
            self.master, relief=FLAT, style='Maron.TFrame')
        self.frame_general_data.grid(
            row=12, column=0, rowspan=9, columnspan=19)

        # Define grid 8 x 19
        general_data_row = 0
        while general_data_row < 9:
            self.frame_general_data.rowconfigure(
                general_data_row, minsize=31.5)
            general_data_row += 1

        general_data_column = 0
        while general_data_column < 19:
            self.frame_general_data.columnconfigure(
                general_data_column, minsize=40)
            general_data_column += 1

        # ******************************** Welcome Widgets Frames *******************************

        # Logo Display in the Welcome Section
        self.stats_logo = PhotoImage(file='assets/main_logo-01.png')
        self.stats_logo_resampled = self.stats_logo.subsample(4, 4)
        self.stats_logo_label = ttk.Label(self.frame_stats_header,
                                          image=self.stats_logo_resampled,
                                          style='Header.TLabel')

        # Welcome Label
        self.stats_header_label = ttk.Label(self.frame_stats_header,
                                            text='Your Stats',
                                            style='Header.TLabel')

        # Geometrtic Distribution
        self.stats_logo_label.grid(row=0, column=6, rowspan=4, columnspan=3)
        self.stats_header_label.grid(
            row=1, column=9, rowspan=2, columnspan=5, sticky='w')

        # ******************************** Top1 Frames *******************************

        # Select Habit Label
        self.select_habit_label = ttk.Label(self.frame_stats_subheader,
                                            text='Your Habits:',
                                            style='WhiteOnPink.TLabel',
                                            anchor="center")

        # Habit Combobox
        self.habits_available = []
        for habit in self.user_info['user_habits']:
            self.habits_available.append(habit[0])

        self.selected_habit = StringVar()
        if len(self.habits_available) > 0:
            self.selected_habit.set(self.habits_available[0])
        self.habit_combobox = ttk.Combobox(
            self.frame_stats_subheader, textvariable=self.selected_habit, width=20)

        self.habit_combobox.config(values=self.habits_available)

        # Active Habit Label
        self.active_habit_label = ttk.Label(self.frame_stats_subheader,
                                            text='No Habit Selected',
                                            style='WhiteOnPink.TLabel',
                                            anchor="center")
        if len(self.habits_available) > 0:
            self.active_habit_label.config(text=self.habits_available[0])

        # Geometrtic Distribution
        self.select_habit_label.grid(
            row=0, column=1, rowspan=2, columnspan=3, sticky='')
        self.habit_combobox.grid(
            row=0, column=4, rowspan=2, columnspan=6, sticky='')
        self.active_habit_label.grid(
            row=0, column=12, rowspan=2, columnspan=4, sticky='')

        # ******************************** Info1 Frames *******************************\

        # Define all Data related to the first habit in the list of sleceted habits
        self.current_habit = self.selected_habit.get()

        self.streak_variable = StringVar()
        self.streak_variable.set('')
        self.historical_streak_variable = StringVar()
        self.historical_streak_variable.set('Historical Best: 0')

        self.week_variable = StringVar()
        self.week_variable.set('')
        self.likely_day = StringVar()
        self.likely_day.set('')
        self.less_likely_day = StringVar()
        self.less_likely_day.set('')

        # If any habit exits, pick first in list and run it
        if self.selected_habit.get() != '':

            self.data_list = []
            for i, v in enumerate(self.user_info['user_habits_streak']):
                if v[0] == self.selected_habit.get():
                    self.data_list = self.user_info['user_habits_streak'][i]
                    break

            self.habit_data = []
            self.habit_datta_index = 0
            self.historical_best_observed = 0
            for i, v in enumerate(self.user_info['user_habits']):
                if v[0] == self.selected_habit.get():
                    self.habit_data = self.user_info['user_habits'][i]
                    self.historical_best_observed = self.user_info['user_habits'][i][4]
                    self.habit_datta_index = i
                    break

            self.ALL_HABIT_DATA = Data(self.data_list, self.habit_data)

            # Get Data
            self.streak_information = self.ALL_HABIT_DATA.active_streak()
            self.likelyhood_habit = self.ALL_HABIT_DATA.probability()

            # Actual Streak
            self.streak_variable.set(self.streak_information[0])

            # Complete weeks with perfect Streak
            self.week_variable.set(self.streak_information[1])

            # Get most likely days for the habit's completion
            self.likely_day.set(self.likelyhood_habit[0])

            # Get less likely days for the habit's completion
            self.less_likely_day.set(self.likelyhood_habit[1])

            # Get best historical habit

            if self.streak_information[0] > self.historical_best_observed:
                self.user_info['user_habits'][self.habit_datta_index][4] = self.streak_information[0]
                self.historical_streak_variable.set(
                    'Historical Best: ' + str(self.streak_information[0]))

                # Update DataBase
                self.myDataBase.update(self.user_info)

            else:
                self.historical_streak_variable.set(
                    'Historical Best: ' + str(self.historical_best_observed))

        # ? *****************************************************SubFrame 1
        self.frame_streak = ttk.Frame(
            self.frame_habit_data, relief=FLAT, style='TFrame')
        self.frame_streak.grid(row=0, column=0, rowspan=6, columnspan=5)

        # Define grid 6 x 5
        streak_row = 0
        while streak_row < 6:
            self.frame_streak.rowconfigure(streak_row, minsize=31.5)
            streak_row += 1

        streak_column = 0
        while streak_column < 5:
            self.frame_streak.columnconfigure(streak_column, minsize=40)
            streak_column += 1

        # **************************Construction SubFrame 1

        # Streak Image
        self.streak_image = PhotoImage(file='assets/ok_streak-01.png')
        self.streak_image_resampled = self.streak_image.subsample(5, 5)
        self.streak_image_label = ttk.Label(self.frame_streak,
                                            image=self.streak_image_resampled,
                                            style='Header.TLabel')

        # Streak Label
        self.streak_data_label = ttk.Label(self.frame_streak,
                                           textvariable=self.streak_variable,
                                           style='PinkOnWhiteLarge.TLabel')

        # Streak Texk Label
        self.streak_text_label = ttk.Label(self.frame_streak,
                                           text='STREAK',
                                           style='BlackOnWhite.TLabel')

        # Streak Texk Label
        self.streak_historical_label = ttk.Label(self.frame_streak,
                                                 textvariable=self.historical_streak_variable,
                                                 style='BoldTextOnWhite.TLabel')

        # Geometrtic Distribution
        self.streak_image_label.grid(row=1, column=1, rowspan=3, columnspan=1)
        self.streak_data_label.grid(
            row=1, column=2, rowspan=2, columnspan=3, sticky='ws')
        self.streak_text_label.grid(
            row=3, column=2, rowspan=1, columnspan=2, sticky='wn')
        self.streak_historical_label.grid(
            row=4, column=0, rowspan=1, columnspan=5)

        # ? *****************************************************SubFrame 2
        self.frame_week = ttk.Frame(
            self.frame_habit_data, relief=FLAT, style='Blue.TFrame')
        self.frame_week.grid(row=0, column=5, rowspan=6, columnspan=5)

        # Define grid 6 x 5
        week_row = 0
        while week_row < 6:
            self.frame_week.rowconfigure(week_row, minsize=31.5)
            week_row += 1

        week_column = 0
        while week_column < 5:
            self.frame_week.columnconfigure(week_column, minsize=40)
            week_column += 1

        # **************************Construction SubFrame 2

        # Week Image
        self.week_image = PhotoImage(file='assets/ok_week-01.png')
        self.week_image_resampled = self.week_image.subsample(5, 5)
        self.week_image_label = ttk.Label(self.frame_week,
                                          image=self.week_image_resampled,
                                          style='WhiteOnBlue.TLabel')

        # Week Label
        self.week_data_label = ttk.Label(self.frame_week,
                                         textvariable=self.week_variable,
                                         style='WhiteOnBlueLarge.TLabel')

        # Week Texk Label
        self.week_text_label = ttk.Label(self.frame_week,
                                         text='WEEKS',
                                         style='WhiteOnBlue.TLabel')

        # Week Sub Texk Label
        self.week_subtext_label = ttk.Label(self.frame_week,
                                            text='Complete Weeks',
                                            style='WhiteOnBlue.TLabel')

        # Geometrtic Distribution
        self.week_image_label.grid(row=1, column=1, rowspan=3, columnspan=1)
        self.week_data_label.grid(
            row=1, column=2, rowspan=2, columnspan=3, sticky='ws')
        self.week_text_label.grid(
            row=3, column=2, rowspan=1, columnspan=2, sticky='wn')
        self.week_subtext_label.grid(
            row=4, column=0, rowspan=1, columnspan=5)

        # ? *****************************************************SubFrame 3
        self.frame_probability = ttk.Frame(
            self.frame_habit_data, relief=FLAT, style='Yellow.TFrame')
        self.frame_probability.grid(row=0, column=10, rowspan=6, columnspan=9)

        # Define grid 6 x 9
        probability_row = 0
        while probability_row < 6:
            self.frame_probability.rowconfigure(probability_row, minsize=31.5)
            probability_row += 1

        probability_column = 0
        while probability_column < 9:
            self.frame_probability.columnconfigure(
                probability_column, minsize=40)
            probability_column += 1

        # **************************Construction SubFrame 3

        # Likely Image
        self.likely_image = PhotoImage(file='assets/ok_calendar-01.png')
        self.likely_image_resampled = self.likely_image.subsample(5, 5)
        self.likely_image_label = ttk.Label(self.frame_probability,
                                            image=self.likely_image_resampled,
                                            style='PinkOnYellow.TLabel')

        # Likely Label
        self.likely_data_label = ttk.Label(self.frame_probability,
                                           textvariable=self.likely_day,
                                           style='PinkOnYellow.TLabel')

        # Likely Texk Label
        self.likely_text_label = ttk.Label(self.frame_probability,
                                           text='More Likely To Complete On:',
                                           style='BoldTextOnYellow.TLabel')

        # Less Likely Image
        self.less_likely_image = PhotoImage(
            file='assets/ok_notcalendar-01.png')
        self.less_likely_resampled = self.less_likely_image.subsample(5, 5)
        self.less_likely_label = ttk.Label(self.frame_probability,
                                           image=self.less_likely_resampled,
                                           style='PinkOnYellow.TLabel')

        # Less likely Label
        self.less_likely_data_label = ttk.Label(self.frame_probability,
                                                textvariable=self.less_likely_day,
                                                style='PinkOnYellow.TLabel')

        # Lees Likely Texk Label
        self.less_likely_text_label = ttk.Label(self.frame_probability,
                                                text='Less Likely To Complete On:',
                                                style='BoldTextOnYellow.TLabel')

        # Geometrtic Distribution
        self.likely_image_label.grid(row=1, column=1, rowspan=2, columnspan=2)
        self.likely_text_label.grid(
            row=1, column=3, rowspan=1, columnspan=5, sticky='ws')
        self.likely_data_label.grid(
            row=2, column=3, rowspan=1, columnspan=5, sticky='w')
        self.less_likely_label.grid(row=3, column=1, rowspan=2, columnspan=2)
        self.less_likely_text_label.grid(
            row=3, column=3, rowspan=1, columnspan=5, sticky='ws')
        self.less_likely_data_label.grid(
            row=4, column=3, rowspan=1, columnspan=5, sticky='w')

        # ******************************** Info2 Frames *******************************

        # ? ******************************************* Update All Data Best Records
        if len(self.user_info['user_habits_streak']) > 0:
            for i, v in enumerate((self.user_info['user_habits'])):
                data_list = self.user_info['user_habits_streak'][i]
                habit_data = self.user_info['user_habits'][i]
                update_data = Data(data_list, habit_data)
                update_data = update_data.active_streak()
                if update_data[0] > self.user_info['user_habits'][i][4]:
                    self.user_info['user_habits'][i][4] = update_data[0]

        # Update DataBase
        self.myDataBase.update(self.user_info)

        # ? ************************************************ Define General Data

        self.GENERAL_DATA = General((self.user_info['user_habits']))
        self.general_information = self.GENERAL_DATA.highest_lowest()

        # **************************Construction Info 2

        # General Label
        self.general_header_label = ttk.Label(self.frame_general_data,
                                              text='General Data',
                                              style='WhiteOnGreen.TLabel',
                                              anchor=CENTER)

        # Likely Label
        self.highest_streak_label = ttk.Label(self.frame_general_data,
                                              text=self.general_information[0][1],
                                              style='PinkOnMaronLarge.TLabel',
                                              anchor=CENTER)

        # Likely Label
        self.highest_text_label = ttk.Label(self.frame_general_data,
                                            text=self.general_information[0][0],
                                            style='PinkOnMaronMedium.TLabel',
                                            anchor=CENTER)

        # Likely Label
        self.highest_textsub_label = ttk.Label(self.frame_general_data,
                                               text='Highest Streak',
                                               style='BlackOnMaronMedium.TLabel',
                                               anchor=CENTER)

        # Less Likely Label
        self.lowest_streak_label = ttk.Label(self.frame_general_data,
                                             text=self.general_information[1][1],
                                             style='PinkOnMaronLarge.TLabel',
                                             anchor=CENTER)

        # Less Likely Label
        self.lowest_text_label = ttk.Label(self.frame_general_data,
                                           text=self.general_information[1][0],
                                           style='PinkOnMaronMedium.TLabel',
                                           anchor=CENTER)

        # Less Likely Label
        self.lowest_textsub_label = ttk.Label(self.frame_general_data,
                                              text='Lowest Streak',
                                              style='BlackOnMaronMedium.TLabel',
                                              anchor=CENTER)

        # Background Label
        self.general_bakground_label = ttk.Label(
            self.frame_general_data, style='BlackOnWhite.TLabel')

        # Frequency Label
        self.general_frequency_label = ttk.Label(
            self.frame_general_data, text='Frequencies:', style='BoldTextOnWhite.TLabel')

        # Combobox for Birth Month
        self.mapped_frequencies = {'Weekly': 1, 'Daily': 7, 'Two Times per Week': 2,
                                   'Three Times per Week': 3, 'Four Times per Week': 4,
                                   'Five Times per Week': 5, 'Six Times per Week': 6}

        self.selected_frequency = StringVar()
        self.frequency_combobox = ttk.Combobox(
            self.frame_general_data, textvariable=self.selected_frequency, width=10)
        self.frequency_combobox.config(values=('Weekly', 'Daily', 'Two Times per Week',
                                               'Three Times per Week', 'Four Times per Week',
                                               'Five Times per Week', 'Six Times per Week'))
        self.selected_frequency.set('Weekly')
        self.current_frequency = self.selected_frequency.get()

        # Habit Label
        self.general_habit_label = ttk.Label(
            self.frame_general_data, text='Habits with Selected Frequency:', style='BoldTextOnWhite.TLabel')

        # Result Habit Label
        self.retreived_habits = StringVar()
        self.general_result_label = ttk.Label(
            self.frame_general_data, textvariable=self.retreived_habits, style='PinkOnWhite.TLabel')
        self.general_result_label.config(wraplength=150)

        self.habits_found = []
        for habit in self.user_info['user_habits']:
            if len(habit[2]) == 1:
                self.habits_found.append(habit[0])

        self.habits_found = ', '.join(self.habits_found)
        if self.habits_found == '':
            self.habits_found = 'None'
        self.retreived_habits.set(self.habits_found)

        # Geometrtic Distribution
        self.general_header_label.grid(
            row=0, column=0, rowspan=2, columnspan=19, sticky='nesw')
        self.highest_streak_label.grid(
            row=3, column=2, rowspan=2, columnspan=2, sticky='ws')
        self.highest_text_label.grid(
            row=5, column=2, rowspan=1, columnspan=3, sticky='w')
        self.highest_textsub_label.grid(
            row=6, column=2, rowspan=1, columnspan=3, sticky='wn')
        self.lowest_streak_label.grid(
            row=3, column=6, rowspan=2, columnspan=2, sticky='ws')
        self.lowest_text_label.grid(
            row=5, column=6, rowspan=1, columnspan=3, sticky='w')
        self.lowest_textsub_label.grid(
            row=6, column=6, rowspan=1, columnspan=3, sticky='wn')

        self.general_bakground_label.grid(
            row=2, column=10, rowspan=7, columnspan=9, sticky='news')
        self.general_frequency_label.grid(
            row=3, column=12, rowspan=1, columnspan=6, sticky='ws')
        self.frequency_combobox.grid(
            row=4, column=12, rowspan=1, columnspan=6, sticky='nesw')
        self.general_habit_label.grid(
            row=5, column=12, rowspan=1, columnspan=6, sticky='ws')
        self.general_result_label.grid(
            row=6, column=12, rowspan=2, columnspan=6, sticky='nw')

        self.update_habit_panel()
        self.update_general_panel()

    #! ******************************** Methods *******************************

    def update_habit_panel(self):
        ''' This method updates the habit information panel when the user 
        selects a new habit. The function observes the selected_habit paremeter 
        and if it has changed, it updates the info to the newly selected habit.
        The method waits 0.5 seconds and calls itself again, repeating the
        process previously describe'''

        if self.selected_habit.get() != self.current_habit:

            self.active_habit_label.config(text=self.selected_habit.get())

            self.frame_habit_data.destroy()

            # *Info Panel 1 Frame Construction ------------------------------

            self.frame_habit_data = ttk.Frame(
                self.master, relief=FLAT, style='Yellow.TFrame')
            self.frame_habit_data.grid(
                row=6, column=0, rowspan=6, columnspan=19)

            # Define grid 1 x 19
            habit_data_row = 0
            while habit_data_row < 6:
                self.frame_habit_data.rowconfigure(
                    habit_data_row, minsize=31.5)
                habit_data_row += 1

            habit_data_column = 0
            while habit_data_column < 19:
                self.frame_habit_data.columnconfigure(
                    habit_data_column, minsize=40)
                habit_data_column += 1

            # Define all Data related to the first habit in the list of sleceted habits

            self.data_list = []
            for i, v in enumerate(self.user_info['user_habits_streak']):
                if v[0] == self.selected_habit.get():
                    self.data_list = self.user_info['user_habits_streak'][i]
                    break

            self.habit_data = []
            self.habit_datta_index = 0
            self.historical_best_observed = 0
            for i, v in enumerate(self.user_info['user_habits']):
                if v[0] == self.selected_habit.get():
                    self.habit_data = self.user_info['user_habits'][i]
                    self.historical_best_observed = self.user_info['user_habits'][i][4]
                    self.habit_datta_index = i
                    break

            self.ALL_HABIT_DATA = Data(self.data_list, self.habit_data)

            # Get Data
            self.streak_information = self.ALL_HABIT_DATA.active_streak()
            self.likelyhood_habit = self.ALL_HABIT_DATA.probability()

            # Actual Streak
            self.streak_variable.set(self.streak_information[0])

            # Complete weeks with perfect Streak
            self.week_variable.set(self.streak_information[1])

            # Get most likely days for the habit's completion
            self.likely_day.set(self.likelyhood_habit[0])

            # Get less likely days for the habit's completion
            self.less_likely_day.set(self.likelyhood_habit[1])

            # Get best historical habit

            if self.streak_information[0] > self.historical_best_observed:
                self.user_info['user_habits'][self.habit_datta_index][4] = self.streak_information[0]
                self.historical_streak_variable.set(
                    'Historical Best: ' + str(self.streak_information[0]))

                # Update DataBase
                self.myDataBase.update(self.user_info)

            else:
                self.historical_streak_variable.set(
                    'Historical Best: ' + str(self.historical_best_observed))

            # ? *****************************************************SubFrame 1
            self.frame_streak = ttk.Frame(
                self.frame_habit_data, relief=FLAT, style='TFrame')
            self.frame_streak.grid(row=0, column=0, rowspan=6, columnspan=5)

            # Define grid 6 x 5
            streak_row = 0
            while streak_row < 6:
                self.frame_streak.rowconfigure(streak_row, minsize=31.5)
                streak_row += 1

            streak_column = 0
            while streak_column < 5:
                self.frame_streak.columnconfigure(streak_column, minsize=40)
                streak_column += 1

            # **************************Construction SubFrame 1

            # Streak Image
            self.streak_image = PhotoImage(file='assets/ok_streak-01.png')
            self.streak_image_resampled = self.streak_image.subsample(5, 5)
            self.streak_image_label = ttk.Label(self.frame_streak,
                                                image=self.streak_image_resampled,
                                                style='Header.TLabel')

            # Streak Label
            self.streak_data_label = ttk.Label(self.frame_streak,
                                               textvariable=self.streak_variable,
                                               style='PinkOnWhiteLarge.TLabel')

            # Streak Texk Label
            self.streak_text_label = ttk.Label(self.frame_streak,
                                               text='STREAK',
                                               style='BlackOnWhite.TLabel')

            # Streak Texk Label
            self.streak_historical_label = ttk.Label(self.frame_streak,
                                                     textvariable=self.historical_streak_variable,
                                                     style='BoldTextOnWhite.TLabel')

            # Geometrtic Distribution
            self.streak_image_label.grid(
                row=1, column=1, rowspan=3, columnspan=1)
            self.streak_data_label.grid(
                row=1, column=2, rowspan=2, columnspan=3, sticky='ws')
            self.streak_text_label.grid(
                row=3, column=2, rowspan=1, columnspan=2, sticky='wn')
            self.streak_historical_label.grid(
                row=4, column=0, rowspan=1, columnspan=5)

            # ? *****************************************************SubFrame 2
            self.frame_week = ttk.Frame(
                self.frame_habit_data, relief=FLAT, style='Blue.TFrame')
            self.frame_week.grid(row=0, column=5, rowspan=6, columnspan=5)

            # Define grid 6 x 5
            week_row = 0
            while week_row < 6:
                self.frame_week.rowconfigure(week_row, minsize=31.5)
                week_row += 1

            week_column = 0
            while week_column < 5:
                self.frame_week.columnconfigure(week_column, minsize=40)
                week_column += 1

            # **************************Construction SubFrame 2

            # Week Image
            self.week_image = PhotoImage(file='assets/ok_week-01.png')
            self.week_image_resampled = self.week_image.subsample(5, 5)
            self.week_image_label = ttk.Label(self.frame_week,
                                              image=self.week_image_resampled,
                                              style='WhiteOnBlue.TLabel')

            # Week Label
            self.week_data_label = ttk.Label(self.frame_week,
                                             textvariable=self.week_variable,
                                             style='WhiteOnBlueLarge.TLabel')

            # Week Texk Label
            self.week_text_label = ttk.Label(self.frame_week,
                                             text='WEEKS',
                                             style='WhiteOnBlue.TLabel')

            # Week Sub Texk Label
            self.week_subtext_label = ttk.Label(self.frame_week,
                                                text='Complete Weeks',
                                                style='WhiteOnBlue.TLabel')

            # Geometrtic Distribution
            self.week_image_label.grid(
                row=1, column=1, rowspan=3, columnspan=1)
            self.week_data_label.grid(
                row=1, column=2, rowspan=2, columnspan=3, sticky='ws')
            self.week_text_label.grid(
                row=3, column=2, rowspan=1, columnspan=2, sticky='wn')
            self.week_subtext_label.grid(
                row=4, column=0, rowspan=1, columnspan=5)

            # ? *****************************************************SubFrame 3
            self.frame_probability = ttk.Frame(
                self.frame_habit_data, relief=FLAT, style='Yellow.TFrame')
            self.frame_probability.grid(
                row=0, column=10, rowspan=6, columnspan=9)

            # Define grid 6 x 9
            probability_row = 0
            while probability_row < 6:
                self.frame_probability.rowconfigure(
                    probability_row, minsize=31.5)
                probability_row += 1

            probability_column = 0
            while probability_column < 9:
                self.frame_probability.columnconfigure(
                    probability_column, minsize=40)
                probability_column += 1

            # **************************Construction SubFrame 3

            # Likely Image
            self.likely_image = PhotoImage(file='assets/ok_calendar-01.png')
            self.likely_image_resampled = self.likely_image.subsample(5, 5)
            self.likely_image_label = ttk.Label(self.frame_probability,
                                                image=self.likely_image_resampled,
                                                style='PinkOnYellow.TLabel')

            # Likely Label
            self.likely_data_label = ttk.Label(self.frame_probability,
                                               textvariable=self.likely_day,
                                               style='PinkOnYellow.TLabel')

            # Likely Texk Label
            self.likely_text_label = ttk.Label(self.frame_probability,
                                               text='More Likely To Complete On:',
                                               style='BoldTextOnYellow.TLabel')

            # Less Likely Image
            self.less_likely_image = PhotoImage(
                file='assets/ok_notcalendar-01.png')
            self.less_likely_resampled = self.less_likely_image.subsample(5, 5)
            self.less_likely_label = ttk.Label(self.frame_probability,
                                               image=self.less_likely_resampled,
                                               style='PinkOnYellow.TLabel')

            # Less likely Label
            self.less_likely_data_label = ttk.Label(self.frame_probability,
                                                    textvariable=self.less_likely_day,
                                                    style='PinkOnYellow.TLabel')

            # Lees Likely Texk Label
            self.less_likely_text_label = ttk.Label(self.frame_probability,
                                                    text='Less Likely To Complete On:',
                                                    style='BoldTextOnYellow.TLabel')

            # Geometrtic Distribution
            self.likely_image_label.grid(
                row=1, column=1, rowspan=2, columnspan=2)
            self.likely_text_label.grid(
                row=1, column=3, rowspan=1, columnspan=5, sticky='ws')
            self.likely_data_label.grid(
                row=2, column=3, rowspan=1, columnspan=5, sticky='w')
            self.less_likely_label.grid(
                row=3, column=1, rowspan=2, columnspan=2)
            self.less_likely_text_label.grid(
                row=3, column=3, rowspan=1, columnspan=5, sticky='ws')
            self.less_likely_data_label.grid(
                row=4, column=3, rowspan=1, columnspan=5, sticky='w')

            # * Set new curernt_habit value
            self.current_habit = self.selected_habit.get()

        self.master.after(500, self.update_habit_panel)

    def update_general_panel(self):
        ''' This method updates the general information panel when the user 
        selects a new frequency. The function observes the selected_frequency 
        paremeter and if it has changed, it updates the info to the newly selected 
        frequency.The method waits 0.5 seconds and calls itself again, repeating the
        process previously describe'''

        if self.selected_frequency.get() != self.current_frequency:

            mapped_selected_frequency = 0
            for k, v in self.mapped_frequencies.items():
                if k == self.selected_frequency.get():
                    mapped_selected_frequency = v

            self.habits_found = []
            for v in self.user_info['user_habits']:
                if len(v[2]) == mapped_selected_frequency:
                    self.habits_found.append(v[0])

            self.habits_found = ', '.join(self.habits_found)
            if self.habits_found == '':
                self.habits_found = 'None'
            self.retreived_habits.set(self.habits_found)

            self.current_frequency = self.selected_frequency.get()

        self.master.after(500, self.update_general_panel)
