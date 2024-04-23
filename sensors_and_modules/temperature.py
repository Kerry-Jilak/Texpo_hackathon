import time
import _thread
from gsm import make_call


class Temperature:
    """
        This Class is used to store and monitor changes in temperature
    """
    def _init_(this):
        this.temperature_readings = []
        this.temperature_threshold = 40
        this.size = 20
    def add(this,temperature):
        """
        Add a temperature reading from the temperature sensor to list of 
        temperature readings.  This method triggers a process in a seperate 
        thread for confirming that the temperature present in the car can cause
        heatstroke. The thread confirms if temperature is still above threshold
        after 3 mins
        """
        print("Current Temperature",str(temperature))
        if len(this.temperature_readings) < this.size:
            this.temperature_readings.append(temperature)
            if temperature > this.temperature_threshold:
                thread_1 = threading.Thread(target=this.risk_detector)
                thread_1.start()
        else:
            this.temperature_readings.pop(0)
            this.temperature_readings.append(temperature)
            if temperature > this.temperature_threshold:
                thread_1 = threading.Thread(target=this.risk_detector)
                thread_1.start()
    def risk_detector(this):
        """
        This method waits for three minutes and checks if there is current 
        temperature is above normal levels
        """
        time.sleep(20)
        if this.temperature_readings[len(this.temperature_readings)-2]>this.temperature_threshold and this.temperature_readings[len(this.temperature_readings)-1]>this.temperature_threshold:
            return print("Alert Car Is overheating")
        else:
            return print("No risk")