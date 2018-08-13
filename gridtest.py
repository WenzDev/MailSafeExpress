import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

       # self.attributes('-fullscreen', True)

        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        frame.configure(background='#0066AB')


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font9 = "-family Arial -size 12 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        self.rowconfigure(0, minsize=60, weight=1)
        self.rowconfigure(1, minsize=60, weight=1)
        self.rowconfigure(2, minsize=60, weight=1)
        self.rowconfigure(3, minsize=0, weight=1)
        self.rowconfigure(4, minsize=0, weight=1)
        self.rowconfigure(5, minsize=60, weight=1)
        self.rowconfigure(6, minsize=60, weight=1)
        self.rowconfigure(7, minsize=60, weight=1)
        self.rowconfigure(8, minsize=60, weight=1)
        self.rowconfigure(9, minsize=60, weight=1)
        self.rowconfigure(10, minsize=60, weight=1)
        self.columnconfigure(0, minsize=60, weight=1)
        self.columnconfigure(1, minsize=60, weight=1)
        self.columnconfigure(2, minsize=60, weight=1)
        self.columnconfigure(3, minsize=60, weight=1)
        self.columnconfigure(4, minsize=60, weight=1)
        self.columnconfigure(5, minsize=20, weight=1)
        self.columnconfigure(6, minsize=60, weight=1)
        self.columnconfigure(7, minsize=60, weight=1)
        self.columnconfigure(8, minsize=60, weight=1)
        self.columnconfigure(9, minsize=60, weight=1)
        self.columnconfigure(10, minsize=60, weight=1)
        label = tk.Label(self, text="Envelope Security Code", font=font9)
        label.configure(bg='#0066AB', fill="white")
        label.grid(row=3, column=5, sticky=N+E+S+W)

        e_sec = tk.Entry(self, font=font9)
        e_sec.grid(row=4, column=5, sticky=E+W)

        button1 = ttk.Button(self, text="Start Over")
        button1.grid(row=0, column=0, columnspan=2 , sticky=N+E+S+W)

        button2 = ttk.Button(self, text="Start Over")
        button2.grid(row=0, column=2, sticky=N+E+S+W)
        button3 = ttk.Button(self, text="Start Over")
        button3.grid(row=0, column=3, sticky=N+E+S+W)
        button4 = ttk.Button(self, text="Start Over")
        button4.grid(row=0, column=4, sticky=N+E+S+W)
        button5 = ttk.Button(self, text="Start Over")
        button5.grid(row=0, column=5, sticky=N+E+S+W)
        button6 = ttk.Button(self, text="Start Over")
        button6.grid(row=0, column=6, sticky=N+E+S+W)
        button7 = ttk.Button(self, text="Start Over")
        button7.grid(row=0, column=7, sticky=N+E+S+W)
        button8 = ttk.Button(self, text="Start Over")
        button8.grid(row=0, column=8, sticky=N+E+S+W)
        button9 = ttk.Button(self, text="Start Over")
        button9.grid(row=0, column=9, sticky=N+E+S+W)
        button10 = ttk.Button(self, text="Start Over")
        button10.grid(row=0, column=10, sticky=N+E+S+W)
        button11 = ttk.Button(self, text="Start Over")
        button11.grid(row=1, column=0, sticky=N+E+S+W)
        button13 = ttk.Button(self, text="Start Over")
        button13.grid(row=2, column=0, sticky=N+E+S+W)
        button14 = ttk.Button(self, text="Start Over")
        button14.grid(row=3, column=0, sticky=N+E+S+W)
        button15 = ttk.Button(self, text="Start Over")
        button15.grid(row=4, column=0, sticky=N+E+S+W)
        button16 = ttk.Button(self, text="Start Over")
        button16.grid(row=5, column=0, sticky=N+E+S+W)
        button17 = ttk.Button(self, text="Start Over")
        button17.grid(row=6, column=0, sticky=N+E+S+W)
        button18 = ttk.Button(self, text="Start Over")
        button18.grid(row=7, column=0, sticky=N+E+S+W)
        button19 = ttk.Button(self, text="Start Over")
        button19.grid(row=8, column=0, sticky=N+E+S+W)
        button20 = ttk.Button(self, text="Start Over")
        button20.grid(row=9, column=0, sticky=N+E+S+W)
        button21 = ttk.Button(self, text="Start Over")
        button21.grid(row=10, column=0, sticky=N+E+S+W)

        btn_Next1 = ttk.Button(self, text="Next",
                               command=lambda: controller.show_frame(PageOne))
        btn_Next1.grid(row=10, column=9, columnspan=2, sticky=N+E+S+W)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        font9 = "-family Arial -size 12 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        bs = ttk.Style()
        bs.configure('my.TButton', font=font9)

        button1 = ttk.Button(self, text="Back to Home", style='my.TButton',
                            command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0.86, rely=0.93, height=54, width=247)

        button2 = ttk.Button(self, text="Page Two", style='my.TButton',
                            command=lambda: controller.show_frame(PageTwo))
        button2.place(relx=0.01, rely=0.01, height=54, width=247)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        font9 = "-family Arial -size 12 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        bs = ttk.Style()
        bs.configure('my.TButton', font=font9)
        button1 = ttk.Button(self, text="Back to Home", style='my.TButton',
                             command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0.86, rely=0.93, height=54, width=247)

        button2 = ttk.Button(self, text="Back to Page 1", style='my.TButton',
                             command=lambda: controller.show_frame(PageOne))
        button2.place(relx=0.01, rely=0.01, height=54, width=247)
        # first name
        self.e_fname = Entry(self)
        self.e_fname.place(relx=0.21, rely=0.18, height=40, relwidth=0.27)
        self.l_fname = Label(self, text='''First Name:''', font=font9,bg='#0066AB')
        self.l_fname.place(relx=0.055, rely=0.13, height=40, width=514)
        # last name
        self.e_lname = Entry(self)
        self.e_lname.place(relx=0.55, rely=0.18, height=40, relwidth=0.27)
        self.l_lname = Label(self, text='''Last Name:''', font=font9,bg='#0066AB')
        self.l_lname.place(relx=0.395, rely=0.13, height=40, width=514)
        # email
        self.e_mail = Entry(self)
        self.e_mail.place(relx=0.21, rely=0.29,height=40, relwidth=0.57)
        self.l_mail = Label(self, text='''Email Address:''', font=font9, bg='#0066AB')
        self.l_mail.place(relx=0.06, rely=0.24, height=31, width=514)
        # phone number
        self.e_phone = Entry(self)
        self.e_phone.place(relx=0.21, rely=0.40, height=40, relwidth=0.57)
        self.l_phone = Label(self, text= '''Phone Number:''', font=font9, bg='#0066AB')
        self.l_phone.place(relx=0.06, rely=0.36, height=31, width=514)
        # Address
        self.e_saddress = Entry(self)
        self.e_saddress.place(relx=0.21, rely=0.51, height=40, relwidth=0.57)
        self.adress = Label(self, text='''Address:''', font=font9, bg='#0066AB')
        self.adress.place(relx=0.05, rely=0.46, height=31, width=514)
        # Address Line 2
        self.e_saddress2 = Entry(self)
        self.e_saddress2.place(relx=0.21, rely=0.62, height=40, relwidth=0.57)
        self.adress2 = Label(self, text='''Address Confirmation:''', font=font9, bg='#0066AB')
        self.adress2.place(relx=0.075, rely=0.57, height=31, width=514)
        # State
        self.state = Label(self, text='''State:''', font=font9, bg='#0066AB')
        self.state.place(relx=0.085, rely=0.685, height=40, relwidth=0.27)
        self.state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                           "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                           "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                           "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                           "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                           "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                           "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        self.combo_state = ttk.Combobox(self, values=self.state_list)
        self.combo_state.place(relx=0.52, rely=0.69, height=40, relwidth=0.27)
        # City
        self.e_city = Entry(self)
        self.e_city.place(relx=0.21, rely=0.69, height=40, relwidth=0.27)
        # Zip Code
        self.e_zip = Entry(self)
        self.e_zip.place(relx=0.21, rely=0.75, height=40, relwidth=0.24)
        # Country
        self.country_list = ["United States", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
                             "Antigua & Deps", "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan",
                             "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize",
                             "Benin", "Bhutan", "Bolivia", "Bosnia Herzegovina", "Botswana", "Brazil", "Brunei",
                             "Bulgaria", "Burkina", "Burma", "Burundi", "Cambodia", "Cameroon", "Canada", "Cape Verde",
                             "Central African Rep", "Chad", "Chile", "People's Republic of China", "Republic of China",
                             "Colombia", "Comoros", "Democratic Republic of the Congo", "Republic of the Congo",
                             "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Danzig", "Denmark",
                             "Djibouti", "Dominica", "Dominican Republic", "East Timor", "Ecuador", "Egypt",
                             "El Salvador", "Equatorial Guinea", "Eritrea  ", "Estonia", "Ethiopia", "Fiji",
                             "Finland", "France", "Gabon", "Gaza Strip", "The Gambia" , "Georgia", "Germany",
                             "Ghana", "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
                             "Haiti", "Holy Roman Empire", "Honduras", "Hungary", "Iceland", "India", "Indonesia",
                             "Iran", "Iraq", "Republic of Ireland", "Israel", "Italy", "Ivory Coast", "Jamaica",
                             "Japan", "Jonathanland", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "North Korea",
                             "South Korea", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
                             "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Macedonia", "Madagascar",
                             "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
                             "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco",
                             "Mongolia", "Montenegro", "Morocco", "Mount Athos", "Mozambique", "Namibia",
                             "Nauru", "Nepal", "Newfoundland", "Netherlands", "New Zealand", "Nicaragua",
                             "Niger", "Nigeria", "Norway", "Oman", "Ottoman Empire", "Pakistan", "Palau",
                             "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland",
                             "Portugal", "Prussia", "Qatar", "Romania", "Rome", "Russian Federation",
                             "Rwanda", "St Kitts & Nevis", "St Lucia", "Saint Vincent & the, Grenadines",
                             "Samoa", "San Marino", "Sao Tome & Principe", "Saudi Arabia", "Senegal",
                             "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
                             "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan",
                             "Suriname", "Swaziland", "Sweden", "Switzerland", "Syria", "Tajikistan",
                             "Tanzania", "Thailand", "Togo", "Tonga", "Trinidad & Tobago", "Tunisia",
                             "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
                             "United Kingdom", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela",
                             "Vietnam", "Yemen", "Zambia", "Zimbabwe"]
        self.combo_country = ttk.Combobox(self, values=self.country_list)
        self.combo_country.place(relx=0.52, rely=0.75, relheight=0.04, relwidth=0.27)




app = SeaofBTCapp()
app.mainloop()
