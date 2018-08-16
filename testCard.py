from tkinter import *
import re


class App:
    def __init__(self, master):
        self.var = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master,width=1800,height=1600)
        f2.grid(row=1,column=10)
        self.carddata = Entry(master)
        self.carddata.grid(row=0, column=1)
        self.e_cc = Entry(master)
        self.e_cc.grid(row=0, column=4)
        self.print = Button(text="Print", command=self.printCD)
        self.print.grid(row=0, column=2)
        # gets string from entry
        self.card_data_get = None
        # first name
        self.first_name = None
        # last name
        self.last_name = None
        # CC number
        self.creditnumber = None
        # group of First and Last
        self.fnl = None
        # CC exp date
        self.exp = None
        # match to get cc #
        self.m_cc = None
        # compiled exp for pulling the exp
        self.p_exp = None
        # match exp
        self.matches = None
        self.pat = None
        self.match = None
        self.digits = None

    def printCD(self):
        # print raw data
        print(self.carddata.get())
        # assign raw data to be regex'd
        self.card_data_get = self.carddata.get()
        # match_creditcard to find it from raw data
        self.m_cc = re.search(r"\d(?P<creditcard>.+)\^.+\^", self.card_data_get)
        # get first and last name from raw data
        self.fnl = re.search(r"\^(?P<last>.+)/(?P<first>.+)\^", self.card_data_get)
        #
        pat = re.compile(r"\^(\d{4})[^^]")
        self.match = pat.match(self.card_data_get)
        self.digits = self.match.group(group1=1)

        self.creditnumber = self.m_cc.group('creditcard')
        self.first_name = self.fnl.group('first')
        self.last_name = self.fnl.group('last')
#        self.e_cc.delete(0, END)
#       self.e_cc.insert(0, self.creditnumber)
        print(self.creditnumber)
        print(self.first_name)
        print(self.last_name)
        print(self.digits)
        print*self.creditnumber,


top = Tk()
app = App(top)
top.mainloop()