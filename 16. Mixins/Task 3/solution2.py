class Clock:
    def current_time(self):
        import time
        a = time.localtime()
        current_time = time.strftime("%H:%M:%S", a)
        print(current_time)
    
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