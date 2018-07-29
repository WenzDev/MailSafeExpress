import tkinter as tk
from tkinter import font as tkfont

class MailSafeExpress(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (SecurityCodePage, UserInformation, PaymentPage)
            page_name = F.__name
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("SecurityCodePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class SecurityCodePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        btn_StartOver = tk.Button(self, text="Start Over",
                            command=lambda: controller.show_frame("SecurityCodePage"))
        btn_StartOver.pack()

