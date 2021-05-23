# Header File: habits.py
# Main Habit Window for Ness.
# History:
# Date    Programmer   - Description
# ---------- ---------- ----------------------------
# 05/04/2021     Ricardo Josue Colindres      - Created

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from datetime import timedelta
from database import DataBase
from styles import Styles


class Habits:

    #! ******************************** Properties *******************************

    def __init__(self, master, username='ricardocolindres@me.com'):

        self.username = username

        self.myDataBase = DataBase(self.username)

        # Load User Info
        self.user_info = self.myDataBase.load()

        # ? ******************************** Master *******************************

        self.session = True

        self.master = master
        self.master.title('Ness')
        self.master.resizable(False, False)
        self.master.geometry("950x600")
        self.master.configure(background='white')
        self.now = datetime.now()

        # Define grid 12 x 20
        master_rows = 0
        while master_rows < 12:
            self.master.rowconfigure(master_rows, minsize=47.5)
            master_rows += 1

        master_column = 0
        while master_column < 20:
            self.master.columnconfigure(master_column, minsize=47.5)
            master_column += 1

        # ******************************** Define Styles *******************************

        self.s = Styles()

        # ? ******************************** Define Frames *******************************

        # *Welcome Frame Construction ------------------------------

        self.frame_welcome = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_welcome.grid(row=0, column=0, rowspan=2, columnspan=20)

        # Define grid 2 x 20
        welcome_rows = 0
        while welcome_rows < 2:
            self.frame_welcome.rowconfigure(welcome_rows, minsize=47.5)
            welcome_rows += 1

        welcome_column = 0
        while welcome_column < 20:
            self.frame_welcome.columnconfigure(welcome_column, minsize=47.5)
            welcome_column += 1

        # *Tab Button Frame Construction ------------------------------

        self.frame_tab = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_tab.grid(row=2, column=0, rowspan=1, columnspan=20)

        # Define grid 1 x 21
        tab_rows = 0
        while tab_rows < 1:
            self.frame_tab.rowconfigure(tab_rows, minsize=47.5)
            tab_rows += 1

        tab_column = 0
        while tab_column < 21:
            self.frame_tab.columnconfigure(tab_column, minsize=47.5)
            tab_column += 1

        # *Top1 Frame Construction ------------------------------

        self.frame_top1 = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_top1.grid(row=3, column=0, rowspan=1, columnspan=20)

        # Define grid 1 x 21
        top1_rows = 0
        while top1_rows < 1:
            self.frame_top1.rowconfigure(top1_rows, minsize=47.5)
            top1_rows += 1

        top1_column = 0
        while top1_column < 21:
            self.frame_top1.columnconfigure(top1_column, minsize=47.5)
            top1_column += 1

        # *Info Panel 1 Frame Construction ------------------------------

        self.frame_main_habits = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_main_habits.grid(row=4, column=0, rowspan=5, columnspan=10)

        # Define grid 7 x 16
        info1_row = 0
        while info1_row < 7:
            self.frame_main_habits.rowconfigure(info1_row, minsize=45)
            info1_row += 1

        info1_column = 0
        while info1_column < 16:
            self.frame_main_habits.columnconfigure(info1_column, minsize=27)
            info1_column += 1

        # *Info Button 1 Frame Construction ------------------------------

        self.frame_main_habits_button = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_main_habits_button.grid(
            row=9, column=0, rowspan=1, columnspan=10)

        # *Info Panel 2 Frame Construction ------------------------------

        self.frame_clocked_habit = ttk.Frame(
            self.master, relief=FLAT, style='Yellow.TFrame')
        self.frame_clocked_habit.grid(
            row=4, column=10, rowspan=3, columnspan=10)

       # Define grid 3 x 21
        info2_row = 0
        while info2_row < 3:
            self.frame_clocked_habit.rowconfigure(info2_row, minsize=47.5)
            info2_row += 1

        info2_column = 0
        while info2_column < 11:
            self.frame_clocked_habit.columnconfigure(info2_column, minsize=47)
            info2_column += 1

        # *Info Panel 3 Frame Construction ------------------------------

        self.frame_create_habit = ttk.Frame(
            self.master, relief=FLAT, style='Yellow.TFrame')
        self.frame_create_habit.grid(
            row=7, column=10, rowspan=3, columnspan=10)

        # Define grid 16 x 20
        info4_rows = 0
        while info4_rows < 16:
            self.frame_create_habit.rowconfigure(info4_rows, minsize=11)
            info4_rows += 1

        info4_column = 0
        while info4_column < 20:
            self.frame_create_habit.columnconfigure(
                info4_column, minsize=23.75)
            info4_column += 1

        # *Footer Frame Construction ------------------------------

        self.frame_footer = ttk.Frame(
            self.master, relief=FLAT, style='Maron.TFrame')
        self.frame_footer.config()
        self.frame_footer.grid(row=10, column=0, rowspan=1, columnspan=20)

        # Define grid 1 x 10
        top2_rows = 0
        while top2_rows < 1:
            self.frame_footer.rowconfigure(top2_rows, minsize=47.5)
            top2_rows += 1

        top2_column = 0
        while top2_column < 21:
            self.frame_footer.columnconfigure(top2_column, minsize=46.4)
            top2_column += 1

        # ? ******************************** Construct Frames *******************************

        # * ******************************** Welcome Frames *******************************

        # Logo Display in the Welcome Section
        self.login_logo = PhotoImage(file='assets/main_logo-01.png')
        self.login_logo = self.login_logo.subsample(4, 4)
        self.top_logo = ttk.Label(self.frame_welcome,
                                  image=self.login_logo)

        # Welcome Label
        self.user_first_name = self.user_info['name']
        custom_named_label = f'Hello {self.user_first_name}, Welcome Back!'
        self.header_label = ttk.Label(self.frame_welcome,
                                      text=custom_named_label,
                                      style='Header.TLabel')

        # Date Time Label
        self.date_label = ttk.Label(self.frame_welcome,
                                    text='01-04-2021 7:56pm',
                                    style='Sub.Header.TLabel')

        # ? ******************************** Clock Widgets Actions *******************************

        def clock():
            self.top_clock = self.now.strftime("%A, %d %B %H:%M %p")
            self.date_label.config(text=self.top_clock)
            self.date_label.after(1000, clock)

        clock()

        # ? ***************************************************************************************

        # Button Sign Out
        self.signout_button = ttk.Button(self.frame_welcome,
                                         text='Sign Out',
                                         style='GreenButton.TButton',
                                         command=self.load_login)

        # Geometrtic Distribution
        self.top_logo.grid(row=0, column=1, rowspan=2, columnspan=2)
        self.header_label.grid(row=0, column=3, rowspan=2,
                               columnspan=8, sticky='w')
        self.date_label.grid(row=0, column=12, rowspan=2, columnspan=4)
        self.signout_button.grid(row=0, column=16, rowspan=2, columnspan=3)

        # ******************************** Tab Frames *******************************

        # Button Habit Center
        self.habit_center_label = ttk.Label(self.frame_tab,
                                            text='HABIT CENTER',
                                            style='WhiteOnPink.TLabel',
                                            anchor='center')

        # Geometrtic Distribution
        self.habit_center_label.grid(
            row=0, column=0, columnspan=20, sticky='nesw', pady=(0, 10))

        # ******************************** Top1 Frames *******************************

        # Labels Top1
        self.top1_main1_label = ttk.Label(self.frame_top1,
                                          text='MY HABITS',
                                          style='WhiteOnGreen.TLabel',
                                          anchor="center")

        # Button Stats Clocked Habits
        self.w_stats_button = ttk.Button(self.frame_top1,
                                         text='H STATS!',
                                         style='BlueButton.TButton',
                                         command=self.open_stats_habits)

        self.top1_main2_label = ttk.Label(self.frame_top1,
                                          text='CLOCKED HABITS',
                                          style='WhiteOnGreen.TLabel',
                                          anchor="center")

        # Button Clocked Stats
        self.c_stats_button = ttk.Button(self.frame_top1,
                                         text='C STATS!',
                                         style='BlueButton.TButton',
                                         command=self.open_stats_clockedhabits)

        # Geometrtic Distribution
        self.top1_main1_label.grid(
            row=0, column=0, columnspan=8, sticky='nesw')
        self.w_stats_button.grid(
            row=0, column=8, columnspan=2, sticky='nesw')
        self.top1_main2_label.grid(
            row=0, column=10, columnspan=9, sticky='nesw')
        self.c_stats_button.grid(
            row=0, column=18, columnspan=2, sticky='nesw')

        # ******************************** Info Panel 1  Frames *******************************

        # MORNING IMAGE
        self.morning_image = PhotoImage(file='assets/morning2_logo-01.png')
        self.resampled_image_morning = self.morning_image.subsample(3, 3)

        # EVENING IMAGE
        self.evening_image = PhotoImage(file='assets/evening_logo-01.png')
        self.resampled_image_evening = self.evening_image.subsample(3, 3)

        # ALL DAY IMAGE
        self.all_day_image = PhotoImage(file='assets/all_time-01.png')
        self.resampled_image_all_day = self.all_day_image.subsample(3, 3)

        # AFTERNOON IMAGE
        self.afternoon_image = PhotoImage(file='assets/afternoon_logo-01.png')
        self.resampled_image_afternoon = self.afternoon_image.subsample(3, 3)

        self.icon_habits = []
        self.label_habits = []
        self.complete_habits = []
        self.progress_bar = []
        self.button_habits = []

        # Create Canvas Holding Habits
        self.scroll_canvas = Canvas(
            self.frame_main_habits, width=450, height=250, highlightthickness=0, relief='ridge', background='white')
        self.scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add Scrollbar
        self.scrollbar_habits = ttk.Scrollbar(
            self.frame_main_habits, orient=VERTICAL, command=self.scroll_canvas.yview)
        self.scrollbar_habits.pack(side=RIGHT, fill=Y)

        #!Modify for windows
        self.scroll_canvas.bind_all(
            "<MouseWheel>", lambda event: self.scroll_canvas.yview_scroll(-1*(event.delta), "units"))

        # Configure Canvas
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar_habits.set)
        self.scroll_canvas.bind('<Configure>', lambda e: self.scroll_canvas.configure(
            scrollregion=self.scroll_canvas.bbox('all')))

        # Frame For habits
        self.frame_habits_cont = ttk.Frame(
            self.scroll_canvas, relief=FLAT, style='TFrame')
        self.scroll_canvas.create_window(
            (0, 0), window=self.frame_habits_cont, anchor='nw')

        # Define grid 7 x 16
        habit_con_row = 0
        while habit_con_row < 7:
            self.frame_habits_cont.rowconfigure(habit_con_row, minsize=45)
            habit_con_row += 1

        habit_con_column = 0
        while habit_con_column < 16:
            self.frame_habits_cont.columnconfigure(
                habit_con_column, minsize=27)
            habit_con_column += 1

        # Define Data to work with
        self.today_data = []
        self.today_id_habit = [self.now.strftime(
            "%m-%d-%Y"), self.now.strftime("%A"), int(self.now.strftime("%V"))]

        # Check if any record for today exists
        for d in self.user_info['user_habits_data']:
            if d[0] == self.today_id_habit:
                self.today_data = d

        # Creat New record if none exits
        if not self.today_data:

            self.today_data.append(self.today_id_habit)
            for habits in self.user_info['user_habits']:
                for day in habits[2]:
                    if day == self.now.strftime("%A"):
                        self.today_data.append(
                            [habits[0], float(int(habits[1])), habits[3], 0.0])
                        break

            self.user_info['user_habits_data'].append(self.today_data)

        # Set Todays Streek to 0
        for habit in self.today_data:
            if habit == self.today_id_habit:
                continue
            for streak in self.user_info['user_habits_streak']:
                if habit[0] == streak[0]:
                    new_day = True
                    for item in streak:
                        if isinstance(item, list):
                            if item[0] == int(self.now.strftime("%j")):
                                new_day = False
                    if new_day == True:
                        streak.append([int(self.now.strftime("%j")), 0])

        # Update DataBase
        self.myDataBase.update(self.user_info)

        # DEPLOY LIST OF HABITS
        self.habit_counter = 0
        for habits in self.today_data:

            if habits == self.today_id_habit:
                continue

            # Icon
            if habits[2] == 'morning':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_morning,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[2] == 'all_time':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_all_day,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[2] == 'affternoon':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_afternoon,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[2] == 'evening':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_evening,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            # Label
            label_text = habits[0]
            self.label_habits.append(ttk.Label(
                self.frame_habits_cont, text=label_text, style='BoldTextOnWhite.TLabel', anchor='w'))
            self.label_habits[self.habit_counter].grid(
                row=self.habit_counter, column=3, columnspan=4, sticky='w')

            # Label
            label_text_complete = str(
                int(habits[3])) + '/' + str(int(habits[1]))
            self.complete_habits.append(ttk.Label(
                self.frame_habits_cont, text=label_text_complete, style='BoldTextOnWhite.TLabel', anchor='center'))
            self.complete_habits[self.habit_counter].grid(
                row=self.habit_counter, column=7, columnspan=2)

            # Progress Bar
            self.progress_bar.append(ttk.Progressbar(
                self.frame_habits_cont, orient=HORIZONTAL, length=40, mode='determinate', maximum=habits[1], value=habits[3], style='Pink.Horizontal.TProgressbar'))
            self.progress_bar[self.habit_counter].grid(
                row=self.habit_counter, column=9, columnspan=2, sticky='we')

            # Button Add Habit
            self.button_habits.append(ttk.Button(self.frame_habits_cont,
                                                 text='Done',
                                                 style='GreenButton.TButton',
                                                 command=lambda i=self.habit_counter: self.done_habit(i)))
            if habits[1] == habits[3]:
                self.button_habits[self.habit_counter].config(text='Completed')
                self.button_habits[self.habit_counter]['state'] = DISABLED

            self.button_habits[self.habit_counter].grid(
                row=self.habit_counter, column=12, columnspan=2)

            self.habit_counter += 1

        # ******************************** Info Panel 1 Button Frames *******************************

        # Button Manage Habit
        self.add_habit_button = ttk.Button(self.frame_main_habits_button,
                                           text='Manage My Habits',
                                           style='GreenButton.TButton',
                                           width=40,
                                           command=lambda: self.open_manage_habits(self.username))

        # Geometrtic Distribution
        # *PANEL 2
        self.add_habit_button.pack()

        # ******************************** Info Panel 2 & 3 Frames *******************************

        # ?  Timed Habits Frame *******************************
        # Load Working Text Label
        counter = 1
        text_work_label = ['Active Habits: ']
        for i, v in enumerate(self.user_info['work_habits']):
            text_work_label.append(str(counter) + '.' + v[1] + ',')
            counter += 1

        text_work_label = ' '.join(text_work_label)

        if len(text_work_label) > 70:
            text_work_label = text_work_label[0:71] + '...'

        # Labels Working Habit
        self.workng_main_label = ttk.Label(self.frame_clocked_habit,
                                           text='0:00:00',
                                           style='Stopwatch.TLabel',
                                           anchor=CENTER)

        # ? Attributes Relevant to Stopwatch Widgets Actions *******************************
        self.stopwatch_counter = 0
        self.running = False
        self.working_session_log = self.user_info['work_habits_data']
        self.session_log = []
        # ? *******************************

        # Text Working Count
        self.working_text_label = ttk.Label(self.frame_clocked_habit,
                                            text=text_work_label,
                                            style='TextOnYellow.TLabel')
        self.working_text_label.config(wraplength=230)
        self.working_text_label.config(justify=CENTER)

        # Button Set Habit
        self.set_habit_button = ttk.Button(self.frame_clocked_habit,
                                           text='Set Habit',
                                           style='BlueButton.TButton',
                                           command=lambda: self.open_clocked_habits(self.username))

        # Button Start Working
        self.start_working_button = ttk.Button(self.frame_clocked_habit,
                                               text='Start Session',
                                               style='BlueButton.TButton',
                                               command=lambda: self.start_working(self.workng_main_label))

        # Button End Session
        self.end_session_button = ttk.Button(self.frame_clocked_habit,
                                             text='End Session',
                                             style='BlueButton.TButton',
                                             command=lambda: self.end_session())

        # STOPWATCH IMAGE
        self.stop_watch_image = PhotoImage(file='assets/stop_watch-01.png')
        self.stop_watch_image = self.stop_watch_image.subsample(5, 5)
        self.stop_watch_button = ttk.Label(self.frame_clocked_habit,
                                           image=self.stop_watch_image,
                                           style='TextOnYellow.TLabel')

        # ?  Create Habit Frame *******************************

        # Labels Create Habit
        self.create_habit_label = ttk.Label(self.frame_create_habit,
                                            text='New Habit',
                                            style='WhiteOnPink.TLabel',
                                            anchor="center")
        # Habit Name Label
        self.name_label = ttk.Label(
            self.frame_create_habit, text='Habit Name:', style='BoldTextOnYellow.TLabel')

        # Entry for Habit Name
        self.entry_name = ttk.Entry(
            self.frame_create_habit, width=20, font=('Arial', 10))

        # Daily Repetitions Name Label
        self.repetition_label = ttk.Label(
            self.frame_create_habit, text='Daily Goal:', style='BoldTextOnYellow.TLabel')

        # Spinbox for Daily Repetitions
        self.repetition_value = IntVar()
        self.repetition_value.set(1)
        self.spinbox_repetition = ttk.Spinbox(
            self.frame_create_habit, from_=1, to=20, textvariable=self.repetition_value, state='readonly', width=3)

        # Radiobutton for Monday
        self.monday_day = StringVar()
        self.monday_radiobutton = ttk.Checkbutton(
            self.frame_create_habit, text='Mon.', variable=self.monday_day, onvalue='Monday', offvalue='', style='TCheckbutton')

        # Checkbutton for Tuesday
        self.tuesday_day = StringVar()
        self.tuesday_radiobutton = ttk.Checkbutton(
            self.frame_create_habit, text='Tue.', variable=self.tuesday_day, onvalue='Tuesday', offvalue='', style='TCheckbutton')

        # Checkbutton for Wednesday
        self.wednesday_day = StringVar()
        self.wednesday_radiobutton = ttk.Checkbutton(
            self.frame_create_habit, text='Wed.', variable=self.wednesday_day, onvalue='Wednesday', offvalue='', style='TCheckbutton')

        # Checkbutton for Thursday
        self.thursday_day = StringVar()
        self.thursday_radiobutton = ttk.Checkbutton(
            self.frame_create_habit, text='Thu.', variable=self.thursday_day, onvalue='Thursday', offvalue='', style='TCheckbutton')

        # Checkbutton for Friday
        self.friday_day = StringVar()
        self.friday_radiobutton = ttk.Checkbutton(
            self.frame_create_habit, text='Fri.', variable=self.friday_day, onvalue='Friday', offvalue='', style='TCheckbutton')

        # Checkbutton for Saturday
        self.saturday_day = StringVar()
        self.saturday_radiobutton = ttk.Checkbutton(
            self.frame_create_habit, text='Sat.', variable=self.saturday_day, onvalue='Saturday', offvalue='', style='TCheckbutton')

        # Checkbutton for Sunday
        self.sunday_day = StringVar()
        self.sunday_radiobutton = ttk.Checkbutton(
            self.frame_create_habit, text='Sun.', variable=self.sunday_day, onvalue='Sunday', offvalue='', style='TCheckbutton')

        # Time Variable

        self.selected_time = StringVar()

        # MORNING IMAGE
        self.morning_image_add_habit = self.morning_image.subsample(2, 2)
        self.morning_button = ttk.Button(self.frame_create_habit,
                                         image=self.morning_image_add_habit,
                                         style='YellowButton.TButton',
                                         command=self.morning_action)

        # EVENING IMAGE
        self.evening_image_add_habit = self.evening_image.subsample(2, 2)
        self.evening_button = ttk.Button(self.frame_create_habit,
                                         image=self.evening_image_add_habit,
                                         style='YellowButton.TButton',
                                         command=self.evening_action)

        # ALL DAY IMAGE
        self.all_day_image_add_habit = self.all_day_image.subsample(2, 2)
        self.all_day_button = ttk.Button(self.frame_create_habit,
                                         image=self.all_day_image_add_habit,
                                         style='YellowButton.TButton',
                                         command=self.all_time_action)

        # AFTERNOON IMAGE
        self.afternoon_image_add_habit = self.afternoon_image.subsample(2, 2)
        self.afternoon_button = ttk.Button(self.frame_create_habit,
                                           image=self.afternoon_image_add_habit,
                                           style='YellowButton.TButton',
                                           command=self.afternoon_action)

        # Button Add Habit
        self.add_habit_button = ttk.Button(self.frame_create_habit,
                                           text='Add',
                                           style='GreenButton.TButton',
                                           command=self.submit_new_habit)

        # Geometrtic Distribution
        # *PANEL 2
        self.workng_main_label.grid(row=0, column=3, columnspan=6)
        self.stop_watch_button.grid(row=0, column=1, rowspan=2, columnspan=2)
        self.working_text_label.grid(row=1, column=3, columnspan=6)
        self.set_habit_button.grid(row=2, column=1, columnspan=2)
        self.start_working_button.grid(row=2, column=4, columnspan=2)
        self.end_session_button.grid(row=2, column=7, columnspan=2)

        # *PANEL 3
        self.create_habit_label.grid(
            row=0, column=0, rowspan=3, columnspan=18, sticky='nesw')

        self.name_label.grid(row=5, column=1, rowspan=2,
                             columnspan=3, sticky='w')
        self.entry_name.grid(row=5, column=4, rowspan=2,
                             columnspan=6, sticky='nesw')
        self.repetition_label.grid(
            row=5, column=11, rowspan=2, columnspan=3, sticky='w')
        self.spinbox_repetition.grid(
            row=5, column=14, rowspan=2, columnspan=2, sticky='ns')
        self.monday_radiobutton.grid(
            row=9, column=1, rowspan=1, columnspan=2, sticky='e')
        self.tuesday_radiobutton.grid(
            row=9, column=3, rowspan=1, columnspan=2, sticky='w')
        self.wednesday_radiobutton.grid(
            row=9, column=5, rowspan=1, columnspan=2, sticky='w')
        self.thursday_radiobutton.grid(
            row=9, column=7, rowspan=1, columnspan=2, sticky='w')
        self.friday_radiobutton.grid(
            row=9, column=9, rowspan=1, columnspan=2, sticky='w')
        self.saturday_radiobutton.grid(
            row=9, column=11, rowspan=1, columnspan=2, sticky='w')
        self.sunday_radiobutton.grid(row=9, column=13, rowspan=1, columnspan=2)

        self.morning_button.grid(row=11, column=5, rowspan=4, columnspan=3)
        self.afternoon_button.grid(row=11, column=8, rowspan=4, columnspan=3)
        self.evening_button.grid(row=11, column=11, rowspan=4, columnspan=3)
        self.all_day_button.grid(row=11, column=14, rowspan=4, columnspan=3)

        self.add_habit_button.grid(
            row=12, column=1, rowspan=3, columnspan=3, sticky='nesw')

        # ******************************** Footer Frames *******************************

        # Copyright
        self.copyright_label = ttk.Label(self.frame_footer, text='Welcome to Ness. Please review our Privacy Notice. © 2021, Ness, Inc.',
                                         style='FooterHabits.TLabel')

        # Geometrtic Distribution
        self.copyright_label.grid(row=0, column=6, columnspan=7)

    #! ******************************** Methods *******************************

    def load_login(self):  # !ADD DESTROY Help
        '''This method signs out the user and loads the welcome class'''

        from main import Welcome
        self.frame_welcome.destroy()
        self.frame_tab.destroy()
        self.frame_top1.destroy()
        self.frame_main_habits.destroy()
        self.frame_main_habits_button.destroy()
        self.frame_clocked_habit.destroy()
        self.frame_create_habit.destroy()
        self.frame_footer.destroy()
        if hasattr(self, "root4"):
            self.root4.destroy()
        if hasattr(self, "root3"):
            self.root3.destroy()
        if hasattr(self, "root2"):
            self.root2.destroy()
        if hasattr(self, "root1"):
            self.root1.destroy()

        # * LOAD NEW CLASS (LOGIN) TO ROOT
        self.another = Welcome(self.master)

    def counter_call(self, label):
        '''This method controls the stopwatch'''

        # Define Habits to run
        time_span_habits = []

        for i, v in enumerate(self.user_info['work_habits']):
            time_span_habits.append([(int(v[0]) * 60), v[1]])

        def count():
            if self.running:
                self.stopwatch_counter
                stopwatch_position = str(
                    timedelta(seconds=self.stopwatch_counter))
                label.config(text=stopwatch_position)
                label.after(1000, count)
                self.stopwatch_counter += 1
        count()

        def alamrs():
            if self.running:
                for item in time_span_habits:
                    if self.stopwatch_counter % item[0] == 0:
                        response = messagebox.askokcancel(title='Habit Alarm',
                                                          message=f'You should {item[1].upper()} now. Click cancel to skip.',
                                                          icon='error')

                        if response == True:
                            self.session_log.append(
                                [1, self.stopwatch_counter, item[0], item[1]])

                        elif response == False:
                            self.session_log.append(
                                [0, self.stopwatch_counter, item[0], item[1]])

                self.master.after(1000, alamrs)

        alamrs()

    def start_working(self, label):
        ''' This method starts the stopwatch'''

        # load fresh habits
        self.user_info = self.myDataBase.load()

        # Load Working Text Label
        counter = 1
        text_work_label = ['Active Habits: ']
        for i, v in enumerate(self.user_info['work_habits']):
            text_work_label.append(str(counter) + '.' + v[1] + ',')
            counter += 1

        text_work_label = ' '.join(text_work_label)

        if len(text_work_label) > 70:
            text_work_label = text_work_label[0:71] + '...'

        self.working_text_label.configure(text=text_work_label)
        self.now2 = datetime.now()
        self.session_log = [(self.now2.strftime("%m-%d-%Y %H:%M:%S"))]
        self.running
        self.running = True
        self.counter_call(label)
        self.set_habit_button['state'] = DISABLED
        self.start_working_button['state'] = DISABLED
        self.end_session_button['state'] = NORMAL

    def end_session(self):
        '''This method stops the stopwatch and updates the database'''

        self.stopwatch_counter = 0
        self.running
        self.running = False
        self.set_habit_button['state'] = NORMAL
        self.start_working_button['state'] = NORMAL
        self.end_session_button['state'] = DISABLED

        self.working_session_log.append(self.session_log)
        self.user_info['work_habits_data'] = self.working_session_log

        self.myDataBase.update(self.user_info)

        self.session_log = []

    def open_clocked_habits(self, username):
        '''This method loads the Work_Habits Class in a new windows. The Work_Habit Class
        manages the cloacked habits defined by the user.'''

        from clocked_habits import Work_Habits
        self.root1 = Toplevel(self.master)
        Work_Habits(self.root1, username)

    def morning_action(self):
        '''This method gives the appearance of the morning button staying pressed'''

        self.morning_button.configure(style='YellowButton2.TButton')
        self.selected_time.set('morning')
        self.afternoon_button.configure(style='YellowButton.TButton')
        self.evening_button.configure(style='YellowButton.TButton')
        self.all_day_button.configure(style='YellowButton.TButton')

    def evening_action(self):
        '''This method gives the appearance of the evening button staying pressed'''

        self.morning_button.configure(style='YellowButton.TButton')
        self.selected_time.set('evening')
        self.afternoon_button.configure(style='YellowButton.TButton')
        self.evening_button.configure(style='YellowButton2.TButton')
        self.all_day_button.configure(style='YellowButton.TButton')

    def afternoon_action(self):
        '''This method gives the appearance of the afternoon button staying pressed'''

        self.morning_button.configure(style='YellowButton.TButton')
        self.selected_time.set('affternoon')
        self.afternoon_button.configure(style='YellowButton2.TButton')
        self.evening_button.configure(style='YellowButton.TButton')
        self.all_day_button.configure(style='YellowButton.TButton')

    def all_time_action(self):
        '''This method gives the appearance of the all time button staying pressed'''

        self.morning_button.configure(style='YellowButton.TButton')
        self.selected_time.set('all_time')
        self.afternoon_button.configure(style='YellowButton.TButton')
        self.evening_button.configure(style='YellowButton.TButton')
        self.all_day_button.configure(style='YellowButton2.TButton')

    def submit_new_habit(self):
        '''This method collects all the information from the new habit form. It checks if
        all the data is correct and sets all parameter in the database for the creation
        of the new habit submitted'''

        self.name_new_habit = self.entry_name.get()
        self.daily_goal_new_habit = self.repetition_value.get()
        self.selected_days_new_habit = [self.monday_day.get(), self.tuesday_day.get(),
                                        self.wednesday_day.get(), self.thursday_day.get(),
                                        self.friday_day.get(), self.saturday_day.get(), self.sunday_day.get()]
        self.selected_days_new_habit = list(
            filter(None, self.selected_days_new_habit))
        self.selected_time_new_habit = self.selected_time.get()

        self.valid_submission = True

        # Tests for validity
        if self.valid_submission == True:
            if self.name_new_habit == '':
                messagebox.showinfo(title='Error',
                                    message='Please fill "Habit Name"',
                                    icon='warning')
                self.valid_submission = False

        if self.valid_submission == True:
            if len(self.name_new_habit) >= 17:
                messagebox.showinfo(title='Error',
                                    message='Please choose a shorter habit name.',
                                    icon='warning')
                self.valid_submission = False

        if self.valid_submission == True:
            for item in self.user_info['user_habits']:
                if item[0] == self.name_new_habit:
                    messagebox.showinfo(title='Error',
                                        message='Habit exists already. Pick a new.',
                                        icon='warning')
                    self.valid_submission = False

        if self.valid_submission == True:
            if len(self.selected_days_new_habit) == 0:
                messagebox.showinfo(title='Error',
                                    message='Please select at least one day.',
                                    icon='warning')
                self.valid_submission = False

        if self.valid_submission == True:
            if self.selected_time_new_habit == '':
                messagebox.showinfo(title='Error',
                                    message='Please select one "Time Period".',
                                    icon='warning')
                self.valid_submission = False
        # End Tests for validity

        if self.valid_submission == True:

            self.all_habit_data = [self.name_new_habit, float(self.daily_goal_new_habit), (list(
                filter(None, self.selected_days_new_habit))), self.selected_time_new_habit, 0]

            self.user_info['user_habits'].append(self.all_habit_data)
            self.user_info['user_habits_streak'].append(
                [self.name_new_habit, len(self.selected_days_new_habit)])

            # Clear all fields
            self.entry_name.delete(0, 'end')
            self.repetition_value.set(1)
            self.monday_day.set('')
            self.tuesday_day.set(''),
            self.wednesday_day.set(''),
            self.thursday_day.set(''),
            self.friday_day.set(''),
            self.saturday_day.set(''),
            self.sunday_day.set('')
            self.morning_button.configure(style='YellowButton.TButton')
            self.afternoon_button.configure(style='YellowButton.TButton')
            self.evening_button.configure(style='YellowButton.TButton')
            self.all_day_button.configure(style='YellowButton.TButton')

            messagebox.showinfo(title='Success',
                                message='You have successfully added your habit.',
                                icon='warning')

            # *UPDATATE HABIT CANVAS

            # Check if any record for today exists
            for d in self.user_info['user_habits_data']:
                if d[0] == self.today_id_habit:
                    self.today_data = d
                    for day in self.selected_days_new_habit:
                        if day == self.now.strftime("%A"):
                            self.today_data.append((self.all_habit_data[0], float(
                                int(self.all_habit_data[1])), self.all_habit_data[3], 0.0))

            # Set Todays Streek to 0
            for idx, streak in enumerate(self.user_info['user_habits_streak']):
                if streak[0] == self.all_habit_data[0]:
                    if self.now.strftime('%A') in self.selected_days_new_habit:
                        self.user_info['user_habits_streak'][idx].append(
                            [int(self.now.strftime("%j")), 0])

            # Update DataBase
            self.myDataBase.update(self.user_info)

            self.refresh_habit_panel()

    def on_mousewheel(self, event):  # !MODIFY FOR WINDOWS
        '''This method manages the scrolling event'''

        self.scroll_canvas.yview_scroll(-1*(event.delta), "units")

    def done_habit(self, i):
        '''This function acepts the index of a button as an argument from My Habit Panel
        and perform multiple updates on the GUI and database'''

        new_value_progress_bar = 0.0
        total_value_progress_bar = 0.0
        for data in self.today_data:
            if data == self.today_id_habit:
                continue
            for parameter in data:
                if parameter == self.label_habits[i].cget("text"):
                    data[3] += 1.0
                    new_value_progress_bar = data[3]
                    total_value_progress_bar = data[1]

        new_completion_label = str(
            int(new_value_progress_bar)) + '/' + str(int(total_value_progress_bar))

        self.progress_bar[i].config(value=new_value_progress_bar)
        self.complete_habits[i].config(text=new_completion_label)

        # If daily goal has been completed
        if new_value_progress_bar == total_value_progress_bar:

            self.button_habits[i].config(text='Completed')
            self.button_habits[i]['state'] = DISABLED

            # Mark today habit completed and update streak database
            for streak in self.user_info['user_habits_streak']:
                if self.label_habits[i].cget("text") == streak[0]:
                    for v in streak:
                        if isinstance(v, list):
                            if v[0] == int(self.now.strftime("%j")):
                                v[1] = 1
                                break

        # Update Data
        for d in self.user_info['user_habits_data']:
            if d[0] == self.today_id_habit:
                d = self.today_data
                break

        # Update DataBase
        self.myDataBase.update(self.user_info)

    def refresh_habit_panel(self):  # !MODIFY FOR WINDOWS
        '''This method reload the habit panel when a habit is submitted and added '''

        self.frame_main_habits.destroy()

        self.user_info = self.myDataBase.load()

        self.frame_main_habits = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_main_habits.grid(row=4, column=0, rowspan=5, columnspan=10)

        # Define grid 7 x 16
        info1_row = 0
        while info1_row < 7:
            self.frame_main_habits.rowconfigure(info1_row, minsize=45)
            info1_row += 1

        info1_column = 0
        while info1_column < 16:
            self.frame_main_habits.columnconfigure(info1_column, minsize=27)
            info1_column += 1

        self.icon_habits = []
        self.label_habits = []
        self.complete_habits = []
        self.progress_bar = []
        self.button_habits = []

        # Create Canvas Holding Habits
        self.scroll_canvas = Canvas(
            self.frame_main_habits, width=450, height=250, highlightthickness=0, relief='ridge', background='white')
        self.scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add Scrollbar
        self.scrollbar_habits = ttk.Scrollbar(
            self.frame_main_habits, orient=VERTICAL, command=self.scroll_canvas.yview)
        self.scrollbar_habits.pack(side=RIGHT, fill=Y)

        #!Modify for windows
        self.scroll_canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        # Configure Canvas
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar_habits.set)
        self.scroll_canvas.bind('<Configure>', lambda e: self.scroll_canvas.configure(
            scrollregion=self.scroll_canvas.bbox('all')))

        # Frame For habits
        self.frame_habits_cont = ttk.Frame(
            self.scroll_canvas, relief=FLAT, style='TFrame')
        self.scroll_canvas.create_window(
            (0, 0), window=self.frame_habits_cont, anchor='nw')

        # Define grid 7 x 16
        habit_con_row = 0
        while habit_con_row < 7:
            self.frame_habits_cont.rowconfigure(habit_con_row, minsize=45)
            habit_con_row += 1

        habit_con_column = 0
        while habit_con_column < 16:
            self.frame_habits_cont.columnconfigure(
                habit_con_column, minsize=27)
            habit_con_column += 1

        # Define Data to work with
        self.today_data = []
        self.today_id_habit = [self.now.strftime(
            "%m-%d-%Y"), self.now.strftime("%A"), int(self.now.strftime("%V"))]

        # Check if any record for today exists
        for d in self.user_info['user_habits_data']:
            if d[0] == self.today_id_habit:
                self.today_data = d

        # Creat New record if none exits
        if not self.today_data:

            self.today_data.append(self.today_id_habit)
            for habits in self.user_info['user_habits']:
                for day in habits[2]:
                    if day == self.now.strftime("%A"):
                        self.today_data.append(
                            [habits[0], float(int(habits[1])), habits[3], 0.0])
                        break

            self.user_info['user_habits_data'].append(self.today_data)

        # Set Todays Streek to 0
        for habit in self.today_data:
            if habit == self.today_id_habit:
                continue
            for streak in self.user_info['user_habits_streak']:
                if habit[0] == streak[0]:
                    new_day = True
                    for item in streak:
                        if isinstance(item, list):
                            if item[0] == int(self.now.strftime("%j")):
                                new_day = False
                    if new_day == True:
                        streak.append([int(self.now.strftime("%j")), 0])

        # Update DataBase
        self.myDataBase.update(self.user_info)

        # DELOPY HABITS
        self.habit_counter = 0
        for habits in self.today_data:

            if habits == self.today_id_habit:
                continue

            # Icon
            if habits[2] == 'morning':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_morning,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[2] == 'all_time':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_all_day,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[2] == 'affternoon':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_afternoon,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[2] == 'evening':
                self.icon_habits.append(ttk.Button(self.frame_habits_cont,
                                                   image=self.resampled_image_evening,
                                                   style='WhiteButton.TButton'))
                self.icon_habits[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            # Label
            label_text = habits[0]
            self.label_habits.append(ttk.Label(
                self.frame_habits_cont, text=label_text, style='BoldTextOnWhite.TLabel', anchor='w'))
            self.label_habits[self.habit_counter].grid(
                row=self.habit_counter, column=3, columnspan=4, sticky='w')

            # Label
            label_text_complete = str(
                int(habits[3])) + '/' + str(int(habits[1]))
            self.complete_habits.append(ttk.Label(
                self.frame_habits_cont, text=label_text_complete, style='BoldTextOnWhite.TLabel', anchor='center'))
            self.complete_habits[self.habit_counter].grid(
                row=self.habit_counter, column=7, columnspan=2)

            # Progress Bar
            self.progress_bar.append(ttk.Progressbar(
                self.frame_habits_cont, orient=HORIZONTAL, length=40, mode='determinate', maximum=habits[1], value=habits[3], style='Pink.Horizontal.TProgressbar'))
            self.progress_bar[self.habit_counter].grid(
                row=self.habit_counter, column=9, columnspan=2, sticky='we')

            # Button Add Habit
            self.button_habits.append(ttk.Button(self.frame_habits_cont,
                                                 text='Done',
                                                 style='GreenButton.TButton',
                                                 command=lambda i=self.habit_counter: self.done_habit(i)))
            if habits[1] == habits[3]:
                self.button_habits[self.habit_counter].config(text='Completed')
                self.button_habits[self.habit_counter]['state'] = DISABLED

            self.button_habits[self.habit_counter].grid(
                row=self.habit_counter, column=12, columnspan=2)

            self.habit_counter += 1

    def open_manage_habits(self, username):
        '''This method loads the Manage Habit window. The Manage Habit Window
        allows the user to manage active habits'''

        self.root2 = Toplevel(self.master)
        self.manage_window(self.root2)

    def manage_window(self, root2):
        '''This method is only callable only if OPEN_MANAGE_HABITS has been called. 
        This method manages all the gui and methods for the Manage Habit Window
        The Manage Habit Window allows the user to manage active habits'''

        self.root2.title('Ness')
        self.root2.resizable(False, False)
        self.root2.geometry("700x600")
        self.root2.configure(background='#fffff3')

        # Define grid 10 x 10
        master_rows = 0
        while master_rows < 10:
            self.root2.rowconfigure(master_rows, minsize=60)
            master_rows += 1

        master_column = 0
        while master_column < 10:
            self.root2.columnconfigure(master_column, minsize=70)
            master_column += 1

        # *Header Manage Habits Frame Construction ------------------------------

        self.frame_manage_top = ttk.Frame(
            self.root2, relief=FLAT, style='TFrame')
        self.frame_manage_top.grid(row=0, column=0, rowspan=2, columnspan=10)

        # Define grid 2 x 10
        manage_top_rows = 0
        while manage_top_rows < 2:
            self.frame_manage_top.rowconfigure(manage_top_rows, minsize=60)
            manage_top_rows += 1

        manage_top_column = 0
        while manage_top_column < 10:
            self.frame_manage_top.columnconfigure(
                manage_top_column, minsize=70)
            manage_top_column += 1

        # *Main Header Manage Habits Frame Construction ------------------------------

        self.frame_manage_subheader = ttk.Frame(
            self.root2, relief=FLAT, style='Yellow.TFrame')
        self.frame_manage_subheader.grid(
            row=2, column=0, rowspan=1, columnspan=10)

        # Define grid 1 x 10
        manage_subheader_row = 0
        while manage_subheader_row < 1:
            self.frame_manage_subheader.rowconfigure(
                manage_subheader_row, minsize=60)
            manage_subheader_row += 1

        manage_subheader_column = 0
        while manage_subheader_column < 10:
            self.frame_manage_subheader.columnconfigure(
                manage_subheader_column, minsize=70)
            manage_subheader_column += 1

        # *Deletion Header Frame Construction ------------------------------

        self.frame_deletion_panel_header = ttk.Frame(
            self.root2, relief=FLAT, style='Yellow.TFrame')
        self.frame_deletion_panel_header.grid(
            row=3, column=0, rowspan=1, columnspan=10)

        # Define grid 1 x 20
        deletion_header_row = 0
        while deletion_header_row < 1:
            self.frame_deletion_panel_header.rowconfigure(
                deletion_header_row, minsize=60)
            deletion_header_row += 1

        deletion_header_column = 0
        while deletion_header_column < 20:
            self.frame_deletion_panel_header.columnconfigure(
                deletion_header_column, minsize=33)
            deletion_header_column += 1

        # *Deletion Panel Frame Construction ------------------------------

        self.frame_deletion_panel = ttk.Frame(
            self.root2, relief=FLAT, style='Yellow.TFrame')
        self.frame_deletion_panel.config()
        self.frame_deletion_panel.grid(
            row=4, column=0, rowspan=7, columnspan=10)

        # Define grid 4 x 10
        deletion_panel_row = 0
        while deletion_panel_row < 4:
            self.frame_deletion_panel.rowconfigure(
                deletion_panel_row, minsize=60)
            deletion_panel_row += 1

        deletion_panel_column = 0
        while deletion_panel_column < 10:
            self.frame_deletion_panel.columnconfigure(
                deletion_panel_column, minsize=70)
            deletion_panel_column += 1

        # ******************************** Header Manage Habits Frames *******************************

        # Logo Display in the Welcome Section
        self.manage_top_logo = ttk.Label(self.frame_manage_top,
                                         image=self.login_logo,
                                         style='Header.TLabel')

        # Welcome Label
        self.manage_hearder_label = ttk.Label(self.frame_manage_top,
                                              text='Manage Your Habits',
                                              style='Header.TLabel')

        # Geometrtic Distribution
        self.manage_top_logo.grid(
            row=0, column=2, rowspan=2, columnspan=2, sticky='')
        self.manage_hearder_label.grid(row=0, column=4, rowspan=2,
                                       columnspan=5, sticky='w')

        # ******************************** Sub Header Frames *******************************

        # Labels Top1
        self.active_header_label = ttk.Label(self.frame_manage_subheader,
                                             text='My Active Habits',
                                             style='WhiteOnPink.TLabel',
                                             anchor="center")

        # Geometrtic Distribution
        self.active_header_label.grid(
            row=0, column=0, rowspan=1, columnspan=20, sticky='nesw')

        # ******************************** Panel Header Frames *******************************

        # 1 Label
        self.one_label_manage = ttk.Label(
            self.frame_deletion_panel_header, text='Time', style='PinkOnYellow.TLabel', anchor=CENTER)

        # 2 Label
        self.two_label_manage = ttk.Label(
            self.frame_deletion_panel_header, text='Habit Name', style='PinkOnYellow.TLabel', anchor=CENTER)

        # 3 Label
        self.three_label_manage = ttk.Label(
            self.frame_deletion_panel_header, text='Daily Goal', style='PinkOnYellow.TLabel', anchor=CENTER)

        # 4 Label
        self.four_label_manage = ttk.Label(
            self.frame_deletion_panel_header, text='Frequency', style='PinkOnYellow.TLabel', anchor=CENTER)

        # Geometrtic Distribution
        self.one_label_manage.grid(row=0, column=0, rowspan=1,
                                   columnspan=2, sticky='se')
        self.two_label_manage.grid(row=0, column=3, rowspan=1,
                                   columnspan=3, sticky='ws')
        self.three_label_manage.grid(row=0, column=6, rowspan=1,
                                     columnspan=2, sticky='ws')
        self.four_label_manage.grid(row=0, column=9, rowspan=1,
                                    columnspan=3, sticky='s')

        # ******************************** Deletion Panel Frames *******************************

        self.icon_habits_2 = []
        self.label_habits_2 = []
        self.goal_habits_2 = []
        self.frequency_habit_2 = []
        self.button_habits_2 = []

        # Create Canvas Holding Habits
        self.scroll_canvas_2 = Canvas(
            self.frame_deletion_panel, width=600, height=305, highlightthickness=0, relief='ridge', bg='#fffff3')
        self.scroll_canvas_2.pack(side=LEFT, fill=BOTH, expand=1)

        # Add Scrollbar
        self.scrollbar_habits_2 = ttk.Scrollbar(
            self.frame_deletion_panel, orient=VERTICAL, command=self.scroll_canvas_2.yview)
        self.scrollbar_habits_2.pack(side=RIGHT, fill=Y)

        # Configure Canvas
        self.scroll_canvas_2.configure(
            yscrollcommand=self.scrollbar_habits_2.set)

        self.scroll_canvas_2.bind('<Configure>', lambda e: self.scroll_canvas_2.configure(
            scrollregion=self.scroll_canvas_2.bbox('all')))

        # Frame For habits
        self.fram_habits_con_2 = ttk.Frame(
            self.scroll_canvas_2, relief=FLAT, style='Yellow.TFrame')
        self.scroll_canvas_2.create_window(
            (0, 0), window=self.fram_habits_con_2, anchor='nw')

        # Define grid 7 x 16
        habit_con_row_2 = 0
        while habit_con_row_2 < 7:
            self.fram_habits_con_2.rowconfigure(habit_con_row_2, minsize=45)
            habit_con_row_2 += 1

        habit_con_column_2 = 0
        while habit_con_column_2 < 16:
            self.fram_habits_con_2.columnconfigure(
                habit_con_column_2, minsize=27)
            habit_con_column_2 += 1

        mapped_day = {'Monday': 'Mon', 'Tuesday': 'Tue', 'Wednesday': 'Wed',
                      'Thursday': 'Thu', 'Friday': 'Fri', 'Saturday': 'Sat', 'Sunday': 'Sun'}

        self.habit_counter = 0
        # Elaborate List of habits
        for habits in self.user_info['user_habits']:

            # Icon
            if habits[3] == 'morning':
                self.icon_habits_2.append(ttk.Label(self.fram_habits_con_2,
                                                    image=self.resampled_image_morning,
                                                    style='TextOnYellow.TLabel'))
                self.icon_habits_2[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[3] == 'all_time':
                self.icon_habits_2.append(ttk.Label(self.fram_habits_con_2,
                                                    image=self.resampled_image_all_day,
                                                    style='TextOnYellow.TLabel'))
                self.icon_habits_2[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[3] == 'affternoon':
                self.icon_habits_2.append(ttk.Label(self.fram_habits_con_2,
                                                    image=self.resampled_image_afternoon,
                                                    style='TextOnYellow.TLabel'))
                self.icon_habits_2[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            elif habits[3] == 'evening':
                self.icon_habits_2.append(ttk.Label(self.fram_habits_con_2,
                                                    image=self.resampled_image_evening,
                                                    style='TextOnYellow.TLabel'))
                self.icon_habits_2[self.habit_counter].grid(
                    row=self.habit_counter, column=0, columnspan=2)

            # Label
            label_text = habits[0]
            self.label_habits_2.append(ttk.Label(
                self.fram_habits_con_2, text=label_text, style='BoldTextOnYellow.TLabel', anchor='w'))
            self.label_habits_2[self.habit_counter].grid(
                row=self.habit_counter, column=3, columnspan=4, sticky='w')

            # Label 2 (Goal)
            label_text_complete = int(habits[1])
            self.goal_habits_2.append(ttk.Label(
                self.fram_habits_con_2, text=label_text_complete, style='BoldTextOnYellow.TLabel', anchor='center'))
            self.goal_habits_2[self.habit_counter].grid(
                row=self.habit_counter, column=7, columnspan=2)

            # Frecuency
            habit_frequency_list = [newday for day in habits[2]
                                    for oldday, newday in mapped_day.items() if oldday == day]

            frequency_label = ''

            if len(habit_frequency_list) == 1:
                frequency_label = habit_frequency_list[0] + \
                    ' - (Weekly Habit)'

            else:
                frequency_label = ', '.join(habit_frequency_list)

            self.frequency_habit_2.append(ttk.Label(
                self.fram_habits_con_2, text=frequency_label, style='BoldTextOnYellow.TLabel', anchor='w'))
            self.frequency_habit_2[self.habit_counter].grid(
                row=self.habit_counter, column=9, columnspan=2, sticky='we')

            # Button Delete Habit
            self.button_habits_2.append(ttk.Button(self.fram_habits_con_2,
                                                   text='Delete',
                                                   style='GreenButton.TButton',
                                                   command=lambda i=self.habit_counter: self.delete_habit(i)))
            self.button_habits_2[self.habit_counter].grid(
                row=self.habit_counter, column=12, columnspan=2)

            self.habit_counter += 1

    def delete_habit(self, i):
        '''This method is callable only if OPEN_MANAGE_HABITS has been called. This function acepts 
        the index of a DELETE button (part of the GUI of the Manage Habit Window) as an argument 
        and deletes ALL the data associates with the selected habit from ALL databases'''

        response = messagebox.askokcancel(title='Confirm',
                                          message='All data associated with this habit will be deleted permanently. Do you want to proceed?',
                                          icon='warning')

        if response == True:

            self.selected_habit = self.label_habits_2[i].cget("text")

            # Delete from USER HABITS
            self.user_info['user_habits'] = [
                x for x in self.user_info['user_habits'] if x[0] != self.selected_habit]

            # Delete from USER HABITS DATA
            for s in self.user_info['user_habits_data']:
                for ix, d in enumerate(s):
                    if d[0] == self.selected_habit:
                        del s[ix]
                        break

            # Delete from USER HABITS STREAK
            self.user_info['user_habits_streak'] = [
                x for x in self.user_info['user_habits_streak'] if x[0] != self.selected_habit]

            self.myDataBase.update(self.user_info)

            self.manage_window(self.root2)
            self.refresh_habit_panel()

    def open_stats_habits(self):
        '''Load the Stats Window. This window shows all insight processed from the data
        collected from each active habit'''

        from stats import Stats
        self.root3 = Toplevel(self.master)
        Stats(self.root3, self.username)

    def open_stats_clockedhabits(self):
        '''Load the Stats Window. This window shows all insight processed from the data
        collected from each active clocked habit'''

        from clocked_stats import ClockedStats
        self.root4 = Toplevel(self.master)
        ClockedStats(self.root4, self.username)
