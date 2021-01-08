class Car():
    """ This is a car class that will display the make, model and color """
    def __init__(self, make, model, color):
        self.make=make
        self.model=model
        self.color=color
        self.gas = 100
    def __str__(self):
        return "{}, {}, {}".format(self.make, self.model, self.color)
    def drive(self):
        self.gas -= 10
        print(self.gas)
    def fill_tank(self):
        self.gas = 100
    def check_gas(self):
        print(f" Gas handle: {self.gas}")

car1 = Car('Mercedes','C300', 'white')
car1.drive()
car1.drive()
car1.check_gas()
car1.fill_tank()
car1.check_gas()
# print(car1)

# help(car1)
class Bartender():
    def __init__(self, name, bar):
        self.name = name
        self.bar = bar
        self.schedule =['Thursday','Friday','Saturday','Sunday']
    def __str__(self):
        return"{}, {}".format(self.name, self.bar)
    def is_late(self):
            for i in range(len(self.schedule)):
                if i == 3:
                    print(f"{self.name} is late today beacuse it is {self.schedule[i]}")
                else: 
                    print(f"{self.name} is on time today!!")  
    def clock_in(self):
        print("What can I get for you?")
    def clock_out(self):
        print("See you later")                      

bartender1 = Bartender('Alex', 'Milanos')
bartender1.is_late()