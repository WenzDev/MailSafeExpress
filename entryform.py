from shipstation.api import *
from GUI import *
api_key = 'fd1377e2624a4a7faf343c329ed4f7fa'
api_secret = '21b3bf6385dc45d1a98e0a61d3de1c88'
m = Mailsafe_Express()
ss = ShipStation(key=api_key, secret=api_secret)
id = '1234567890'
ss_order = ShipStationOrder(order_number=id)

class Ship_Station():
    def __init__(self):
        self.security_code = None
        self.csecurity_code = None
        self.item_type = None
        self.f_name = None
        self.l_name = None
        self.ship_address = None
        self.bill_address = None

    def set_form(self):
        self.security_code = m.get_sec()
        self.csecurity_code = m.get_csec()
        self.item_type = None
        self.f_name = None
        self.l_name = None
        self.ship_address = None
        self.bill_address = None

    def print_form(self):
        print(self.security_code, self.csecurity_code, self.item_type, self.f_name, self.l_name, self.ship_address,
              self.bill_address)

    if __name__ == '__main__':
        set_form(), print_form()


