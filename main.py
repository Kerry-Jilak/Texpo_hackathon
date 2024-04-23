import utime
import _thread
from prevention import temperature
from prevention import gas
from sensors_and_modules import temperature_humidity_sensor
import machine

button = machine.Pin(15,machine.Pin.OUT)


# Classes
Temp = temperature.Temperature()


# Heastroke Prevention
def temp_rh():
    while True:
       temp,hum = temperature_humidity_sensor.measure_tmp_rh() 
       Temp.add_readings(temp,hum)
       Temp.risk_detector()

def start_temp_rh_thread():
    _thread.start_new_thread(temp_rh,())




# Suffocation Prevention
def suffocation_prevention():
    while True:
        pass




# Checking for human presence
def Check_for_human_presence():
    pass
    if human_present:
       suffocation_prevention()
       start_temp_rh_thread()
       



# Checking for Whether door is closed
button.irq(trigger=machine.Pin.IRQ_RISING, handler = Check_for_human_presence)
