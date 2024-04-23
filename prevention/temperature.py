import utime
import _thread
from sensors_and_modules import gps_module
from sensors_and_modules import gsm_module

"""
is_in_range = number in range(1, 21)
"""
class Temperature:
    """
        This Class is used to store and monitor changes in temperature
    """
    def _init_(this):
        this.temperature_readings = []
        this.relative_humidity_readings = []
        this.size = 3
        this.temperature_ranges = [
            [19.7,20.5],
            [20.5,21.7],
            [21.7,22.9],
            [22.9,24.2],
            [24.2,26.0],
            [26.0,26.5],
            [26.5,27.0]
            ]
        this.relative_humidity_ranges = [
            [45,82],
            [30,77],
            [28,71],
            [23,67],
            [24,58],
            [21,52],
            [20,27]
            ]
        
    def add_readings(this,temperature,relative_humidity):
        """
        Add a temperature reading from the temperature sensor to list of 
        temperature readings.  This method triggers a process in a seperate 
        thread for confirming that the temperature present in the car can cause
        heatstroke. The thread confirms if temperature is still above threshold
        after 3 mins
        """
        if len(this.temperature_readings) < this.size:
            this.temperature_readings.append(temperature)
            this.relative_humidity_readings.append(relative_humidity)
        else:
            this.temperature_readings.pop(0)
            this.temperature_readings.append(temperature)
            this.relative_humidity_readings.append(relative_humidity)

    def risk_detector(this):
        """
        This method waits for three minutes and checks if there is current 
        temperature is above normal levels
        """
        if this.temperature_readings[len(this.temperature_readings)-2]>this.temperature_threshold and this.temperature_readings[len(this.temperature_readings)-1]>this.temperature_threshold:
            return gsm_module.make_call()
        else:
            return 