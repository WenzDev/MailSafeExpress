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

import testgui2_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel(root)
    testgui2_support.init(root, top)
    root.mainloop()


w = None


def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel(root)
    top = New_Toplevel(w)
    testgui2_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#d9d9d9'  # X11 color: 'gray85'

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.Label1 = Label(top)
        self.Label1.place(relx=0.08, rely=0.2, height=241, width=494)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''You know this dick aint free''')
        self.Label1.configure(width=494)


if __name__ == '__main__':
    vp_start_gui()
