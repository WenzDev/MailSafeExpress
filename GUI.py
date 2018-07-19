import sys

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

import gui_support




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

    def next_sec(self):
        if self.e_csec.get() != self.e_sec.get():
            print("Error")
        else:
            self.sec_number = self.e_sec.get()
            self.csec_number = self.e_csec.get()
            print(self.sec_number, self.csec_number)


if __name__ == '__main__':
    vp_start_gui()
