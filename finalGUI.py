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


app = SeaofBTCapp()
app.mainloop()