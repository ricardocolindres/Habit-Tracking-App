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


class Welcome:
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
        self.frame_login = ttk.Frame(master, relief=FLAT, style='Maron.TFrame')
        self.frame_login.config(padding=(40, 10))
        self.frame_login.place(x=555, y=80)

        # Logo Display in the Login Section
        self.login_logo = PhotoImage(file='assets/logo_main-01.png')
        self.login_logo = self.login_logo.subsample(3, 3)
        self.top_logo = ttk.Label(
            self.frame_login, image=self.login_logo, style='BlackOnMaron.TLabel')

        # Username Label
        self.user_label = ttk.Label(
            self.frame_login, text='Email:', style='BlackOnMaron.TLabel')

        # Entry for Username
        self.entry_username = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10))

        # Password Label
        self.pass_label = ttk.Label(
            self.frame_login, text='Password:', style='BlackOnMaron.TLabel')

        # Entry for Password
        self.entry_password = ttk.Entry(
            self.frame_login, width=40, font=('Arial', 10), show='*')

        # Button LogIn
        self.login_button = ttk.Button(self.frame_login, text='Log In', style='PinkButton.TButton',
                                       command=self.submit)

        # Geometrtic Distribution
        self.top_logo.grid(row=0, column=0)
        self.user_label.grid(row=1, column=0, sticky='w')
        self.entry_username.grid(row=2, column=0, ipady=8)
        self.pass_label.grid(row=3, column=0, sticky='w')
        self.entry_password.grid(row=4, column=0, ipady=8)
        self.login_button.grid(row=5, column=0, ipady=3,
                               pady=20, sticky='nsew')

        # ******************************** Footer Frame *******************************

        # *Footer Frame Construction
        self.frame_footer = ttk.Frame(self.master, relief=FLAT, style='TFrame')
        self.frame_footer.config(padding=(0, 15))
        self.frame_footer.pack(fill=X, side=BOTTOM)

        # Button Sign Up
        ttk.Button(self.frame_footer, text='New? Sign Up!', style='PinkButton.TButton',
                   command=self.load_signup).grid(row=0, column=2)

        # Copyright
        ttk.Label(self.frame_footer, text='Welcome to Ness. Please review our Privacy Notice. © 2021, Ness, Inc.',
                  style='TextOnWhite.TLabel').grid(row=0, column=0, padx=35)

        # Error Message
        self.error_label = ttk.Label(self.frame_footer,
                                     text='Login to see your profile!',
                                     style='BoldTextOnWhite.TLabel')
        self.error_label.grid(row=0, column=1, padx=45)

    #! ******************************** Methods *******************************

    def load_signup(self):
        ''' This method loads the Sign Up Window'''
        from signup import SingUp
        self.frame_login.destroy()
        self.frame_footer.destroy()
        self.background_label.destroy()

        # * LOAD NEW CLASS (SIGNUP) TO ROOT
        self.another = SingUp(self.master)

    def submit(self):
        '''This function logs in a new user if all critirias are met.'''

        self.username = self.entry_username.get()
        self.password = self.entry_password.get()

        # Test for missing values for logging in

        if self.username == '':
            messagebox.showinfo(title='LogIn Error',
                                message='Enter: Username', icon='warning')

            self.error_label.config(style='PinkOnWhite.TLabel',
                                    text="Error: Please Enter Username")

        elif self.password == '':
            messagebox.showinfo(title='LogIn Error',
                                message='Enter: Password', icon='warning')

            self.error_label.config(style='PinkOnWhite.TLabel',
                                    text="Error: Please Enter Password")

        # If no missing values, proceed to login attempt
        else:
            # Load Credential's Database
            self.full_database = FullDatabase()
            credentials = self.full_database.load_credentials()

            login_status = False

            #Loop in Database
            for i, v in enumerate(credentials):
                if credentials[i]['username'] == self.username:
                    if credentials[i]['password'] == self.password:
                        login_status = True

            # Define Action
            if login_status == True:
                from habits import Habits
                self.frame_login.destroy()
                self.frame_footer.destroy()
                self.background_label.destroy()

                # * LOAD NEW CLASS (SIGNUP) TO ROOT
                self.another = Habits(self.master, self.username)

            else:
                messagebox.showinfo(title='LogIn Error',
                                    message='Username or Password Invalid', icon='warning')

                self.error_label.config(style='PinkOnWhite.TLabel',
                                        text="Username or Password Invalid")


if __name__ == "__main__":

    def main():
        root = Tk()
        welcome = Welcome(root)
        root.mainloop()

    main()
