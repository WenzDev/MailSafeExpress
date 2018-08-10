from tkinter import *
from tkinter import messagebox
import stripe
from payment import *
import re



class App:
    def __init__(self, master):
        self.var = IntVar()
        frame = Frame(master)
        frame.grid()
        f2 = Frame(master,width=1800,height=1600)
        f2.grid(row=1,column=10)
        self.carddata = Entry(master)
        self.carddata.focus()
        self.carddata.grid(row=0, column=1)
        self.print = Button(text="Print", command=self.printCD)
        self.print.grid(row=0, column=2)
        self.print = Button(text="Stripe", command=self.sendstripe)
        self.print.grid(row=0, column=3)
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
        self.raw = None
        self.custInfo = [self.first_name, self.last_name, self.creditnumber, self.exp]

    def printCD(self):
        # print raw data
        # assign raw data to be regex'd
        self.raw = self.carddata.get()
        if "%E?;E?" in self.raw:
            print("Error! Swipe again")
            messagebox.showerror("Swipe your card again!", "We were unable to read your card")
        else:
            print("Processing")

        #               cc               first          last            exp
        regex = r"^%B(?P<nr>[^^]+)\^(?P<fname>[^/]+)/(?P<lname>[^^]+)\^(\d{4})[^^]"
        # find the matches

        matches = re.finditer(regex, self.raw, re.MULTILINE)

        for matchNum, match in enumerate(matches):
            matchNum = matchNum + 1

            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                self.first_name = match.group(3)
                self.last_name = match.group(2)
                self.creditnumber = match.group(1)
                self.exp = match.group(4)

            print("First Name:" + " " + self.first_name)
            print("Last Name:" + " " + self.last_name)
            print("Card Number:" + " " + self.creditnumber)
            print("Expiration Date:" + " " + self.exp)
            self.custInfo = [self.first_name, self.last_name, self.creditnumber, self.exp]
            self.fnl = self.first_name + " " + self.last_name

    def sendstripe(self):
        stripe.Customer.create(
            description="Customer",
            metadata=self.fnl
        )
        return self.custInfo



top = Tk()
app = App(top)
top.mainloop()