class SmartPhones:
    def __init__(self, name, color, memory, battery = 0):
        self.name = name
        self.color = color
        self.memory = memory
        self.battery = battery

    def __str__(self):
        return f'{self.name} {self.memory}'

    def charge(self,plus_battery):
        self.battery += plus_battery
        return self.battery

class Iphone(SmartPhones):
    def __init__(self, name, color, memory,ios, battery = 0):
        super().__init__(name, color, memory, battery)
        self.ios = ios

    def send_imessage(self, message):
        return f'sending {message} from {self.name} {self.memory}'

class Samsung(SmartPhones):
    def __init__(self, name, color, memory, android, battery = 0) :
        super().__init__(name, color, memory, battery)
        self.android = android

    def show_time(self):
        from datetime import datetime
        current_time = datetime.now()
        return current_time.time()

phone = SmartPhones('generic', 'blue', '128GB') 
print(phone) 

print(phone.battery) 
phone.charge(20) 
print(phone.battery) 

iphone7 = Iphone('Iphone 7', 'gold', '128gb', '12.1.3') 
print(iphone7)
print(iphone7.send_imessage('hello')) 

samsung21 = Samsung('Samsung A21', 'black', '256gb', 'Oreo') 
print(samsung21.show_time())