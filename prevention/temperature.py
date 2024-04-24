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
        temperature readings.
        """
        if len(this.temperature_readings) < this.size:
            this.temperature_readings.append(temperature)
            this.relative_humidity_readings.append(relative_humidity)
        else:
            this.temperature_readings.pop(0)
            this.temperature_readings.append(temperature)
            this.relative_humidity_readings.append(relative_humidity)
    
    def get_reading_averages(this):
        a = 0
        b = 0
        c = 0
        d = 0
        for x in this.temperature_readings:
            a += 1
            b += x
        temp_average = b/a
        
        for z in this.relative_humidity_readings:
            c += 1
            d += z
        rh_average = d/c
            
        return temp_average, rh_average

    def risk_detector(this):
        """
        This method check if there temperature is to high. It triggers an alert when
        temperatures are too high
        """
        
        temp_average, rh_average = this.get_reading_averages()
        
        for x in range(7):
            if temp_average in range(this.temperature_ranges[x][0],this.temperature_ranges[x][1]) and rh_average in range(this.relative_humidity_ranges[x][0],this.relative_humidity_ranges[x][1]):
                continue
            else:
                gsm_module.make_call()
                # Get gps data for sms
                # Sound Alarm
                return gsm_module.send_sms()