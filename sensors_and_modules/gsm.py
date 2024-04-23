import time
from machine import UART, Pin

# Initialize UART
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Function to send AT commands and receive response
def send_at_command(command, wait_time=2000):
    uart.write(command + '\r\n')
    time.sleep_ms(wait_time)
    response = uart.read()
    return response

# Function to make a call
def make_call(phone_number):
    send_at_command("ATD{};".format(phone_number))  # ; indicates voice call
    time.sleep(30)  # Duration of the call (in seconds)
    send_at_command("ATH")  # Hang up the call

# Call a phone number
make_call("+1234567890")  # Replace with your desired phone number