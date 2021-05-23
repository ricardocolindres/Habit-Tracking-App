# Header File: main.py
# Welcome / LogIn Window for Ness.
# History:
# Date    Programmer   - Description
# ---------- ---------- ----------------------------
# 05/04/2021     Ricardo Josue Colindres      - Created

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from database import FullDatabase
from styles import Styles
import re


class SingUp:

    #! ******************************** Properties *******************************

    def __init__(self, master):

        # ******************************** Main Window *******************************

        self.master = master
        self.master.title('Ness')
        self.master.resizable(False, False)
        self.master.geometry("950x600")

        # Main Background Image

        self.background_image = PhotoImage(file='assets/background_main.png')
        self.background_image = self.background_image.subsample(4, 4)
        self.background_label = ttk.Label(
            self.master, image=self.background_image, borderwidth=0)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # ******************************** Define Styles *******************************

        self.s = Styles()

        # ******************************** LogIn Frame *******************************

        # *Login Frame Construction
        self.frame_login = ttk.Frame(
            self.master, relief=FLAT, style='Maron.TFrame')
        self.frame_login.config(padding=(40, 10))
        self.frame_login.place(x=590, y=0)

        # Logo Display in the Login Section
        self.login_logo = PhotoImage(file='assets/logo_main-01.png')
        self.login_logo = self.login_logo.subsample(3, 3)
        self.top_logo = ttk.Label(
            self.frame_login, image=self.login_logo, style='BlackOnMaron.TLabel')

        # Name Label
        self.name_label = ttk.Label(
            self.frame_login, text='Name:', style='BlackOnMaron.TLabel')

        # Entry for Name
        self.entry_name = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10))

        # Last Name Label
        self.lastname_label = ttk.Label(
            self.frame_login, text='Last Name:', style='BlackOnMaron.TLabel')

        # Entry for Last Name
        self.entry_lastname = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10))

        # Username Label
        self.username_label = ttk.Label(
            self.frame_login, text='Email:', style='BlackOnMaron.TLabel')

        # Entry for Username
        self.entry_username = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10))

        # Password Label
        self.password_label = ttk.Label(
            self.frame_login, text='Password:', style='BlackOnMaron.TLabel')

        # Entry for Password
        self.entry_password = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10), show='*')

        # Birthday Label
        self.birthday_label = ttk.Label(
            self.frame_login, text='Birthday:', style='BlackOnMaron.TLabel')

        # Combobox for Birth Month
        self.birth_month = StringVar()
        self.month_combobox = ttk.Combobox(
            self.frame_login, textvariable=self.birth_month, width=5)
        self.month_combobox.config(values=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                           'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

        # SpinBox for Birth Day
        self.birth_day = IntVar()
        self.birth_day.set(15)
        self.day_spinbox = Spinbox(
            self.frame_login, from_=1, to=31, textvariable=self.birth_day, width=5, state='readonly', readonlybackground='white')

        # SpinBox for Birth Year
        self.birth_year = IntVar()
        self.birth_year.set(1990)
        self.year_spinbox = Spinbox(
            self.frame_login, from_=1960, to=2050, textvariable=self.birth_year, width=5,  state='readonly', readonlybackground='white')

        # Weight Label
        self.weight_label = ttk.Label(
            self.frame_login, text='Weight (Lbs):', style='BlackOnMaron.TLabel')

        # SpinBox for Weight
        self.weight_user = IntVar()
        self.weight_user.set(150)
        self.weight_spinbox = Spinbox(
            self.frame_login, from_=80, to=500, textvariable=self.weight_user, state='readonly', width=7, readonlybackground='white')

        # Height Label
        self.height_label = ttk.Label(
            self.frame_login, text='Height (cm):', style='BlackOnMaron.TLabel')

        # SpinBox for Height
        self.height_user = IntVar()
        self.height_user.set(170)
        self.height_spinbox = Spinbox(
            self.frame_login, from_=100, to=300, textvariable=self.height_user, state='readonly', width=7, readonlybackground='white')

        # Height Label
        self.gender_label = ttk.Label(
            self.frame_login, text='Gender:', style='BlackOnMaron.TLabel')

        # Combobox for Active Habits
        self.genders = ['Male', 'Female']
        self.gender_variable = StringVar()
        self.gender_combobox = ttk.Combobox(
            self.frame_login, textvariable=self.gender_variable, width=5)

        self.gender_combobox.config(values=self.genders)

        # Button Sign Up
        self.login_button = ttk.Button(self.frame_login,
                                       text='Sign Up!',
                                       style='PinkButton.TButton',
                                       command=self.submit)

        # Geometrtic Distribution
        self.top_logo.grid(row=0, column=0, columnspan=3)
        self.name_label.grid(row=1, column=0, columnspan=3, sticky='w')
        self.entry_name.grid(row=2, column=0, columnspan=3, ipady=8)
        self.lastname_label.grid(row=3, column=0, columnspan=3, sticky='w')
        self.entry_lastname.grid(row=4, column=0, columnspan=3, ipady=8)
        self.username_label.grid(row=5, column=0, columnspan=3, sticky='w')
        self.entry_username.grid(row=6, column=0, columnspan=3, ipady=8)
        self.password_label.grid(row=7, column=0, columnspan=3, sticky='w')
        self.entry_password.grid(row=8, column=0, columnspan=3, ipady=8)
        self.birthday_label.grid(row=9, column=0, columnspan=3, sticky='w')
        self.month_combobox.grid(row=10, column=0, ipady=3, sticky='w')
        self.day_spinbox.grid(row=10, column=1, ipady=3)
        self.year_spinbox.grid(row=10, column=2, ipady=3, sticky='e')
        self.weight_label.grid(row=11, column=0, columnspan=1, sticky='w')
        self.height_label.grid(row=11, column=2, columnspan=1, sticky='e')

        self.weight_spinbox.grid(row=12, column=0,
                                 columnspan=1, ipady=3, sticky='w')
        self.height_spinbox.grid(row=12, column=2,
                                 columnspan=1, ipady=3, sticky='e')

        self.gender_label.grid(row=13, column=0, columnspan=3, sticky='w')

        self.gender_combobox.grid(row=14, column=0,
                                  columnspan=3, ipady=3, sticky='ew')
        self.login_button.grid(row=15, column=0, columnspan=3, ipady=3,
                               pady=20, sticky='nsew')

        # ******************************** Footer Frame *******************************

        # *Footer Frame Construction
        self.frame_footer = ttk.Frame(self.master, relief=FLAT, style='TFrame')
        self.frame_footer.config(padding=(0, 15))
        self.frame_footer.pack(fill=X, side=BOTTOM)

        # Button Sign Up
        ttk.Button(self.frame_footer, text='Back to LogIn!', style='PinkButton.TButton',
                   command=self.load_Login).grid(row=0, column=2)

        # Copyright
        ttk.Label(self.frame_footer, text='Welcome to Ness. Please review our Privacy Notice. © 2021, Ness, Inc.',
                  style='TextOnWhite.TLabel').grid(row=0, column=0, padx=35)

        # Error Message
        self.error_label = ttk.Label(self.frame_footer,
                                     text='Login to see your profile!',
                                     style='BoldTextOnWhite.TLabel')
        self.error_label.grid(row=0, column=1, padx=45)

        # ******************************** Actions *******************************

    #! ******************************** Methods *******************************

    def load_Login(self):
        ''' This method return the user to the LogIn portal'''

        from main import Welcome
        self.frame_login.destroy()
        self.frame_footer.destroy()
        self.background_label.destroy()

        # * LOAD NEW CLASS (SIGNUP) TO ROOT
        self.another = Welcome(self.master)

    def submit(self):
        '''This function registers a new user. All critirias must be met.'''

        # Get all values from form
        self.name = self.entry_name.get()
        self.lastname = self.entry_lastname.get()
        self.username = self.entry_username.get()
        self.password = self.entry_password.get()
        self.month = self.birth_month.get()
        self.day = self.birth_day.get()
        self.year = self.birth_year.get()
        self.weight = self.weight_user.get()
        self.height = self.height_user.get()
        self.selected_gender = self.gender_combobox.get()

        # Set special values
        calendar_map = {'Jan': 1, 'Feb': 2, 'Mar': 3,
                        'Apr': 4, 'May': 5, 'Jun': 6,
                        'Jul': 7, 'Aug': 8, 'Sep': 9,
                        'Oct': 10, 'Nov': 11, 'Dec': 12}

        self.month_number = ''.join(
            [str(v) for k, v in calendar_map.items() if self.month == k])
        self.user_fullname = self.name + ' ' + self.lastname
        self.birthday_date = str(self.year) + '-' + \
            self.month_number + '-' + str(self.day)

        # Set dicionarties
        user_info = {
            "username": self.username,
            "name": self.name,
            "lastname": self.lastname,
            "fullname": self.user_fullname,
            "birthday": self.birthday_date,
            "weight": [self.weight],
            "height": self.height,
            "gender": self.selected_gender,
            "work_habits": [[1, "Drink Water"], [5, "Stand Up"]],

            "work_habits_data": [],

            "user_habits": [

                ["Drink Water", 8.0, [
                    "Monday", "Tuesday", "Wednesday", "Thursday",
                    "Friday", "Saturday", "Sunday"], "all_time", 0],

                ["Exericise", 1.0, [
                 "Monday", "Tuesday", "Wednesday", "Thursday",
                 "Friday", "Saturday", "Sunday"], "morning", 0]

            ],
            "user_habits_data": [],
            "user_habits_streak": [],
            "password": self.password
        }

        user_credentials = {
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "lastname": self.lastname,
            "birthday": self.birthday_date
        }

        valid_submission = True

        # Check for empty values
        for k, v in user_info.items():
            if v == '':
                messagebox.showinfo(title='Error',
                                    message='Error: Please fill ALL fields',
                                    icon='warning')

                self.error_label.config(style='Error.TLabel',
                                        text="Error: Please fill ALL fields.")
                valid_submission = False
                break

        # Check for valid email format
        if valid_submission == True:
            if not re.match(r"[^@\s]+@[^@\s]+\.[a-zA-Z0-9]+$", self.username):
                messagebox.showinfo(title='Error',
                                    message='Error: Please enter a valid email.',
                                    icon='warning')

                self.error_label.config(style='Error.TLabel',
                                        text="Error: Please enter a valid email!.")
                valid_submission = False

        # Check if email exists already
        if valid_submission == True:

            # Load Databases
            self.full_database = FullDatabase()
            credentials = self.full_database.load_credentials()
            user = self.full_database.load_users_info()

            for i, v in enumerate(credentials):
                if credentials[i]['username'] == self.username:

                    messagebox.showinfo(title='Error',
                                        message='Error: Email Exists Already.',
                                        icon='warning')

                    self.error_label.config(style='Error.TLabel',
                                            text="Error: Please enter a NEW email!.")
                    valid_submission = False

        # Proceed with signin up process
        if valid_submission == True:

            # Delete password from USER_INFO dictionary
            del user_info['password']

            credentials.append(user_credentials)
            user.append(user_info)

            # Update DataBase
            self.full_database.update_database(credentials, user)

            from habits import Habits
            self.frame_login.destroy()
            self.frame_footer.destroy()
            self.background_label.destroy()

            # * LOAD NEW CLASS (SIGNUP) TO ROOT
            self.another = Habits(self.master, self.username)
