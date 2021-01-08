class Phone:
    """ This is a phone class that can be used for inheritanve purposes"""
    def __init__(self, phone_number, color):
        self.phone_number = phone_number
        self.color = color
    def __str__(self):
        return f"This phone belongs to {self.phone_number}"
    def call(self, other_number):
        print(f"Calling number: {other_number}")
    def text(self, other_number, message):
        print(f"Sending text to the {other_number}")
    def open_app(self, app_name):
        print(f"Opening {app.name}")  


class Android(Phone):
    def __init__ (self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = None
        self.battery = 50
    def __str__(self):
        return f"Android phone that belongs to number {self.phone_number}"

    def set_passcode(self, passcode):

        self.passcode = passcode

    def unlock_phone(self, passcode):
        if passcode == self.passcode:
            print('Phone unlocked')    
    
    def view_battery_life(self):
        print(f"Battery Life: {self.battery}")

    def charge_phone(self, charging_amount):
        self.battery += charging_amount
        if self.battery > 100:
            self.battery: 100
        
frank_phone = Android('888-777-3333', 'black')

frank_phone.view_battery_life()
frank_phone.call('999-999-9999')


class IPhone(Phone):
    def __init__ (self, phone_number, color):
        super().__init__(phone_number, color)
        self.passcode = True
        self.charger = True
        self.headphones = False
        self.battery = 50
    def __str__(self):
        return f"iPhone that belongs to number {self.phone_number}"    
    def unlock_phone(self, passcode):
        if self.passcode == True:
            print('Welcome Back!')
        else:
            print('Your Phone is locked')
    def charge_phone(self):
        if  self.charger == True:
            self.battery += 10
            print(f"your battery is at {self.battery} ")
        else: 
            print("You don't have a charger!")
    def itunes( self):
        if self.headphones == True:
            print('Play some tunes')
        else:
            print("You dont headphones!")

lev_phone = IPhone('888-777-3333', 'gold')
lev_phone.charge_phone()
lev_phone.itunes()