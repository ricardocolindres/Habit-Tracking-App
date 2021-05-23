# Header File: set_clocked_habits.py
# Manage Clock Habits Window for Ness.
# History:
# Date    Programmer   - Description
# ---------- ---------- ----------------------------
# 05/04/2021     Ricardo Josue Colindres      - Created

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import DataBase
from styles import Styles


class Work_Habits:

    #! ******************************** Properties *******************************

    def __init__(self, master, username='ricardocolindres@me.com'):

        self.username = username

        self.myDataBase = DataBase(self.username)

        # Load User Info
        self.user_info = self.myDataBase.load()

        # ******************************** Main Window *******************************

        self.master = master
        self.master.title('Ness')
        self.master.resizable(False, False)
        self.master.geometry("475x475")
        self.master.configure(background='white')

        # Define grid 17 x 10
        master_rows = 0
        while master_rows < 17:
            self.master.rowconfigure(master_rows, minsize=25)
            master_rows += 1

        master_column = 0
        while master_column < 10:
            self.master.columnconfigure(master_column, minsize=47.5)
            master_column += 1

        # ******************************** Define Styles *******************************

        self.s = Styles()

        # ******************************** Define Frames *******************************

        # *Welcome Frame Construction ------------------------------

        self.frame_welcome = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_welcome.config()
        self.frame_welcome.grid(row=0, column=0, rowspan=4, columnspan=10)

        # Define grid 4 x 10
        welcome_rows = 0
        while welcome_rows < 4:
            self.frame_welcome.rowconfigure(welcome_rows, minsize=25)
            welcome_rows += 1

        welcome_column = 0
        while welcome_column < 10:
            self.frame_welcome.columnconfigure(welcome_column, minsize=47.5)
            welcome_column += 1

        # *Top1 Frame Construction ------------------------------

        self.frame_top1 = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_top1.config()
        self.frame_top1.grid(row=4, column=0, rowspan=2, columnspan=10)

        # Define grid 2 x 10
        top1_rows = 0
        while top1_rows < 2:
            self.frame_top1.rowconfigure(top1_rows, minsize=25)
            top1_rows += 1

        top1_column = 0
        while top1_column < 10:
            self.frame_top1.columnconfigure(top1_column, minsize=50)
            top1_column += 1

        # *Info Panel 1 Frame Construction ------------------------------

        self.frame_info_panel1 = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_info_panel1.config()
        self.frame_info_panel1.grid(row=6, column=0, rowspan=11, columnspan=5)

        # Define grid 11 x 5
        info1_rows = 0
        while info1_rows < 11:
            self.frame_info_panel1.rowconfigure(info1_rows, minsize=25)
            info1_rows += 1

        info1_column = 0
        while info1_column < 5:
            self.frame_info_panel1.columnconfigure(info1_column, minsize=47.5)
            info1_column += 1

        # *Info Panel 2 Frame Construction ------------------------------

        self.frame_info_panel2 = ttk.Frame(
            self.master, relief=FLAT, style='TFrame')
        self.frame_info_panel2.config()
        self.frame_info_panel2.grid(row=6, column=5, rowspan=11, columnspan=5)

        # Define grid 11 x 5
        info2_rows = 0
        while info2_rows < 11:
            self.frame_info_panel2.rowconfigure(info2_rows, minsize=25)
            info2_rows += 1

        info2_column = 0
        while info2_column < 5:
            self.frame_info_panel2.columnconfigure(info2_column, minsize=47.5)
            info2_column += 1

        # ******************************** Welcome Widgets Frames *******************************

        # Logo Display in the Welcome Section
        self.login_logo = PhotoImage(file='assets/main_logo-01.png')
        self.login_logo = self.login_logo.subsample(4, 4)
        self.top_logo = ttk.Label(self.frame_welcome,
                                  image=self.login_logo)

        # Welcome Label
        self.header_label = ttk.Label(self.frame_welcome,
                                      text='Set Your Clocked Habits',
                                      style='Header.TLabel')

        # Geometrtic Distribution
        self.top_logo.grid(row=1, column=1, rowspan=2, columnspan=2)
        self.header_label.grid(row=1, column=3, rowspan=2, columnspan=6)

        # ******************************** Top1 Frames *******************************

        # Labels Top1
        self.top1_main1_label = ttk.Label(self.frame_top1,
                                          text='MY HABITS',
                                          style='WhiteOnPink.TLabel',
                                          anchor="center")

        # Geometrtic Distribution
        self.top1_main1_label.grid(
            row=0, column=0, rowspan=2, columnspan=10, sticky='nesw')

        # ******************************** Info1 Frames *******************************

        self.work_habits_list = ['', '', '', '', '']

        for i, v in enumerate(self.user_info['work_habits']):
            self.work_habits_list[i] = v[1] + ' / ' + str(v[0]) + 'min.'

        self.active_habits_lsit = list(filter(None, self.work_habits_list))

        # 1 Label
        self.habit_one = self.work_habits_list[0]
        self.one_label = ttk.Label(
            self.frame_info_panel1, text=self.habit_one, style='WhiteOnGreenSmall.TLabel', anchor=CENTER)

        # 2 Label
        self.habit_two = self.work_habits_list[1]
        self.two_label = ttk.Label(
            self.frame_info_panel1, text=self.habit_two, style='BoldTextOnWhite.TLabel', anchor=CENTER)

        # 3 Label
        self.habit_three = self.work_habits_list[2]
        self.three_label = ttk.Label(
            self.frame_info_panel1, text=self.habit_three, style='WhiteOnGreenSmall.TLabel', anchor=CENTER)

        # 4 Label
        self.habit_four = self.work_habits_list[3]
        self.four_label = ttk.Label(
            self.frame_info_panel1, text=self.habit_four, style='BoldTextOnWhite.TLabel', anchor=CENTER)

        # 5 Label
        self.habit_five = self.work_habits_list[4]
        self.five_label = ttk.Label(
            self.frame_info_panel1, text=self.habit_five, style='WhiteOnGreenSmall.TLabel', anchor=CENTER)

        self.one_label.grid(row=1, column=0, rowspan=2,
                            columnspan=5, sticky='nesw')
        self.two_label.grid(row=3, column=0, rowspan=2,
                            columnspan=5, sticky='nesw')
        self.three_label.grid(row=5, column=0, rowspan=2,
                              columnspan=5, sticky='nesw')
        self.four_label.grid(row=7, column=0, rowspan=2,
                             columnspan=5, sticky='nesw')
        self.five_label.grid(row=9, column=0, rowspan=2,
                             columnspan=5, sticky='nesw')

        # ******************************** Info2 Frames *******************************

        # Frequency Label
        self.frequency_label = ttk.Label(
            self.frame_info_panel2, text='Frequency(Minutes):', style='BoldTextOnWhite.TLabel')

        # SpinBox for Frecuency
        self.frequency_chosen = IntVar()
        self.frequency_spinbox = Spinbox(
            self.frame_info_panel2, from_=0, to=60, textvariable=self.frequency_chosen, state='readonly', width=5)

        # Activity Label
        self.activity_label = ttk.Label(
            self.frame_info_panel2, text='Activity:', style='BoldTextOnWhite.TLabel')

        # Entry for Activity
        self.entry_activity = ttk.Entry(
            self.frame_info_panel2, width=10, font=('Arial', 10))

        # Button Add Habit
        self.add_habit_button = ttk.Button(self.frame_info_panel2,
                                           text='Add Habit!',
                                           style='BlueButton.TButton',
                                           command=self.add_habit)

        # Active Habits Label
        self.active_habits_label = ttk.Label(
            self.frame_info_panel2, text='Active Habits:', style='BoldTextOnWhite.TLabel')

        # Combobox for Active Habits
        self.todelete_habit = StringVar()
        self.active_habits_combobox = ttk.Combobox(
            self.frame_info_panel2, textvariable=self.todelete_habit, width=5)

        self.active_habits_combobox.config(values=self.active_habits_lsit)

        # Button Delete
        self.delete_habit_button = ttk.Button(self.frame_info_panel2,
                                              text='Delete Habit',
                                              style='BlueButton.TButton',
                                              command=self.delete_habit)

        self.frequency_label.grid(
            row=1, column=1, rowspan=1, columnspan=2, sticky='w')
        self.frequency_spinbox.grid(
            row=2, column=1, rowspan=1, columnspan=2, sticky='nesw')
        self.activity_label.grid(
            row=3, column=1, rowspan=1, columnspan=2, sticky='w')
        self.entry_activity.grid(
            row=4, column=1, rowspan=1, columnspan=2, sticky='nesw')
        self.add_habit_button.grid(
            row=5, column=1, rowspan=1, columnspan=2, sticky='nesw')
        self.active_habits_label.grid(
            row=7, column=1, rowspan=1, columnspan=2, sticky='w')
        self.active_habits_combobox.grid(
            row=8, column=1, rowspan=1, columnspan=2, sticky='nesw')
        self.delete_habit_button.grid(
            row=9, column=1, rowspan=1, columnspan=2, sticky='nesw')

    #! ******************************** Methods *******************************

    def add_habit(self):
        ''' This method adds a clocked habit'''

        # Get all values from form
        self.frequency = int(self.frequency_spinbox.get())
        self.activity = self.entry_activity.get()

        valid_submission = True

        # Check for excess characters
        if len(self.activity) > 15:
            messagebox.showinfo(title='Error',
                                message='Error: Max. allowed characters for Activiy = 15',
                                icon='warning')

            valid_submission = False

        # Check for excess characters
        if self.frequency == 0:
            messagebox.showinfo(title='Error',
                                message='Please Fill Frequency',
                                icon='warning')

            valid_submission = False

        # Check for excess characters
        if len(self.activity) == 0:
            messagebox.showinfo(title='Error',
                                message='Please Fill Activity',
                                icon='warning')

            valid_submission = False

        # Proceed addding habit to database
        if valid_submission == True:

            if len(self.user_info['work_habits']) >= 5:
                messagebox.showinfo(title='Error',
                                    message='Maximun Number of Habits Reached',
                                    icon='warning')

                valid_submission = False
                self.entry_activity.delete(0, 'end')
                self.frequency_chosen.set(0)

            else:
                self.user_info['work_habits'].append(
                    [self.frequency, self.activity])

        if valid_submission == True:

            # Save updated USER_INFO database
            self.myDataBase.update(self.user_info)

            self.work_habits_list = ['', '', '', '', '']

            for i, v in enumerate(self.user_info['work_habits']):
                self.work_habits_list[i] = v[1] + ' / ' + str(v[0]) + 'min.'

            self.active_habits_lsit = list(
                filter(None, self.work_habits_list))

            # 1 Label
            self.habit_one = self.work_habits_list[0]
            self.one_label.configure(text=self.habit_one)

            # 2 Label
            self.habit_two = self.work_habits_list[1]
            self.two_label.configure(text=self.habit_two)

            # 3 Label
            self.habit_three = self.work_habits_list[2]
            self.three_label.configure(text=self.habit_three)

            # 4 Label
            self.habit_four = self.work_habits_list[3]
            self.four_label.configure(text=self.habit_four)

            # 5 Label
            self.habit_five = self.work_habits_list[4]
            self.five_label.configure(text=self.habit_five)

            # Combobox
            self.active_habits_combobox.config(
                values=self.active_habits_lsit)

            self.entry_activity.delete(0, 'end')
            self.frequency_chosen.set(0)

    def delete_habit(self):
        ''' This method deletes a clocked habit'''

        # Get all values from form
        self.selected_habit_deletion = self.active_habits_combobox.get()
        self.selected_habit_deletion = self.selected_habit_deletion.split('/')
        self.selected_habit_deletion = self.selected_habit_deletion[0]
        self.selected_habit_deletion = self.selected_habit_deletion.strip()

        for item in self.user_info['work_habits']:
            if item[1] == self.selected_habit_deletion:
                self.user_info['work_habits'].remove(item)
                break

        self.myDataBase.update(self.user_info)

        self.work_habits_list = ['', '', '', '', '']

        for i, v in enumerate(self.user_info['work_habits']):
            self.work_habits_list[i] = v[1] + ' / ' + str(v[0]) + 'min.'

        self.active_habits_lsit = list(
            filter(None, self.work_habits_list))

        # 1 Label
        self.habit_one = self.work_habits_list[0]
        self.one_label.configure(text=self.habit_one)

        # 2 Label
        self.habit_two = self.work_habits_list[1]
        self.two_label.configure(text=self.habit_two)

        # 3 Label
        self.habit_three = self.work_habits_list[2]
        self.three_label.configure(text=self.habit_three)

        # 4 Label
        self.habit_four = self.work_habits_list[3]
        self.four_label.configure(text=self.habit_four)

        # 5 Label
        self.habit_five = self.work_habits_list[4]
        self.five_label.configure(text=self.habit_five)

        # Combobox
        self.active_habits_combobox.config(
            values=self.active_habits_lsit)

        self.active_habits_combobox.set('')
