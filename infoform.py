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

import infoform_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    infoform_support.set_Tk_var()
    top = info_form(root)
    infoform_support.init(root, top)
    root.mainloop()

w = None
def create_info_form(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    infoform_support.set_Tk_var()
    top = info_form(w)
    infoform_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_info_form():
    global w
    w.destroy()
    w = None


class info_form:
    def __init__(self, top=None):
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
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active', _ana2color)])

        top.geometry("1920x1061+1762+0")
        top.title("Mailsafe Express")
        top.configure(background="#0066ab")
        top.configure(highlightbackground="#f0f0f0")
        top.configure(highlightcolor="black")

        self.menubar = Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.btn_nextinfo = Button(top)
        self.btn_nextinfo.place(relx=0.86, rely=0.93, height=54, width=247)
        self.btn_nextinfo.configure(activebackground="#d9d9d9")
        self.btn_nextinfo.configure(activeforeground="#000000")
        self.btn_nextinfo.configure(background="#00497a")
        self.btn_nextinfo.configure(disabledforeground="#a3a3a3")
        self.btn_nextinfo.configure(font=font9)
        self.btn_nextinfo.configure(foreground="#ffffff")
        self.btn_nextinfo.configure(highlightbackground="#d9d9d9")
        self.btn_nextinfo.configure(highlightcolor="black")
        self.btn_nextinfo.configure(pady="0")
        self.btn_nextinfo.configure(takefocus="0")
        self.btn_nextinfo.configure(text='''Next''')

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

        self.e_fname = Entry(top)
        self.e_fname.place(relx=0.21, rely=0.28,height=40, relwidth=0.27)
        self.e_fname.configure(background="white")
        self.e_fname.configure(disabledforeground="#a3a3a3")
        self.e_fname.configure(font="TkFixedFont")
        self.e_fname.configure(foreground="#000000")
        self.e_fname.configure(highlightbackground="#d9d9d9")
        self.e_fname.configure(highlightcolor="black")
        self.e_fname.configure(insertbackground="black")
        self.e_fname.configure(selectbackground="#c4c4c4")
        self.e_fname.configure(selectforeground="black")
        self.e_fname.configure(takefocus="0")

        self.e_lname = Entry(top)
        self.e_lname.place(relx=0.52, rely=0.28,height=40, relwidth=0.27)
        self.e_lname.configure(background="white")
        self.e_lname.configure(disabledforeground="#a3a3a3")
        self.e_lname.configure(font="TkFixedFont")
        self.e_lname.configure(foreground="#000000")
        self.e_lname.configure(highlightbackground="#d9d9d9")
        self.e_lname.configure(highlightcolor="black")
        self.e_lname.configure(insertbackground="black")
        self.e_lname.configure(selectbackground="#c4c4c4")
        self.e_lname.configure(selectforeground="black")
        self.e_lname.configure(takefocus="0")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.21, rely=0.25, height=31, width=514)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#0066ab")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''First Name''')

        self.lbl_rsec = Label(top)
        self.lbl_rsec.place(relx=0.52, rely=0.25, height=31, width=514)
        self.lbl_rsec.configure(activebackground="#f9f9f9")
        self.lbl_rsec.configure(activeforeground="black")
        self.lbl_rsec.configure(background="#0066ab")
        self.lbl_rsec.configure(disabledforeground="#a3a3a3")
        self.lbl_rsec.configure(font=font10)
        self.lbl_rsec.configure(foreground="#ffffff")
        self.lbl_rsec.configure(highlightbackground="#d9d9d9")
        self.lbl_rsec.configure(highlightcolor="black")
        self.lbl_rsec.configure(text='''Last Name''')

        self.e_mail = Entry(top)
        self.e_mail.place(relx=0.21, rely=0.36,height=40, relwidth=0.57)
        self.e_mail.configure(background="white")
        self.e_mail.configure(disabledforeground="#a3a3a3")
        self.e_mail.configure(font="TkFixedFont")
        self.e_mail.configure(foreground="#000000")
        self.e_mail.configure(insertbackground="black")
        self.e_mail.configure(width=1104)

        self.Label1_1 = Label(top)
        self.Label1_1.place(relx=0.36, rely=0.32, height=31, width=514)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#0066ab")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font10)
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Email Address''')

        self.e_phone = Entry(top)
        self.e_phone.place(relx=0.21, rely=0.44,height=40, relwidth=0.57)
        self.e_phone.configure(background="white")
        self.e_phone.configure(disabledforeground="#a3a3a3")
        self.e_phone.configure(font="TkFixedFont")
        self.e_phone.configure(foreground="#000000")
        self.e_phone.configure(insertbackground="black")
        self.e_phone.configure(width=1104)

        self.Label1_2 = Label(top)
        self.Label1_2.place(relx=0.36, rely=0.41, height=31, width=514)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#0066ab")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font=font10)
        self.Label1_2.configure(foreground="#ffffff")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''Telephone Number''')

        self.Label1_3 = Label(top)
        self.Label1_3.place(relx=0.21, rely=0.52, height=31, width=1104)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#0066ab")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font=font10)
        self.Label1_3.configure(foreground="#ffffff")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Shipping Address:''')
        self.Label1_3.configure(width=1104)

        self.Label1_4 = Label(top)
        self.Label1_4.place(relx=0.1, rely=0.56, height=41, width=244)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#0066ab")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(font=font10)
        self.Label1_4.configure(foreground="#ffffff")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''Street Address''')
        self.Label1_4.configure(width=244)

        self.Label1_5 = Label(top)
        self.Label1_5.place(relx=0.07, rely=0.62, height=41, width=274)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#0066ab")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font10)
        self.Label1_5.configure(foreground="#ffffff")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''Street Address Line 2''')
        self.Label1_5.configure(width=274)

        self.Label1_5 = Label(top)
        self.Label1_5.place(relx=0.14, rely=0.69, height=41, width=194)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#0066ab")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(font=font10)
        self.Label1_5.configure(foreground="#ffffff")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text='''City''')
        self.Label1_5.configure(width=194)

        self.e_city = Entry(top)
        self.e_city.place(relx=0.21, rely=0.69,height=40, relwidth=0.27)
        self.e_city.configure(background="white")
        self.e_city.configure(disabledforeground="#a3a3a3")
        self.e_city.configure(font="TkFixedFont")
        self.e_city.configure(foreground="#000000")
        self.e_city.configure(insertbackground="black")
        self.e_city.configure(width=514)

        self.e_saddress2 = Entry(top)
        self.e_saddress2.place(relx=0.21, rely=0.62,height=40, relwidth=0.57)
        self.e_saddress2.configure(background="white")
        self.e_saddress2.configure(disabledforeground="#a3a3a3")
        self.e_saddress2.configure(font="TkFixedFont")
        self.e_saddress2.configure(foreground="#000000")
        self.e_saddress2.configure(insertbackground="black")
        self.e_saddress2.configure(width=1104)

        self.e_saddress = Entry(top)
        self.e_saddress.place(relx=0.21, rely=0.56,height=40, relwidth=0.57)
        self.e_saddress.configure(background="white")
        self.e_saddress.configure(disabledforeground="#a3a3a3")
        self.e_saddress.configure(font="TkFixedFont")
        self.e_saddress.configure(foreground="#000000")
        self.e_saddress.configure(insertbackground="black")
        self.e_saddress.configure(width=1104)

        self.e_state = Entry(top)
        self.e_state.place(relx=0.52, rely=0.69,height=40, relwidth=0.27)
        self.e_state.configure(background="white")
        self.e_state.configure(disabledforeground="#a3a3a3")
        self.e_state.configure(font="TkFixedFont")
        self.e_state.configure(foreground="#000000")
        self.e_state.configure(insertbackground="black")
        self.e_state.configure(width=514)

        self.Label1_6 = Label(top)
        self.Label1_6.place(relx=0.48, rely=0.69, height=41, width=64)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#0066ab")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(font=font10)
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''State''')
        self.Label1_6.configure(width=64)

        self.e_zip = Entry(top)
        self.e_zip.place(relx=0.21, rely=0.75,height=40, relwidth=0.24)
        self.e_zip.configure(background="white")
        self.e_zip.configure(disabledforeground="#a3a3a3")
        self.e_zip.configure(font="TkFixedFont")
        self.e_zip.configure(foreground="#000000")
        self.e_zip.configure(insertbackground="black")
        self.e_zip.configure(width=464)

        self.Label1_6 = Label(top)
        self.Label1_6.place(relx=0.15, rely=0.75, height=41, width=104)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#0066ab")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(font=font10)
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''Zip Code''')
        self.Label1_6.configure(width=104)

        self.Label1_6 = Label(top)
        self.Label1_6.place(relx=0.45, rely=0.75, height=41, width=124)
        self.Label1_6.configure(activebackground="#f9f9f9")
        self.Label1_6.configure(activeforeground="black")
        self.Label1_6.configure(background="#0066ab")
        self.Label1_6.configure(disabledforeground="#a3a3a3")
        self.Label1_6.configure(font=font10)
        self.Label1_6.configure(foreground="#ffffff")
        self.Label1_6.configure(highlightbackground="#d9d9d9")
        self.Label1_6.configure(highlightcolor="black")
        self.Label1_6.configure(text='''Country''')
        self.Label1_6.configure(width=124)




if __name__ == '__main__':
    vp_start_gui()
