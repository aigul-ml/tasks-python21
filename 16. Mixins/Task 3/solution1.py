class Clock:
    def current_time(self):
        from datetime import datetime 
        a = datetime.now().strftime("%H:%M:%S")
        print(a)
    
class Alarm:
    def on(self):
       print('Будильник включен')
           
    def off(self):
        print('Будильник выключен')

class AlarmClock(Clock, Alarm):
    def alarm_on(self):
        self.on()


clock = AlarmClock()

clock.current_time() 
clock.alarm_on() 