import tkinter as tk
from tkinter import ttk
from tkinter import *

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        self.attributes('-fullscreen', True)


        # Fix the icon for window ? tk.Tk.iconbitmap(self, default="if_shopping_cart_16x16_9988.ico")

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
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()


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
        self.e_fname.place(relx=0.21, rely=0.28, height=40, relwidth=0.27)
        self.l_fname = Label(self, text='''First Name''', font=font9)
        self.l_fname.place(relx=0.21, rely=0.25, height=31, width=514)
        # last name
        self.e_lname = Entry(self)
        self.e_lname.place(relx=0.52, rely=0.28, height=40, relwidth=0.27)
        self.l_lname = Label(self, text='''Last Name''', font=font9)
        self.l_lname.place(relx=0.52, rely=0.25, height=31, width=514)
        # email
        self.e_mail = Entry(self)
        self.e_mail.place(relx=0.21, rely=0.36,height=40, relwidth=0.57)
        self.l_mail = Label(self, text='''Email Address''', font=font9)
        self.l_mail.place(relx=0.36, rely=0.32, height=31, width=514)
        # phone number
        self.e_phone = Entry(self)
        self.e_phone.place(relx=0.21, rely=0.44, height=40, relwidth=0.57)
        # Address
        self.e_saddress = Entry(self)
        self.e_saddress.place(relx=0.21, rely=0.56, height=40, relwidth=0.57)
        # Address Line 2
        self.e_saddress2 = Entry(self)
        self.e_saddress2.place(relx=0.21, rely=0.62, height=40, relwidth=0.57)
        # City
        self.e_city = Entry(self)
        self.e_city.place(relx=0.21, rely=0.69, height=40, relwidth=0.27)
        # State
        self.state_list = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
                           "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas",
                           "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                           "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey",
                           "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
                           "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
                           "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
        self.combo_state = ttk.Combobox(self, values=self.state_list)
        self.combo_state.place(relx=0.52, rely=0.69, height=40, relwidth=0.27)
        # Zip Code
        self.e_zip = Entry(self)
        self.e_zip.place(relx=0.21, rely=0.75, height=40, relwidth=0.24)



app = SeaofBTCapp()
app.mainloop()