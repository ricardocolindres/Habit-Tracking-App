from tkinter import *
from tkinter import ttk
from platform import system


class Styles:

    def __init__(self):

        self.operating_system = system()

        if self.operating_system == 'Darwin':

            self.style = ttk.Style()
            self.style.theme_use('clam')

            # General frame styles
            self.style.configure('TFrame', background='white')
            self.style.configure('TLabel', background='white')
            self.style.configure('Yellow.TFrame', background='#fffff3')
            self.style.configure('Maron.TFrame', background='#efefe1')
            self.style.configure('Pink.TFrame', background='#f27272')
            self.style.configure('Blue.TFrame', background='#8ea3ae')

            # Welcome frame styless
            self.style.configure('Header.TLabel',
                                 foreground='#6d6e71',
                                 font=(('Helvetica', 23, '')))

            self.style.configure('Sub.Header.TLabel',
                                 foreground='#6d6e71',
                                 font=(('Arial', 15, '')))

            self.style.configure('GreenButton.TButton',
                                 foreground='white',
                                 background='#bbceb2',
                                 highlightthickness='0',
                                 font=('Arial', 11, 'bold'))

            self.style.map('GreenButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('active', 'white'),
                                       ('pressed', 'white')],
                           background=[('disabled', '#58595b'),
                                       ('pressed', '#8ea3ae'),
                                       ('active', '#8ea3ae')])

            self.style.configure('BlueButton.TButton',
                                 foreground='white',
                                 background='#8ea3ae',
                                 highlightthickness='0',
                                 font=('Arial', 11, 'bold'),
                                 relief=FLAT)

            self.style.map('BlueButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#808184'),
                                       ('pressed', '#f37b75'),
                                       ('active', '#f37b75')])

            self.style.configure('PinkButton.TButton',
                                 foreground='white',
                                 background='#f27272',
                                 highlightthickness='0',
                                 font=('Helvetica', 11, 'bold'))

            self.style.map('PinkButton.TButton',
                           foreground=[('disabled', 'yellow'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', 'black'),
                                       ('pressed', '#8ea3ae'),
                                       ('active', '#8ea3ae')],)

            self.style.configure('WhiteButton.TButton',
                                 foreground='white',
                                 background='white',
                                 highlightthickness='0',
                                 font=('Arial', 11, 'bold'),
                                 relief=FLAT)

            self.style.map('WhiteButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')])

            self.style.configure('YellowButton.TButton',
                                 foreground='black',
                                 background='#fffff3',
                                 highlightthickness='0',
                                 font=('Arial', 11, 'bold'),
                                 relief=FLAT)

            self.style.map('YellowButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#efefe1'),
                                       ('pressed', '#efefe1'),
                                       ('active', '#efefe1')])

            self.style.configure('YellowButton2.TButton',
                                 foreground='black',
                                 background='#efefe1',
                                 highlightthickness='0',
                                 font=('Arial', 11, 'bold'),
                                 relief=RAISED)

            self.style.map('YellowButton2.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#efefe1'),
                                       ('pressed', '#efefe1'),
                                       ('active', '#efefe1')])

            self.style.configure('WhiteOnPink.TLabel',
                                 foreground='white',
                                 background='#f37b75',
                                 font=('Arial', 13, 'bold'))

            self.style.configure('PinkOnYellow.TLabel',
                                 background='#fffff3',
                                 foreground='#f27272',
                                 font=('Arial', 12, 'bold'))

            self.style.configure('WhiteOnGreen.TLabel',
                                 background='#bbceb2',
                                 foreground='white',
                                 font=('Arial', 14, 'bold'))

            self.style.configure('WhiteOnGreenSmall.TLabel',
                                 background='#bbceb2',
                                 foreground='white',
                                 font=('Arial', 12, 'bold'))

            self.style.configure('Stopwatch.TLabel',
                                 background='#fffff3',
                                 foreground='#58595b',
                                 font=('Arial', 38, 'bold'))

            self.style.configure('TextOnYellow.TLabel',
                                 background='#fffff3',
                                 foreground='#6d6e71',
                                 justify=CENTER,
                                 font=('Arial', 12,))

            self.style.configure('BoldTextOnYellow.TLabel',
                                 background='#fffff3',
                                 foreground='#6d6e71',
                                 justify=CENTER,
                                 font=('Arial', 12, 'bold'))

            self.style.configure('BoldTextOnWhite.TLabel',
                                 background='white',
                                 foreground='#6d6e71',
                                 justify=LEFT,
                                 font=('Arial', 12, 'bold'))

            self.style.configure('BoldTextOnGreen.TLabel',
                                 background='#bbceb2',
                                 foreground='#6d6e71',
                                 justify=LEFT,
                                 font=('Arial', 12, 'bold'))

            self.style.configure('PinkOnWhiteLarge.TLabel',
                                 background='white',
                                 foreground='#f27272',
                                 font=('Arial', 40, 'bold'))

            self.style.configure('BlackOnWhite.TLabel',
                                 background='white',
                                 foreground='black',
                                 font=('Arial', 11, 'bold'))

            self.style.configure('WhiteOnBlueLarge.TLabel',
                                 background='#8ea3ae',
                                 foreground='white',
                                 font=('Arial', 40, 'bold'))

            self.style.configure('WhiteOnBlue.TLabel',
                                 background='#8ea3ae',
                                 foreground='white',
                                 font=('Arial', 11, 'bold'))

            self.style.configure('PinkOnMaronLarge.TLabel',
                                 background='#efefe1',
                                 foreground='#f27272',
                                 font=('Arial', 40, 'bold'))

            self.style.configure('PinkOnMaronMedium.TLabel',
                                 background='#efefe1',
                                 foreground='#f27272',
                                 font=('Arial', 18, 'bold'))

            self.style.configure('BlackOnMaronMedium.TLabel',
                                 background='#efefe1',
                                 foreground='black',
                                 font=('Arial', 14, 'bold'))

            self.style.configure('BlackOnMaron.TLabel',
                                 foreground='black',
                                 background='#efefe1')

            self.style.configure('TextOnWhite.TLabel',
                                 foreground='black',
                                 background='white')

            self.style.configure('PinkOnWhite.TLabel',
                                 background='white',
                                 font=(('Helvetica', 12, 'bold')),
                                 foreground='#f27272')

            self.style.configure('PinkOnWhite.TLabel',
                                 background='white',
                                 foreground='#f27272',
                                 font=('Arial', 13, 'bold'))

            self.style.configure('TCheckbutton',
                                 background='#fffff3',
                                 font=('Arial', 11, 'bold'),
                                 foreground='#6d6e71')

            self.style.map('TCheckbutton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', '#f27272'),
                                       ('active', '#f27272')],
                           background=[('disabled', '#f9f9f9'),
                                       ('pressed', '#fffff3'),
                                       ('active', '#fffff3')])

            self.style.configure('Pink.Horizontal.TProgressbar',
                                 background='#f37b75', troughcolor='#a6a8ab')

            # Footer Style

            self.style.configure('FooterHabits.TLabel',
                                 background='#efefe1',
                                 foreground='#808184',
                                 font=('Arial', 11, ''))

        elif self.operating_system == 'Windows':

            self.style = ttk.Style()
            self.style.theme_use('clam')

            # General frame styles
            self.style.configure('TFrame', background='white')
            self.style.configure('TLabel', background='white')
            self.style.configure('Yellow.TFrame', background='#fffff3')
            self.style.configure('Maron.TFrame', background='#efefe1')
            self.style.configure('Pink.TFrame', background='#f27272')
            self.style.configure('Blue.TFrame', background='#8ea3ae')

            # Welcome frame styless
            self.style.configure('Header.TLabel',
                                 foreground='#6d6e71',
                                 font=(('Helvetica', 19, '')))

            self.style.configure('Sub.Header.TLabel',
                                 foreground='#6d6e71',
                                 font=(('Arial', 12, '')))

            self.style.configure('GreenButton.TButton',
                                 foreground='white',
                                 background='#bbceb2',
                                 highlightthickness='0',
                                 font=('Arial', 8, 'bold'))

            self.style.map('GreenButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('active', 'white'),
                                       ('pressed', 'white')],
                           background=[('disabled', '#58595b'),
                                       ('pressed', '#8ea3ae'),
                                       ('active', '#8ea3ae')])

            self.style.configure('BlueButton.TButton',
                                 foreground='white',
                                 background='#8ea3ae',
                                 highlightthickness='0',
                                 font=('Arial', 8, 'bold'),
                                 relief=FLAT)

            self.style.map('BlueButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#808184'),
                                       ('pressed', '#f37b75'),
                                       ('active', '#f37b75')])

            self.style.configure('PinkButton.TButton',
                                 foreground='white',
                                 background='#f27272',
                                 highlightthickness='0',
                                 font=('Helvetica', 8, 'bold'))

            self.style.map('PinkButton.TButton',
                           foreground=[('disabled', 'yellow'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', 'black'),
                                       ('pressed', '#8ea3ae'),
                                       ('active', '#8ea3ae')],)

            self.style.configure('WhiteButton.TButton',
                                 foreground='white',
                                 background='white',
                                 highlightthickness='0',
                                 font=('Arial', 8, 'bold'),
                                 relief=FLAT)

            self.style.map('WhiteButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')])

            self.style.configure('YellowButton.TButton',
                                 foreground='black',
                                 background='#fffff3',
                                 highlightthickness='0',
                                 font=('Arial', 8, 'bold'),
                                 relief=FLAT)

            self.style.map('YellowButton.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#efefe1'),
                                       ('pressed', '#efefe1'),
                                       ('active', '#efefe1')])

            self.style.configure('YellowButton2.TButton',
                                 foreground='black',
                                 background='#efefe1',
                                 highlightthickness='0',
                                 font=('Arial', 8, 'bold'),
                                 relief=RAISED)

            self.style.map('YellowButton2.TButton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', 'white'),
                                       ('active', 'white')],
                           background=[('disabled', '#efefe1'),
                                       ('pressed', '#efefe1'),
                                       ('active', '#efefe1')])

            self.style.configure('WhiteOnPink.TLabel',
                                 foreground='white',
                                 background='#f37b75',
                                 font=('Arial', 10, 'bold'))

            self.style.configure('PinkOnYellow.TLabel',
                                 background='#fffff3',
                                 foreground='#f27272',
                                 font=('Arial', 9, 'bold'))

            self.style.configure('WhiteOnGreen.TLabel',
                                 background='#bbceb2',
                                 foreground='white',
                                 font=('Arial', 11, 'bold'))

            self.style.configure('WhiteOnGreenSmall.TLabel',
                                 background='#bbceb2',
                                 foreground='white',
                                 font=('Arial', 9, 'bold'))

            self.style.configure('Stopwatch.TLabel',
                                 background='#fffff3',
                                 foreground='#58595b',
                                 font=('Arial', 28, 'bold'))

            self.style.configure('TextOnYellow.TLabel',
                                 background='#fffff3',
                                 foreground='#6d6e71',
                                 justify=CENTER,
                                 font=('Arial', 9,))

            self.style.configure('BoldTextOnYellow.TLabel',
                                 background='#fffff3',
                                 foreground='#6d6e71',
                                 justify=CENTER,
                                 font=('Arial', 9, 'bold'))

            self.style.configure('BoldTextOnWhite.TLabel',
                                 background='white',
                                 foreground='#6d6e71',
                                 justify=LEFT,
                                 font=('Arial', 9, 'bold'))

            self.style.configure('BoldTextOnGreen.TLabel',
                                 background='#bbceb2',
                                 foreground='#6d6e71',
                                 justify=LEFT,
                                 font=('Arial', 9, 'bold'))

            self.style.configure('PinkOnWhiteLarge.TLabel',
                                 background='white',
                                 foreground='#f27272',
                                 font=('Arial', 30, 'bold'))

            self.style.configure('BlackOnWhite.TLabel',
                                 background='white',
                                 foreground='black',
                                 font=('Arial', 8, 'bold'))

            self.style.configure('WhiteOnBlueLarge.TLabel',
                                 background='#8ea3ae',
                                 foreground='white',
                                 font=('Arial', 30, 'bold'))

            self.style.configure('WhiteOnBlue.TLabel',
                                 background='#8ea3ae',
                                 foreground='white',
                                 font=('Arial', 8, 'bold'))

            self.style.configure('PinkOnMaronLarge.TLabel',
                                 background='#efefe1',
                                 foreground='#f27272',
                                 font=('Arial', 30, 'bold'))

            self.style.configure('PinkOnMaronMedium.TLabel',
                                 background='#efefe1',
                                 foreground='#f27272',
                                 font=('Arial', 15, 'bold'))

            self.style.configure('BlackOnMaronMedium.TLabel',
                                 background='#efefe1',
                                 foreground='black',
                                 font=('Arial', 11, 'bold'))

            self.style.configure('BlackOnMaron.TLabel',
                                 foreground='black',
                                 background='#efefe1')

            self.style.configure('TextOnWhite.TLabel',
                                 foreground='black',
                                 background='white')

            self.style.configure('PinkOnWhite.TLabel',
                                 background='white',
                                 font=(('Helvetica', 9, 'bold')),
                                 foreground='#f27272')

            self.style.configure('PinkOnWhite.TLabel',
                                 background='white',
                                 foreground='#f27272',
                                 font=('Arial', 10, 'bold'))

            self.style.configure('TCheckbutton',
                                 background='#fffff3',
                                 font=('Arial', 8, 'bold'),
                                 foreground='#6d6e71')

            self.style.map('TCheckbutton',
                           foreground=[('disabled', 'white'),
                                       ('pressed', '#f27272'),
                                       ('active', '#f27272')],
                           background=[('disabled', '#f9f9f9'),
                                       ('pressed', '#fffff3'),
                                       ('active', '#fffff3')])

            self.style.configure('Pink.Horizontal.TProgressbar',
                                 background='#f37b75', troughcolor='#a6a8ab')

            # Footer Style

            self.style.configure('FooterHabits.TLabel',
                                 background='#efefe1',
                                 foreground='#808184',
                                 font=('Arial', 8, ''))
