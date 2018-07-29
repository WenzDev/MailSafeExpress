from tkinter import *
import re


class App:
    def __init__(self, master):
        self.var = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master,width=1800,height=1600)
        f2.grid(row=0,column=1)
        self.carddata = Entry(master)
        self.carddata.grid(row=0, column=1)
        self.print = Button(text="Print", command=self.printCD)
        self.print.grid(row=0, column=2)
        self.card_data_get = None
        self.first_name = None
        self.last_name = None
        self.creditnumber = None


    def printCD(self):
        print(self.carddata.get())
        self.card_data_get = self.carddata.get()
        self.creditnumber = self.card_data_get[self.card_data_get.find("B")+1:self.card_data_get.find("^")]
        print(self.creditnumber)
        self.first_name = self.card_data_get[self.card_data_get.find("^")+2:self.card_data_get.find("^")]
        print(self.first_name)




top = Tk()
app = App(top)
top.mainloop()