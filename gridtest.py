import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        self.title("Mailsafe Express v1.0")
        self.iconbitmap(default='mseico256.ico')

        # self.attributes('-fullscreen', True)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, PaymentPage):

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
        self.match = False
        self.securitycode = None
        self.csecuritycode = None
        font9 = "-family Arial -size 24 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        buttonfont = "-family Arial -size 16 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"

        self.rowconfigure(0, minsize=60, weight=0)
        self.rowconfigure(1, minsize=60, weight=1)
        self.rowconfigure(2, minsize=60, weight=1)
        self.rowconfigure(3, minsize=30, weight=0)
        self.rowconfigure(4, minsize=30, weight=0)
        self.rowconfigure(5, minsize=60, weight=1)
        self.rowconfigure(6, minsize=30, weight=0)
        self.rowconfigure(7, minsize=30, weight=0)
        self.rowconfigure(8, minsize=30, weight=1)
        self.rowconfigure(9, minsize=60, weight=1)
        self.rowconfigure(10, minsize=30, weight=1)
        self.columnconfigure(0, minsize=60, weight=1)
        self.columnconfigure(1, minsize=60, weight=1)
        self.columnconfigure(2, minsize=60, weight=1)
        self.columnconfigure(3, minsize=60, weight=1)
        self.columnconfigure(4, minsize=60, weight=1)
        self.columnconfigure(5, minsize=30, weight=1)
        self.columnconfigure(6, minsize=60, weight=1)
        self.columnconfigure(7, minsize=60, weight=1)
        self.columnconfigure(8, minsize=60, weight=1)
        self.columnconfigure(9, minsize=60, weight=1)
        self.columnconfigure(10, minsize=60, weight=1)
        image = PhotoImage(file="msecrop.png")
        l_MSEL = tk.Label(self, image=image)
        l_MSEL.configure(background='#0066AB', borderwidth=0)
        l_MSEL.photo = image
        l_MSEL.grid(row=0, column=5, rowspan=3, sticky=N+E+S+W)

        # Label for ESC
        l_sec = tk.Label(self, text="Envelope Security Code", font=font9)
        l_sec.configure(bg='#0066AB')
        l_sec.configure(foreground="#ffffff")
        l_sec.grid(row=3, column=5, sticky=N+E+W)
        # Entry for Security Code
        self.e_sec = tk.Entry(self, font=font9)
        self.e_sec.grid(row=4, column=4, columnspan=3, sticky=E+W)
        # Label for CSEC
        l_csec = tk.Label(self, text="Confirm Envelope Security Code", font=font9)
        l_csec.configure(foreground="#ffffff")
        l_csec.configure(bg='#0066AB')
        l_csec.grid(row=6, column=5, sticky=N+E+W)
        # Entry for Confirm Security Code
        self.e_csec = tk.Entry(self, font=font9)
        self.e_csec.grid(row=7, column=4, columnspan=3, sticky=E+W)
        # Start Over Button
        button1 = tk.Button(self, text="Start Over")
        button1.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                          borderwidth=2)
        button1.configure(height=3, width=15)
        button1.grid(row=0, column=0, columnspan=2, sticky=N+E+W)
        # Next Page Button
        btn_Next1 = tk.Button(self, text="Next",
                              command=lambda: controller.show_frame(PageOne))
        btn_Next1.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                            relief=SUNKEN)
        btn_Next1.configure(height=3, width=15)
        btn_Next1.grid(row=10, column=9, columnspan=2, sticky=S+E+W)

    def errorsec(self):
        font9 = "-family Arial -size 24 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        popup = tk.Toplevel()
        popup.title("Error")
        popup.configure(background='#0066AB')
        l_error = tk.Label(popup, text="Your security codes don't match!", font=font9, background='#0066AB',
                           foreground="#ffffff")
        l_error.pack(side="top", fill="x", pady=10)
        btn_close = tk.Button(popup, text="Okay", command=popup.destroy)
        btn_close.pack()


    def check_sec(self, controller):
        if self.e_sec.get() == self.e_csec.get():
            print("Success! Your envelope security code is:" + " " + self.e_sec.get())
            l_command = lambda: controller.show_frame(StartPage)
            l_command()
            self.match = True
        else:
            self.errorsec()
            print("Error: Type that again!")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.rowconfigure(0, minsize=60, weight=0)
        self.rowconfigure(1, minsize=100, weight=1)
        self.rowconfigure(2, minsize=30, weight=0)
        self.rowconfigure(3, minsize=30, weight=1)
        self.rowconfigure(4, minsize=30, weight=1)
        self.rowconfigure(5, minsize=60, weight=1)
        self.rowconfigure(6, minsize=30, weight=0)
        self.rowconfigure(7, minsize=30, weight=0)
        self.rowconfigure(8, minsize=30, weight=1)
        self.rowconfigure(9, minsize=60, weight=1)
        self.rowconfigure(10, minsize=60, weight=1)
        self.columnconfigure(0, minsize=60, weight=1)
        self.columnconfigure(1, minsize=60, weight=1)
        self.columnconfigure(2, minsize=60, weight=1)
        self.columnconfigure(3, minsize=60, weight=1)
        self.columnconfigure(4, minsize=60, weight=1)
        self.columnconfigure(5, minsize=30, weight=0)
        self.columnconfigure(6, minsize=60, weight=1)
        self.columnconfigure(7, minsize=60, weight=1)
        self.columnconfigure(8, minsize=60, weight=1)
        self.columnconfigure(9, minsize=60, weight=1)
        self.columnconfigure(10, minsize=60, weight=1)

        font9 = "-family Arial -size 12 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        buttonfont = "-family Arial -size 16 -weight bold -slant roman " \
                     "-underline 0 -overstrike 0"
        fbutton = tk.Button(self, text="Filler Button")
        fbutton.grid(row=0, column=1, sticky=N + E + S + W)
        button2 = tk.Button(self, text="Filler Button")
        button2.grid(row=0, column=2, sticky=N + E + S + W)
        button3 = tk.Button(self, text="Filler Button")
        button3.grid(row=0, column=3, sticky=N + E + S + W)
        button4 = tk.Button(self, text="Filler Button")
        button4.grid(row=0, column=4, sticky=N + E + S + W)
        button5 = tk.Button(self, text="Filler Button")
        button5.grid(row=0, column=5, sticky=N + E + S + W)
        button6 = tk.Button(self, text="Filler Button")
        button6.grid(row=0, column=6, sticky=N + E + S + W)
        button7 = tk.Button(self, text="Filler Button")
        button7.grid(row=0, column=7, sticky=N + E + S + W)
        button8 = tk.Button(self, text="Filler Button")
        button8.grid(row=0, column=8, sticky=N + E + S + W)
        button9 = tk.Button(self, text="Filler Button")
        button9.grid(row=0, column=9, sticky=N + E + S + W)
        button10 = tk.Button(self, text="Filler Button")
        button10.grid(row=0, column=10, sticky=N + E + S + W)
        missedbutton = tk.Button(self, text="FillerButton")
        missedbutton.grid(row=0, column=0, sticky=N + E + S + W)
        button11 = tk.Button(self, text="Filler Button")
        button11.grid(row=1, column=0, sticky=N + E + S + W)
        button13 = tk.Button(self, text="Filler Button")
        button13.grid(row=2, column=0, sticky=N + E + S + W)
        button14 = tk.Button(self, text="Filler Button")
        button14.grid(row=3, column=0, sticky=N + E + S + W)
        button15 = tk.Button(self, text="Filler Button")
        button15.grid(row=4, column=0, sticky=N + E + S + W)
        button16 = tk.Button(self, text="Filler Button")
        button16.grid(row=5, column=0, sticky=N + E + S + W)
        button17 = tk.Button(self, text="Filler Button")
        button17.grid(row=6, column=0, sticky=N + E + S + W)
        button18 = tk.Button(self, text="Filler Button")
        button18.grid(row=7, column=0, sticky=N + E + S + W)
        button19 = tk.Button(self, text="Filler Button")
        button19.grid(row=8, column=0, sticky=N + E + S + W)
        button20 = tk.Button(self, text="Filler Button")
        button20.grid(row=9, column=0, sticky=N + E + S + W)
        button21 = tk.Button(self, text="Filler Button")
        button21.grid(row=10, column=0, sticky=N + E + S + W)

        btn_so2 = tk.Button(self, text="Start Over")
        btn_so2.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                          borderwidth=2)
        btn_so2.configure(height=3, width=14)
        btn_so2.grid(row=0, column=0, sticky=N+E+W)

        btn_next2 = tk.Button(self, text="Next",
                              command=lambda: controller.show_frame(PageTwo))
        btn_next2.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                            relief=SUNKEN)
        btn_next2.configure(height=3, width=14)
        btn_next2.grid(row=10, column=10, sticky=S+E+W)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        # State List for Combobox
        self.state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                           "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                           "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                           "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                           "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                           "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                           "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        # Country List for ComboBox
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
                             "Finland", "France", "Gabon", "Gaza Strip", "The Gambia", "Georgia", "Germany",
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

        tk.Frame.__init__(self, parent)
        font9 = "-family Arial -size 24 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        entryfont = "-family Arial -size 20 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"
        buttonfont = "-family Arial -size 16 -weight bold -slant roman " \
                     "-underline 0 -overstrike 0"
        specfont = "-family Arial -size 15 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        self.rowconfigure(0, minsize=60, weight=0)
        self.rowconfigure(1, minsize=10, weight=1)
        self.rowconfigure(2, minsize=30, weight=0)
        self.rowconfigure(3, minsize=30, weight=1)
        self.rowconfigure(4, minsize=30, weight=0)
        self.rowconfigure(5, minsize=30, weight=1)
        self.rowconfigure(6, minsize=30, weight=0)
        self.rowconfigure(7, minsize=60, weight=1)
        self.rowconfigure(8, minsize=30, weight=0)
        self.rowconfigure(9, minsize=70, weight=1)
        self.rowconfigure(10, minsize=30, weight=0)
        self.rowconfigure(11, minsize=60, weight=1)
        self.rowconfigure(12, minsize=30, weight=0)
        self.rowconfigure(13, minsize=60, weight=1)
        self.columnconfigure(0, minsize=60, weight=1)
        self.columnconfigure(1, minsize=60, weight=1)
        self.columnconfigure(2, minsize=60, weight=1)
        self.columnconfigure(3, minsize=60, weight=1)
        self.columnconfigure(4, minsize=60, weight=1)
        self.columnconfigure(5, minsize=30, weight=1)
        self.columnconfigure(6, minsize=60, weight=1)
        self.columnconfigure(7, minsize=60, weight=1)
        self.columnconfigure(8, minsize=60, weight=1)
        self.columnconfigure(9, minsize=60, weight=1)
        self.columnconfigure(10, minsize=60, weight=1)
        self.columnconfigure(11, minsize=60, weight=1)

        # fbutton = tk.Button(self, text="Filler Button")
        # fbutton.grid(row=0, column=1, sticky=N+E+S+W)
        # button2 = tk.Button(self, text="Filler Button")
        # button2.grid(row=0, column=2, sticky=N+E+S+W)
        # button3 = tk.Button(self, text="Filler Button")
        # button3.grid(row=0, column=3, sticky=N+E+S+W)
        # button4 = tk.Button(self, text="Filler Button")
        # button4.grid(row=0, column=4, sticky=N+E+S+W)
        # button5 = tk.Button(self, text="Filler Button")
        # button5.grid(row=0, column=5, sticky=N+E+S+W)
        # button6 = tk.Button(self, text="Filler Button")
        # button6.grid(row=0, column=6, sticky=N+E+S+W)
        # button7 = tk.Button(self, text="Filler Button")
        # button7.grid(row=0, column=7, sticky=N+E+S+W)
        # button8 = tk.Button(self, text="Filler Button")
        # button8.grid(row=0, column=8, sticky=N+E+S+W)
        # button9 = tk.Button(self, text="Filler Button")
        # button9.grid(row=0, column=9, sticky=N+E+S+W)
        # button10 = tk.Button(self, text="Filler Button")
        # button10.grid(row=0, column=10, sticky=N+E+S+W)
        # missedbutton = tk.Button(self, text="FillerButton")
        # missedbutton.grid(row=0, column=0, sticky=N+E+S+W)
        # bc11 = tk.Button(self, text="Filler Button")
        # bc11.grid(row=0, column=11, sticky=N+E+S+W)
        # bc12 = tk.Button(self, text="Filler Button")
        # bc12.grid(row=0, column=12, sticky=N+E+S+W)
        # button11 = tk.Button(self, text="Filler Button")
        # button11.grid(row=1, column=0, sticky=N+E+S+W)
        # button13 = tk.Button(self, text="Filler Button")
        # button13.grid(row=2, column=0, sticky=N+E+S+W)
        # button14 = tk.Button(self, text="Filler Button")
        # button14.grid(row=3, column=0, sticky=N+E+S+W)
        # button15 = tk.Button(self, text="Filler Button")
        # button15.grid(row=4, column=0, sticky=N+E+S+W)
        # button16 = tk.Button(self, text="Filler Button")
        # button16.grid(row=5, column=0, sticky=N+E+S+W)
        # button17 = tk.Button(self, text="Filler Button")
        # button17.grid(row=6, column=0, sticky=N+E+S+W)
        # button18 = tk.Button(self, text="Filler Button")
        # button18.grid(row=7, column=0, sticky=N+E+S+W)
        # button19 = tk.Button(self, text="Filler Button")
        # button19.grid(row=8, column=0, sticky=N+E+S+W)
        # button20 = tk.Button(self, text="Filler Button")
        # button20.grid(row=9, column=0, sticky=N+E+S+W)
        # button21 = tk.Button(self, text="Filler Button")
        # button21.grid(row=10, column=0, sticky=N+E+S+W)
        # b11 = tk.Button(self, text="Filler Button")
        # b11.grid(row=11, column=0, sticky=N+E+S+W)
        # b12 = tk.Button(self, text="Filler Button")
        # b12.grid(row=12, column=0, sticky=N+E+S+W)
        # b13 = tk.Button(self, text="Filler Button")
        # b13.grid(row=13, column=0, sticky=N+E+S+W)

        # Start Over Button (Page 3)
        button1 = tk.Button(self, text="Start Over")
        button1.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                          borderwidth=2)
        button1.configure(height=3, width=20)
        button1.grid(row=0, column=0, sticky=N+E+W)
        # Next Page Button
        btn_Next1 = tk.Button(self, text="Next",
                              command=lambda: controller.show_frame(PaymentPage))
        btn_Next1.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                            relief=SUNKEN)
        btn_Next1.configure(height=3, width=20)
        btn_Next1.grid(row=13, column=12, sticky=S+E+W)
        # Label for First Name
        l_fname = tk.Label(self, text="First Name *", font=font9)
        l_fname.configure(background='#0066AB', foreground='#ffffff')
        l_fname.grid(row=1, column=2, sticky=W+S)
        # Entry for First Name
        self.e_fname = tk.Entry(self, font=entryfont)
        self.e_fname.grid(row=2, column=2, columnspan=4, sticky=E+W)
        # Label for First Name
        l_lname = tk.Label(self, text="Last Name *", font=font9)
        l_lname.configure(background='#0066AB', foreground='#ffffff')
        l_lname.grid(row=1, column=7, sticky=W+S)
        # Entry for Last Name
        self.e_lname = tk.Entry(self, font=entryfont)
        self.e_lname.grid(row=2, column=7, columnspan=4, sticky=E+W)
        # Label for Email
        self.l_email = tk.Label(self, text="Email Address *", font=font9)
        self.l_email.configure(background='#0066AB', foreground='#ffffff')
        self.l_email.grid(row=3, column=2, sticky=W+S)
        # Entry for Email
        self.e_mail = tk.Entry(self, font=entryfont)
        self.e_mail.grid(row=4, column=2, columnspan=4, sticky=E+W)
        # Label for Telephone Number
        self.l_tele = tk.Label(self, text="Telephone Number *", font=font9)
        self.l_tele.configure(background='#0066AB', foreground='#ffffff')
        self.l_tele.grid(row=3, column=7, sticky=W+S)
        # Entry for Telephone Number
        self.e_tele = tk.Entry(self, font=entryfont)
        self.e_tele.grid(row=4, column=7, columnspan=4, sticky=E+W)
        # Label for Street Address 1
        self.l_stradd1 = tk.Label(self, text="Street Address 1 *", font=font9)
        self.l_stradd1.configure(background='#0066AB', foreground='#ffffff')
        self.l_stradd1.grid(row=5, column=2, sticky=W+S)
        # Entry for Street Address 1
        self.e_stradd1 = tk.Entry(self, font=entryfont)
        self.e_stradd1.grid(row=6, column=2, columnspan=9, sticky=E+W)
        # Label for Street Address Line 2
        self.l_stradd2 = tk.Label(self, text="Street Address Line 2", font=font9)
        self.l_stradd2.configure(background='#0066AB', foreground='#ffffff')
        self.l_stradd2.grid(row=7, column=2, sticky=W+S)
        # Entry for Street Address Line 2
        self.e_stradd2 = tk.Entry(self, font=entryfont)
        self.e_stradd2.grid(row=8, column=2, columnspan=9, sticky=E+W)
        # Specification for SAL 2
        self.l_stradd2spec = tk.Label(self, text="Optional: Apt/Suite/P.O Box", font=specfont)
        self.l_stradd2spec.configure(background='#0066AB', foreground='#ffffff')
        self.l_stradd2spec.grid(row=9, column=2, sticky=W+N)
        # Label for City
        self.l_city = tk.Label(self, text="City *", font=font9)
        self.l_city.configure(background='#0066AB', foreground='#ffffff')
        self.l_city.grid(row=9, column=2, sticky=W+S)
        # Entry for City
        self.e_city = tk.Entry(self, font=entryfont)
        self.e_city.grid(row=10, column=2, columnspan=4, sticky=E+W)
        # Label for State
        self.l_state = tk.Label(self, text="State *", font=font9)
        self.l_state.configure(background='#0066AB', foreground='#ffffff')
        self.l_state.grid(row=9, column=7, sticky=W+S)
        # Combo Box for State
        self.c_state = ttk.Combobox(self, values=self.state_list, font=entryfont)
        self.c_state.grid(row=10, column=7, columnspan=4, sticky=E+W)
        # Label for Zip Code
        self.l_zip = tk.Label(self, text="Postal Code *", font=font9)
        self.l_zip.configure(background='#0066AB', foreground='#ffffff')
        self.l_zip.grid(row=11, column=2, sticky=W+S)
        # Entry for Zip Code
        self.e_zip = tk.Entry(self, font=entryfont)
        self.e_zip.grid(row=12, column=2, columnspan=4, sticky=E+W)
        # Label for Country
        self.l_country = tk.Label(self, text="Country *", font=font9)
        self.l_country.configure(background='#0066AB', foreground='#ffffff')
        self.l_country.grid(row=11, column=7, sticky=W+S)
        # Combobox for Country
        self.c_country = ttk.Combobox(self, values=self.country_list, font=entryfont)
        self.c_country.grid(row=12, column=7, columnspan=4, sticky=E+W)


class PaymentPage(tk.Frame):

    def __init__(self, parent, controller):

        # State List for Combobox
        self.state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                           "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                           "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                           "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                           "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                           "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                           "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        # Country List for ComboBox
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
                             "Finland", "France", "Gabon", "Gaza Strip", "The Gambia", "Georgia", "Germany",
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

        tk.Frame.__init__(self, parent)
        font9 = "-family Arial -size 24 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        entryfont = "-family Arial -size 20 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"
        buttonfont = "-family Arial -size 16 -weight bold -slant roman " \
                     "-underline 0 -overstrike 0"
        specfont = "-family Arial -size 15 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        self.rowconfigure(0, minsize=60, weight=0)
        self.rowconfigure(1, minsize=10, weight=1)
        self.rowconfigure(2, minsize=30, weight=0)
        self.rowconfigure(3, minsize=30, weight=1)
        self.rowconfigure(4, minsize=30, weight=0)
        self.rowconfigure(5, minsize=30, weight=1)
        self.rowconfigure(6, minsize=30, weight=0)
        self.rowconfigure(7, minsize=60, weight=1)
        self.rowconfigure(8, minsize=30, weight=0)
        self.rowconfigure(9, minsize=70, weight=1)
        self.rowconfigure(10, minsize=30, weight=0)
        self.rowconfigure(11, minsize=60, weight=1)
        self.rowconfigure(12, minsize=30, weight=0)
        self.rowconfigure(13, minsize=60, weight=1)
        self.columnconfigure(0, minsize=60, weight=1)
        self.columnconfigure(1, minsize=60, weight=1)
        self.columnconfigure(2, minsize=60, weight=1)
        self.columnconfigure(3, minsize=60, weight=1)
        self.columnconfigure(4, minsize=60, weight=1)
        self.columnconfigure(5, minsize=30, weight=1)
        self.columnconfigure(6, minsize=60, weight=1)
        self.columnconfigure(7, minsize=60, weight=1)
        self.columnconfigure(8, minsize=60, weight=1)
        self.columnconfigure(9, minsize=60, weight=1)
        self.columnconfigure(10, minsize=60, weight=1)
        self.columnconfigure(11, minsize=60, weight=1)

        fbutton = tk.Button(self, text="Filler Button")
        fbutton.grid(row=0, column=1, sticky=N+E+S+W)
        button2 = tk.Button(self, text="Filler Button")
        button2.grid(row=0, column=2, sticky=N+E+S+W)
        button3 = tk.Button(self, text="Filler Button")
        button3.grid(row=0, column=3, sticky=N+E+S+W)
        button4 = tk.Button(self, text="Filler Button")
        button4.grid(row=0, column=4, sticky=N+E+S+W)
        button5 = tk.Button(self, text="Filler Button")
        button5.grid(row=0, column=5, sticky=N+E+S+W)
        button6 = tk.Button(self, text="Filler Button")
        button6.grid(row=0, column=6, sticky=N+E+S+W)
        button7 = tk.Button(self, text="Filler Button")
        button7.grid(row=0, column=7, sticky=N+E+S+W)
        button8 = tk.Button(self, text="Filler Button")
        button8.grid(row=0, column=8, sticky=N+E+S+W)
        button9 = tk.Button(self, text="Filler Button")
        button9.grid(row=0, column=9, sticky=N+E+S+W)
        button10 = tk.Button(self, text="Filler Button")
        button10.grid(row=0, column=10, sticky=N+E+S+W)
        missedbutton = tk.Button(self, text="FillerButton")
        missedbutton.grid(row=0, column=0, sticky=N+E+S+W)
        bc11 = tk.Button(self, text="Filler Button")
        bc11.grid(row=0, column=11, sticky=N+E+S+W)
        bc12 = tk.Button(self, text="Filler Button")
        bc12.grid(row=0, column=12, sticky=N+E+S+W)
        button11 = tk.Button(self, text="Filler Button")
        button11.grid(row=1, column=0, sticky=N+E+S+W)
        button13 = tk.Button(self, text="Filler Button")
        button13.grid(row=2, column=0, sticky=N+E+S+W)
        button14 = tk.Button(self, text="Filler Button")
        button14.grid(row=3, column=0, sticky=N+E+S+W)
        button15 = tk.Button(self, text="Filler Button")
        button15.grid(row=4, column=0, sticky=N+E+S+W)
        button16 = tk.Button(self, text="Filler Button")
        button16.grid(row=5, column=0, sticky=N+E+S+W)
        button17 = tk.Button(self, text="Filler Button")
        button17.grid(row=6, column=0, sticky=N+E+S+W)
        button18 = tk.Button(self, text="Filler Button")
        button18.grid(row=7, column=0, sticky=N+E+S+W)
        button19 = tk.Button(self, text="Filler Button")
        button19.grid(row=8, column=0, sticky=N+E+S+W)
        button20 = tk.Button(self, text="Filler Button")
        button20.grid(row=9, column=0, sticky=N+E+S+W)
        button21 = tk.Button(self, text="Filler Button")
        button21.grid(row=10, column=0, sticky=N+E+S+W)
        b11 = tk.Button(self, text="Filler Button")
        b11.grid(row=11, column=0, sticky=N+E+S+W)
        b12 = tk.Button(self, text="Filler Button")
        b12.grid(row=12, column=0, sticky=N+E+S+W)
        b13 = tk.Button(self, text="Filler Button")
        b13.grid(row=13, column=0, sticky=N+E+S+W)

        # Start Over Button (Page 3)
        button1 = tk.Button(self, text="Start Over")
        button1.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                          borderwidth=2)
        button1.configure(height=3, width=20)
        button1.grid(row=0, column=0, sticky=N+E+W)
        # Next Page Button
        btn_Next1 = tk.Button(self, text="Next",
                              command=lambda: controller.show_frame(StartPage))
        btn_Next1.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                            relief=SUNKEN)
        btn_Next1.configure(height=3, width=20)
        btn_Next1.grid(row=13, column=12, sticky=S+E+W)
        # Label for First Name
        self.l_fname2 = tk.Label(self, text="First Name *", font=font9)
        self.l_fname2.configure(background='#0066AB', foreground='#ffffff')
        self.l_fname2.grid(row=3, column=2, sticky=W+S)
        # Entry for First Name
        self.e_fname2 = tk.Entry(self, font=entryfont)
        self.e_fname2.grid(row=4, column=2, columnspan=4, sticky=E+W)
        # Label for Last Name
        self.l_lname2 = tk.Label(self, text="Last Name *", font=font9)
        self.l_lname2.configure(background='#0066AB', foreground='#ffffff')
        self.l_lname2.grid(row=3, column=7, sticky=W+S)
        # Entry for Last Name
        self.e_lname2 = tk.Entry(self, font=entryfont)
        self.e_lname2.grid(row=4, column=7, columnspan=4, sticky=E+W)
        # Label for Credit Card Number
        self.l_ccn = tk.Label(self, text="Credit Card Number*", font=font9)
        self.l_ccn.configure(background='#0066AB', foreground='#ffffff')
        self.l_ccn.grid(row=5, column=2, sticky=W+S)
        # Entry for Credit Card Number
        self.e_stradd1 = tk.Entry(self, font=entryfont)
        self.e_stradd1.grid(row=6, column=2, columnspan=9, sticky=E+W)
        # Label for Security Code
        self.l_stradd2 = tk.Label(self, text="Street Address Line 2", font=font9)
        self.l_stradd2.configure(background='#0066AB', foreground='#ffffff')
        self.l_stradd2.grid(row=7, column=2, sticky=W+S)
        # Entry for Street Address Line 2
        self.e_stradd2 = tk.Entry(self, font=entryfont)
        self.e_stradd2.grid(row=8, column=2, columnspan=9, sticky=E+W)
        # Label for City
        self.l_city = tk.Label(self, text="City *", font=font9)
        self.l_city.configure(background='#0066AB', foreground='#ffffff')
        self.l_city.grid(row=9, column=2, sticky=W+S)
        # Entry for City
        self.e_city = tk.Entry(self, font=entryfont)
        self.e_city.grid(row=10, column=2, columnspan=4, sticky=E+W)

        # Label for Zip Code
        self.l_zip = tk.Label(self, text="Postal Code *", font=font9)
        self.l_zip.configure(background='#0066AB', foreground='#ffffff')
        self.l_zip.grid(row=11, column=2, sticky=W+S)
        # Entry for Zip Code
        self.e_zip = tk.Entry(self, font=entryfont)
        self.e_zip.grid(row=12, column=2, columnspan=4, sticky=E+W)



app = SeaofBTCapp()
app.mainloop()
