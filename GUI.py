import sys
import stripe
import gui_support
stripe.api_key = 'sk_test_gC3XXUojw3qTRewhzCK3SlV6'
import itemGUI_support
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = Mailsafe_Express (root)
    gui_support.init(root, top)
    photo = PhotoImage(file='msecrop.png')
    label = Label(root, image=photo, borderwidth=0)
    label.pack()
    root.mainloop()


w = None


def create_Mailsafe_Express(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = Mailsafe_Express (w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Mailsafe_Express():
    global w
    w.destroy()
    w = None


class Mailsafe_Express:
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

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.btn_Next = Button(top)
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

        self.btn_startover = Button(top)
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

        self.e_csec = Entry(top)
        self.e_csec.place(relx=0.27, rely=0.58,height=40, relwidth=0.46)
        self.e_csec.configure(background="white")
        self.e_csec.configure(disabledforeground="#a3a3a3")
        self.e_csec.configure(font="TkFixedFont")
        self.e_csec.configure(foreground="#000000")
        self.e_csec.configure(insertbackground="black")
        self.e_csec.configure(takefocus="0")
        self.e_csec.configure(width=884)

        self.e_sec = Entry(top)
        self.e_sec.place(relx=0.27, rely=0.46,height=40, relwidth=0.46)
        self.e_sec.configure(background="white")
        self.e_sec.configure(disabledforeground="#a3a3a3")
        self.e_sec.configure(font="TkFixedFont")
        self.e_sec.configure(foreground="#000000")
        self.e_sec.configure(insertbackground="black")
        self.e_sec.configure(takefocus="0")
        self.e_sec.configure(width=884)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.27, rely=0.38, height=81, width=884)
        self.Label1.configure(background="#0066ab")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Security Envelope Code''')
        self.Label1.configure(width=884)

        self.lbl_rsec = Label(top)
        self.lbl_rsec.place(relx=0.27, rely=0.5, height=81, width=884)
        self.lbl_rsec.configure(background="#0066ab")
        self.lbl_rsec.configure(disabledforeground="#a3a3a3")
        self.lbl_rsec.configure(font=font10)
        self.lbl_rsec.configure(foreground="#ffffff")
        self.lbl_rsec.configure(text='''Confirm Security Envelope Code''')
        self.lbl_rsec.configure(width=884)

 def vp_start_gui():
 '''Starting point when module is the main routine.'''
 global val, w, root
        root = Tk()
        top = Mailsafe_Express(root)
        itemGUI_support.init(root, top)
        root.mainloop()

        w = None

    def create_haz_page(root, *args, **kwargs):
        '''Starting point when module is imported by another program.'''
        global w, w_win, rt
        rt = root
        w = Toplevel(root)
        top = Mailsafe_Express(w)
        itemGUI_support.init(w, top, *args, **kwargs)
        return (w, top)

    def destroy_haz_page():
        global w
        w.destroy()
        w = None

    class haz_page:
        def __init__(self, top=None):
            '''This class configures and populates the toplevel window.
               top is the toplevel containing window.'''
            _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
            _fgcolor = '#000000'  # X11 color: 'black'
            _compcolor = '#d9d9d9'  # X11 color: 'gray85'
            _ana1color = '#d9d9d9'  # X11 color: 'gray85'
            _ana2color = '#d9d9d9'  # X11 color: 'gray85'
            font10 = "-family Arial -size 12 -weight bold -slant roman " \
                     "-underline 0 -overstrike 0"
            font9 = "-family Arial -size 17 -weight bold -slant roman " \
                    "-underline 0 -overstrike 0"

            top.geometry("1920x1061+-197+37")
            top.title("Mailsafe Express")
            top.configure(background="#0066ab")
            top.configure(highlightbackground="#f0f0f0")
            top.configure(highlightcolor="black")

            self.menubar = Menu(top, font="TkMenuFont", bg=_bgcolor, fg=_fgcolor)
            top.configure(menu=self.menubar)

            self.btn_Next = Button(top)
            self.btn_Next.place(relx=0.86, rely=0.93, height=54, width=247)
            self.btn_Next.configure(activebackground="#d9d9d9")
            self.btn_Next.configure(activeforeground="#000000")
            self.btn_Next.configure(background="#00497a")
            self.btn_Next.configure(disabledforeground="#a3a3a3")
            self.btn_Next.configure(font=font10)
            self.btn_Next.configure(foreground="#ffffff")
            self.btn_Next.configure(highlightbackground="#d9d9d9")
            self.btn_Next.configure(highlightcolor="black")
            self.btn_Next.configure(pady="0")
            self.btn_Next.configure(takefocus="0")
            self.btn_Next.configure(text='''Next''')

            self.btn_startover = Button(top)
            self.btn_startover.place(relx=0.01, rely=0.01, height=54, width=247)
            self.btn_startover.configure(activebackground="#aaaaaa")
            self.btn_startover.configure(activeforeground="#ffffff")
            self.btn_startover.configure(background="#00497a")
            self.btn_startover.configure(disabledforeground="#e0e0e0")
            self.btn_startover.configure(font=font10)
            self.btn_startover.configure(foreground="#ffffff")
            self.btn_startover.configure(highlightbackground="#aaaaaa")
            self.btn_startover.configure(highlightcolor="#ffffff")
            self.btn_startover.configure(pady="0")
            self.btn_startover.configure(takefocus="0")
            self.btn_startover.configure(text='''Start Over''')

            self.btn_haz = Button(top)
            self.btn_haz.place(relx=0.09, rely=0.19, height=94, width=717)
            self.btn_haz.configure(activebackground="#d9d9d9")
            self.btn_haz.configure(activeforeground="#000000")
            self.btn_haz.configure(background="#00497a")
            self.btn_haz.configure(disabledforeground="#a3a3a3")
            self.btn_haz.configure(font=font9)
            self.btn_haz.configure(foreground="#ffffff")
            self.btn_haz.configure(highlightbackground="#d9d9d9")
            self.btn_haz.configure(highlightcolor="black")
            self.btn_haz.configure(pady="0")
            self.btn_haz.configure(text='''Hazardous''')

            self.btn_nonhaz = Button(top)
            self.btn_nonhaz.place(relx=0.51, rely=0.19, height=94, width=727)
            self.btn_nonhaz.configure(activebackground="#d9d9d9")
            self.btn_nonhaz.configure(activeforeground="#000000")
            self.btn_nonhaz.configure(background="#00497a")
            self.btn_nonhaz.configure(disabledforeground="#a3a3a3")
            self.btn_nonhaz.configure(font=font9)
            self.btn_nonhaz.configure(foreground="#ffffff")
            self.btn_nonhaz.configure(highlightbackground="#d9d9d9")
            self.btn_nonhaz.configure(highlightcolor="black")
            self.btn_nonhaz.configure(pady="0")
            self.btn_nonhaz.configure(text='''Non-Hazardous''')

            self.Label1 = Label(top)
            self.Label1.place(relx=0.51, rely=0.28, height=631, width=724)
            self.Label1.configure(activebackground="#f9f9f9")
            self.Label1.configure(activeforeground="black")
            self.Label1.configure(background="#d9d9d9")
            self.Label1.configure(disabledforeground="#a3a3a3")
            self.Label1.configure(foreground="#000000")
            self.Label1.configure(highlightbackground="#d9d9d9")
            self.Label1.configure(highlightcolor="black")

            self.Label2 = Label(top)
            self.Label2.place(relx=0.09, rely=0.28, height=631, width=714)
            self.Label2.configure(activebackground="#f9f9f9")
            self.Label2.configure(activeforeground="black")
            self.Label2.configure(background="#d9d9d9")
            self.Label2.configure(disabledforeground="#a3a3a3")
            self.Label2.configure(foreground="#000000")
            self.Label2.configure(highlightbackground="#d9d9d9")
            self.Label2.configure(highlightcolor="black")
        def next_sec(self):
            if self.e_csec.get() == self.e_sec.get():
                self.sec_number = self.e_sec.get()
                self.csec_number = self.e_csec.get()
                print(self.sec_number, self.csec_number)
            else:
                print("Error: Security Envelope Codes Do Not Match!")


if __name__ == '__main__':
    vp_start_gui()
