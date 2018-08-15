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

    def check_sec(self):
        if self.e_sec.get() == self.e_csec.get():
            print("Success! Your envelope security code is:" + " " + self.e_sec.get())
        else:
            self.errorsec()
            print("Error: Type that again!")


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.rowconfigure(0, minsize=60, weight=1)
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

        font9 = "-family Arial -size 12 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        buttonfont = "-family Arial -size 16 -weight bold -slant roman " \
                     "-underline 0 -overstrike 0"

        btn_so2 = tk.Button(self, text="Start Over")
        btn_so2.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                          borderwidth=2)
        btn_so2.configure(height=3, width=10)
        btn_so2.grid(row=0, column=0, sticky=N+E+W)

        btn_next2 = tk.Button(self, text="Next",
                              command=lambda: controller.show_frame(PageTwo))
        btn_next2.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                            relief=SUNKEN)
        btn_next2.configure(height=3, width=10)
        btn_next2.grid(row=10, column=10, sticky=S+E+W)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        font9 = "-family Arial -size 24 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        entryfont = "-family Arial -size 20 -weight normal -slant roman " \
                "-underline 0 -overstrike 0"
        buttonfont = "-family Arial -size 16 -weight bold -slant roman " \
                     "-underline 0 -overstrike 0"
        self.rowconfigure(0, minsize=60, weight=1)
        self.rowconfigure(1, minsize=60, weight=1)
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
        self.columnconfigure(5, minsize=30, weight=1)
        self.columnconfigure(6, minsize=60, weight=1)
        self.columnconfigure(7, minsize=60, weight=1)
        self.columnconfigure(8, minsize=60, weight=1)
        self.columnconfigure(9, minsize=60, weight=1)
        self.columnconfigure(10, minsize=60, weight=1)

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
        # Start Over Button (Page 3)
        btn_so3 = tk.Button(self, text="Start Over",
                             command=lambda: controller.show_frame(StartPage))
        btn_so3.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                          borderwidth=2)
        btn_so3.configure(height=3, width=10)
        btn_so3.grid(row=0, column=0, sticky=N+E+W)
        # Next Button (Page 3)
        btn_next3 = tk.Button(self, text="Next",
                             command=lambda: controller.show_frame(StartPage))
        btn_next3.configure(font=buttonfont, fg='#ffffff', background='#00497a', highlightbackground='#3E4149',
                            relief=SUNKEN)
        btn_next3.configure(height=3, width=10)
        btn_next3.grid(row=10, column=9, columnspan=2, sticky=S+E+W)

        self.e_fname = tk.Entry(self, font=entryfont)
        self.e_fname.grid(row=2, column=2, columnspan=3, sticky=E+W)

        self.e_lname = tk.Entry(self, font=entryfont)
        self.e_lname.grid(row=2, column=6, columnspan=3, sticky=E+W)

        self.e_mail = tk.Entry(self, font=entryfont)
        self.e_mail.grid(row=4, column=2, columnspan=7, sticky=E+W)

        self.e_tele = tk.Entry(self, font=entryfont)
        self.e_tele.grid(row=6, column=2, columnspan=7, sticky=E+W)






app = SeaofBTCapp()
app.mainloop()
