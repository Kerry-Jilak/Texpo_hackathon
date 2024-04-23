from machine import Pin
from time import sleep
import dht

sensor = dht.DHT11(Pin(22))

def measure_tmp_rh():
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        return temp,hum
    except:
        return 0, 0
