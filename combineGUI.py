import tkinter as tk
import tkinter

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Frame):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(None, *args, **kwargs)

        super().__init__(**kwargs)
        self.tk = tk.Tk()

        self.tk.attributes('-fullscreen', True)

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand= True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Mailsafe_Express, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Mailsafe_Express)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def qf(param):
    print(param)


class Mailsafe_Express():
    def __init__(self, top=None):
        self.sec_number = None
        self.csec_number = None
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family Arial -size 17 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        font9 = "-family Arial -size 12 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"

        top.geometry("1920x1077+1761+0")
        top.title("Mailsafe Express")
        top.configure(background="#0066ab")
        top.configure(highlightbackground="#f0f0f0")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.btn_Next = tk.Button(top)
        self.btn_Next.place(relx=0.86, rely=0.92, height=54, width=247)
        self.btn_Next.configure(activebackground="#d9d9d9")
    #     self.btn_Next.configure(command=next_sec)

        self.btn_Next.configure(activeforeground="#000000")
        self.btn_Next.configure(background="#00497a")
        self.btn_Next.configure(disabledforeground="#a3a3a3")
        self.btn_Next.configure(font=font9)
        self.btn_Next.configure(foreground="#ffffff")
        self.btn_Next.configure(highlightbackground="#d9d9d9")
        self.btn_Next.configure(highlightcolor="black")
        self.btn_Next.configure(pady="0")
        self.btn_Next.configure(takefocus="0")
        self.btn_Next.configure(text='''Next''')
        self.btn_Next.configure(width=247)
        self.btn_Next.configure(command=self.next_sec)

        self.btn_startover = tk.Button(top)
        self.btn_startover.place(relx=0.01, rely=0.01, height=54, width=247)
        self.btn_startover.configure(activebackground="#aaaaaa")
        self.btn_startover.configure(activeforeground="#ffffff")
        self.btn_startover.configure(background="#00497a")
        self.btn_startover.configure(disabledforeground="#e0e0e0")
        self.btn_startover.configure(font=font9)
        self.btn_startover.configure(foreground="#ffffff")
        self.btn_startover.configure(highlightbackground="#aaaaaa")
        self.btn_startover.configure(highlightcolor="#ffffff")
        self.btn_startover.configure(pady="0")
        self.btn_startover.configure(takefocus="0")
        self.btn_startover.configure(text='''Start Over''')
        self.btn_startover.configure(width=247)

        self.e_csec = tk.Entry(top)
        self.e_csec.place(relx=0.27, rely=0.58,height=40, relwidth=0.46)
        self.e_csec.configure(background="white")
        self.e_csec.configure(disabledforeground="#a3a3a3")
        self.e_csec.configure(font="TkFixedFont")
        self.e_csec.configure(foreground="#000000")
        self.e_csec.configure(insertbackground="black")
        self.e_csec.configure(takefocus="0")
        self.e_csec.configure(width=884)

        self.e_sec = tk.Entry(top)
        self.e_sec.place(relx=0.27, rely=0.46,height=40, relwidth=0.46)
        self.e_sec.configure(background="white")
        self.e_sec.configure(disabledforeground="#a3a3a3")
        self.e_sec.configure(font="TkFixedFont")
        self.e_sec.configure(foreground="#000000")
        self.e_sec.configure(insertbackground="black")
        self.e_sec.configure(takefocus="0")
        self.e_sec.configure(width=884)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.27, rely=0.38, height=81, width=884)
        self.Label1.configure(background="#0066ab")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Security Envelope Code''')
        self.Label1.configure(width=884)

        self.lbl_rsec = tk.Label(top)
        self.lbl_rsec.place(relx=0.27, rely=0.5, height=81, width=884)
        self.lbl_rsec.configure(background="#0066ab")
        self.lbl_rsec.configure(disabledforeground="#a3a3a3")
        self.lbl_rsec.configure(font=font10)
        self.lbl_rsec.configure(foreground="#ffffff")
        self.lbl_rsec.configure(text='''Confirm Security Envelope Code''')
        self.lbl_rsec.configure(width=884)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text ="Continue",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()

        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(Mailsafe_Express))
        button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        '''
        Do we want to be able to access the start page from Page 2?
        Maybe a quit function but will have to erase all data previously entered in...
        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        '''

        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

if __name__ == '__main__':
    root = tk.Tk()
    run = SeaofBTCapp(root)
    root.mainloop()