# Header File: clocked_stats.py
# Display Clocked Stats For Habits in Ness App.
# History:
# Date    Programmer   - Description
# ---------- ---------- ----------------------------
# 05/04/2021     Ricardo Josue Colindres      - Created

from tkinter import *
from tkinter import ttk
from datetime import datetime
from data import ClockedSession
from database import DataBase
from styles import Styles


class ClockedStats:

    #! ******************************** Properties *******************************

    def __init__(self, master, username='ricardocolindres@me.com'):

        # Load User Info
        self.username = username

        self.myDataBase = DataBase(self.username)

        # Load User Info
        self.user_info = self.myDataBase.load()

        # ******************************** Main Window *******************************

        self.master = master
        self.master.title('Ness')
        self.master.resizable(False, False)
        self.master.geometry("700x500")
        self.master.configure(background='#fffff3')
        self.now = datetime.now()

        # Define grid 12 x 19
        master_rows = 0
        while master_rows < 11:
            self.master.rowconfigure(master_rows, minsize=45)
            master_rows += 1

        master_column = 0
        while master_column < 19:
            self.master.columnconfigure(master_column, minsize=37)
            master_column += 1

        # ******************************** Define Styles *******************************

        self.s = Styles()

        # ******************************** Define Frames *******************************

        # *Welcome Frame Construction ------------------------------

        self.frame_clockedstats_header = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_clockedstats_header.grid(
            row=0, column=0, rowspan=3, columnspan=19)

        # Define grid 3 x 19
        clockedstats_header_rows = 0
        while clockedstats_header_rows < 3:
            self.frame_clockedstats_header.rowconfigure(
                clockedstats_header_rows, minsize=45)
            clockedstats_header_rows += 1

        clockedstats_header_column = 0
        while clockedstats_header_column < 19:
            self.frame_clockedstats_header.columnconfigure(
                clockedstats_header_column, minsize=37)
            clockedstats_header_column += 1

        # *Top1 Frame Construction ------------------------------

        self.frame_clockedstats_subheader = ttk.Frame(
            self.master, relief=FLAT, style='Pink.TFrame')
        self.frame_clockedstats_subheader.grid(
            row=3, column=0, rowspan=1, columnspan=19)

        # Define grid 1 x 19
        clocked_subheader_row = 0
        while clocked_subheader_row < 1:
            self.frame_clockedstats_subheader.rowconfigure(
                clocked_subheader_row, minsize=45)
            clocked_subheader_row += 1

        clocked_subheader_column = 0
        while clocked_subheader_column < 19:
            self.frame_clockedstats_subheader.columnconfigure(
                clocked_subheader_column, minsize=38.5)
            clocked_subheader_column += 1

        # *Panel Header1 Frame Construction ------------------------------

        self.frame_clockedstats_panelheader = ttk.Frame(
            self.master, relief=FLAT, style='Yellow.TFrame')
        self.frame_clockedstats_panelheader.grid(
            row=4, column=0, rowspan=1, columnspan=19)

        # Define grid 1 x 19
        clockedhabits_panelheader_row = 0
        while clockedhabits_panelheader_row < 1:
            self.frame_clockedstats_panelheader.rowconfigure(
                clockedhabits_panelheader_row, minsize=45)
            clockedhabits_panelheader_row += 1

        clockedhabits_panelheader_column = 0
        while clockedhabits_panelheader_column < 19:
            self.frame_clockedstats_panelheader.columnconfigure(
                clockedhabits_panelheader_column, minsize=37)
            clockedhabits_panelheader_column += 1

        # * Panel Frame Construction ------------------------------

        self.frame_clockedstats_panel = ttk.Frame(
            self.master, relief=FLAT, style='Yellow.TFrame')
        self.frame_clockedstats_panel.config()
        self.frame_clockedstats_panel.grid(
            row=5, column=0, rowspan=6, columnspan=19)

        # Define grid 6 x 19
        clockedstats_panel_row = 0
        while clockedstats_panel_row < 6:
            self.frame_clockedstats_panel.rowconfigure(
                clockedstats_panel_row, minsize=45)
            clockedstats_panel_row += 1

        clockedstats_panel_column = 0
        while clockedstats_panel_column < 19:
            self.frame_clockedstats_panel.columnconfigure(
                clockedstats_panel_column, minsize=38.5)
            clockedstats_panel_column += 1

        # ******************************** Welcome Widgets Frames *******************************

        # Logo Display in the Welcome Section
        self.clockedstats_logo = PhotoImage(file='assets/main_logo-01.png')
        self.clockedstats_logo_2 = self.clockedstats_logo.subsample(4, 4)
        self.clockedstats_header_logo = ttk.Label(self.frame_clockedstats_header,
                                                  image=self.clockedstats_logo_2,
                                                  style='Header.TLabel')

        # Welcome Label
        self.manage_hearder_label = ttk.Label(self.frame_clockedstats_header,
                                              text='Clocked Habits Stats',
                                              style='Header.TLabel')

        # Geometrtic Distribution
        self.clockedstats_header_logo.grid(
            row=0, column=5, rowspan=3, columnspan=2, sticky='e')
        self.manage_hearder_label.grid(
            row=1, column=8, rowspan=1, columnspan=5, sticky='w')

        # ******************************** Top1 Frames *******************************

        # Labels Top1
        self.seession_header_label = ttk.Label(self.frame_clockedstats_subheader,
                                               text='My Sessions: ',
                                               style='WhiteOnPink.TLabel',
                                               anchor=CENTER)

        # Labels Top1
        self.seession_header2_label = ttk.Label(self.frame_clockedstats_subheader,
                                                text="Session's Data",
                                                style='WhiteOnPink.TLabel',
                                                anchor=CENTER)

        # Clean Session Data
        self.user_info['work_habits_data'] = [
            x for x in self.user_info['work_habits_data'] if len(x) > 1]
        self.user_info['work_habits_data'] = self.user_info['work_habits_data'][-10:]
        self.myDataBase.update(self.user_info)

        # Session Combobox
        self.sessions_available = []
        max_sessions = 0
        for session in reversed(self.user_info['work_habits_data']):
            if max_sessions < 11:
                self.sessions_available.append(session[0])
            max_sessions += 1

        self.selected_session = StringVar()
        if len(self.sessions_available) > 0:
            self.selected_session.set(self.sessions_available[0])
        self.session_combobox = ttk.Combobox(
            self.frame_clockedstats_subheader, textvariable=self.selected_session, width=20)

        self.session_combobox.config(values=self.sessions_available)
        self.current_session = self.selected_session.get()

        # Geometrtic Distribution
        self.seession_header_label.grid(
            row=0, column=2, rowspan=1, columnspan=3, sticky='')
        self.session_combobox.grid(
            row=0, column=5, rowspan=1, columnspan=5, sticky='we')
        self.seession_header2_label.grid(
            row=0, column=12, rowspan=1, columnspan=3, sticky='')

        # ******************************** Info1 Frames *******************************

        # 1 Label
        self.first_label_manage = ttk.Label(
            self.frame_clockedstats_panelheader, text='Habit Name', style='PinkOnYellow.TLabel', anchor=CENTER)

        # 2 Label
        self.second_label_manage = ttk.Label(
            self.frame_clockedstats_panelheader, text='Frecuency', style='PinkOnYellow.TLabel', anchor=CENTER)

        # 3 Label
        self.third_label_manage = ttk.Label(
            self.frame_clockedstats_panelheader, text='Time Elapsed', style='PinkOnYellow.TLabel', anchor=CENTER)

        # 4 Label
        self.fourth_label_manage = ttk.Label(
            self.frame_clockedstats_panelheader, text='Target Goal', style='PinkOnYellow.TLabel', anchor=CENTER)

        # 5 Label
        self.fifth_label_manage = ttk.Label(
            self.frame_clockedstats_panelheader, text='Achived Goal', style='PinkOnYellow.TLabel', anchor=CENTER)

        # Geometrtic Distribution
        self.first_label_manage.grid(row=0, column=1, rowspan=1,
                                     columnspan=3, sticky='')
        self.second_label_manage.grid(row=0, column=5, rowspan=1,
                                      columnspan=2, sticky='')
        self.third_label_manage.grid(row=0, column=8, rowspan=1,
                                     columnspan=2, sticky='')
        self.fourth_label_manage.grid(row=0, column=11, rowspan=1,
                                      columnspan=2, sticky='')
        self.fifth_label_manage.grid(row=0, column=14, rowspan=1,
                                     columnspan=2, sticky='')

       # ******************************** Panel Frames *******************************

        self.session_data = []
        if len(self.sessions_available) > 0:
            self.ALL_SESSION_DATA = ClockedSession(
                (self.selected_session.get()), (self.user_info['work_habits_data']))
            self.session_data = self.ALL_SESSION_DATA.listed_data()

        if len(self.session_data) > 0:

            self.labels_clockedstats = []
            self.internal_counter = 0
            self.clocked_habit_counter = 0
            for item in self.session_data:

                if self.clocked_habit_counter == 0:
                    style = 'BoldTextOnGreen.TLabel'

                    self.labels_clockedstats.append(ttk.Label(
                        self.frame_clockedstats_panel, style='WhiteOnGreen.TLabel'))
                    self.labels_clockedstats[self.internal_counter].grid(
                        row=self.clocked_habit_counter, column=0, columnspan=19, sticky='nesw')
                    self.internal_counter += 1

                elif (self.clocked_habit_counter % 2) == 0:
                    style = 'BoldTextOnGreen.TLabel'

                    self.labels_clockedstats.append(ttk.Label(
                        self.frame_clockedstats_panel, style='WhiteOnGreen.TLabel'))
                    self.labels_clockedstats[self.internal_counter].grid(
                        row=self.clocked_habit_counter, column=0, columnspan=19, sticky='nesw')
                    self.internal_counter += 1

                else:
                    style = 'BoldTextOnYellow.TLabel'

                # Label 1 (Habit Name)
                label1_text = item[0]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label1_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=1, columnspan=3)
                self.internal_counter += 1

                # Label 2 (Frecuency)
                label2_text = item[1]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label2_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=5, columnspan=2)
                self.internal_counter += 1

                # Label 3 (Time Elapsed)
                label3_text = item[2]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label3_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=8, columnspan=2)
                self.internal_counter += 1

                # Label 4 (Target Goal)
                label4_text = item[3]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label4_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=11, columnspan=2)
                self.internal_counter += 1

                # Label 5 (Achived Goal)
                label5_text = item[4]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label5_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=14, columnspan=2)
                self.internal_counter += 1

                self.clocked_habit_counter += 1

        # Info
        self.info_label = ttk.Label(self.frame_clockedstats_panel,
                                    text='Only data from your last 10 sessions is stored.',
                                    style='TextOnYellow.TLabel')
        self.info_label.grid(row=5, column=0, columnspan=19)

        self.update_clockedhabit_panel()

    #! ******************************** Methods *******************************

    def update_clockedhabit_panel(self):
        ''' This method updates the clocked habit information panel when the user 
        selects a new session. The function observes the selected_session paremeter 
        and if it has changed, it updates the info to the newly selected session.
        The method waits 0.5 seconds and calls itself again, repeating the
        process previously describe'''

        if self.selected_session.get() != self.current_session:

            for item in self.labels_clockedstats:
                item.destroy()

            # ******************************** Panel Frames *******************************
            self.session_data = []
            self.ALL_SESSION_DATA = ClockedSession(
                (self.selected_session.get()), (self.user_info['work_habits_data']))
            self.session_data = self.ALL_SESSION_DATA.listed_data()

            self.labels_clockedstats = []
            self.internal_counter = 0
            self.clocked_habit_counter = 0

            for item in self.session_data:

                if self.clocked_habit_counter == 0:
                    style = 'BoldTextOnGreen.TLabel'

                    self.labels_clockedstats.append(ttk.Label(
                        self.frame_clockedstats_panel, style='WhiteOnGreen.TLabel'))
                    self.labels_clockedstats[self.internal_counter].grid(
                        row=self.clocked_habit_counter, column=0, columnspan=19, sticky='nesw')
                    self.internal_counter += 1

                elif (self.clocked_habit_counter % 2) == 0:
                    style = 'BoldTextOnGreen.TLabel'

                    self.labels_clockedstats.append(ttk.Label(
                        self.frame_clockedstats_panel, style='WhiteOnGreen.TLabel'))
                    self.labels_clockedstats[self.internal_counter].grid(
                        row=self.clocked_habit_counter, column=0, columnspan=19, sticky='nesw')
                    self.internal_counter += 1

                else:
                    style = 'BoldTextOnYellow.TLabel'

                # Label 1 (Habit Name)
                label1_text = item[0]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label1_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=1, columnspan=3)
                self.internal_counter += 1

                # Label 2 (Frecuency)
                label2_text = item[1]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label2_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=5, columnspan=2)
                self.internal_counter += 1

                # Label 3 (Time Elapsed)
                label3_text = item[2]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label3_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=8, columnspan=2)
                self.internal_counter += 1

                # Label 4 (Target Goal)
                label4_text = item[3]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label4_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=11, columnspan=2)
                self.internal_counter += 1

                # Label 5 (Achived Goal)
                label5_text = item[4]
                self.labels_clockedstats.append(ttk.Label(
                    self.frame_clockedstats_panel, text=label5_text, style=style, anchor=CENTER))
                self.labels_clockedstats[self.internal_counter].grid(
                    row=self.clocked_habit_counter, column=14, columnspan=2)
                self.internal_counter += 1

                self.clocked_habit_counter += 1

            # Info
            self.info_label = ttk.Label(self.frame_clockedstats_panel,
                                        text='Only data from your last 10 sessions is stored.',
                                        style='TextOnYellow.TLabel')
            self.info_label.grid(row=5, column=0, columnspan=19)
            self.current_session = self.selected_session.get()

        self.master.after(500, self.update_clockedhabit_panel)
